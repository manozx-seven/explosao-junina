/* ============================================================
 * patch_docx.js — troca textos dentro de um .docx, sem dependência nenhuma.
 *
 * Por que existe: o `gen_socio.py` é a fonte de verdade do Plano de
 * Implementação, mas regerar exige `python-docx`, e nem sempre a máquina tem pip
 * (foi o caso em 28/07/2026). Além disso o material de DIVULGAÇÃO não tem
 * gerador — é editado avulso. Sem uma ferramenta assim, mudar um valor no
 * sistema e não conseguir mexer nos documentos deixa os dois divergentes, que é
 * exatamente o erro que o CONTEXTO.md §8-A do Sócio Torcedor manda evitar.
 *
 * Um .docx é um zip com `word/document.xml` dentro. Este script lê o zip,
 * troca o texto e regrava. Só encosta em `document.xml`; o resto passa intacto.
 *
 * Uso:
 *   node patch_docx.js <arquivo.docx> "de|para" "de|para" ...
 *
 * A troca é feita SOMENTE dentro de <w:t>…</w:t> (o texto visível), então nunca
 * corrompe marcação. Avisa quando um "de" não foi encontrado — normalmente
 * significa que o Word quebrou aquele trecho em vários runs e é preciso um
 * pedaço menor.
 * ============================================================ */
const fs = require('fs');
const zlib = require('zlib');

// ---------- CRC32 (o zip exige) ----------
const TABELA_CRC = (() => {
  const t = new Int32Array(256);
  for (let i = 0; i < 256; i++) {
    let c = i;
    for (let k = 0; k < 8; k++) c = (c & 1) ? (0xEDB88320 ^ (c >>> 1)) : (c >>> 1);
    t[i] = c;
  }
  return t;
})();
function crc32(buf) {
  let c = -1;
  for (let i = 0; i < buf.length; i++) c = TABELA_CRC[(c ^ buf[i]) & 0xFF] ^ (c >>> 8);
  return (c ^ -1) >>> 0;
}

// ---------- leitura ----------
function lerZip(buf) {
  const entradas = [];
  for (let i = 0; i < buf.length - 3; i++) {
    if (buf.readUInt32LE(i) !== 0x04034b50) continue;
    const metodo = buf.readUInt16LE(i + 8);
    const compSize = buf.readUInt32LE(i + 18);
    const nomeLen = buf.readUInt16LE(i + 26);
    const extraLen = buf.readUInt16LE(i + 28);
    const nome = buf.slice(i + 30, i + 30 + nomeLen).toString('utf8');
    const ini = i + 30 + nomeLen + extraLen;
    if (!compSize || !nome) continue;
    const bruto = buf.slice(ini, ini + compSize);
    let dados;
    try { dados = metodo === 8 ? zlib.inflateRawSync(bruto) : bruto; }
    catch (e) { continue; }
    entradas.push({ nome, dados });
  }
  return entradas;
}

// ---------- escrita ----------
function escreverZip(entradas) {
  const locais = [];
  const central = [];
  let offset = 0;

  for (const e of entradas) {
    const nome = Buffer.from(e.nome, 'utf8');
    const comprimido = zlib.deflateRawSync(e.dados, { level: 9 });
    const crc = crc32(e.dados);

    const local = Buffer.alloc(30);
    local.writeUInt32LE(0x04034b50, 0);   // assinatura
    local.writeUInt16LE(20, 4);           // versão necessária
    local.writeUInt16LE(0, 6);            // flags
    local.writeUInt16LE(8, 8);            // método: deflate
    local.writeUInt16LE(0, 10);           // hora
    local.writeUInt16LE(0x21, 12);        // data (1980-01-01, determinístico)
    local.writeUInt32LE(crc, 14);
    local.writeUInt32LE(comprimido.length, 18);
    local.writeUInt32LE(e.dados.length, 22);
    local.writeUInt16LE(nome.length, 26);
    local.writeUInt16LE(0, 28);           // sem campo extra
    locais.push(local, nome, comprimido);

    const cab = Buffer.alloc(46);
    cab.writeUInt32LE(0x02014b50, 0);
    cab.writeUInt16LE(20, 4);             // versão de quem criou
    cab.writeUInt16LE(20, 6);             // versão necessária
    cab.writeUInt16LE(0, 8);
    cab.writeUInt16LE(8, 10);
    cab.writeUInt16LE(0, 12);
    cab.writeUInt16LE(0x21, 14);
    cab.writeUInt32LE(crc, 16);
    cab.writeUInt32LE(comprimido.length, 20);
    cab.writeUInt32LE(e.dados.length, 24);
    cab.writeUInt16LE(nome.length, 28);
    cab.writeUInt16LE(0, 30);             // extra
    cab.writeUInt16LE(0, 32);             // comentário
    cab.writeUInt16LE(0, 34);             // disco
    cab.writeUInt16LE(0, 36);             // atributos internos
    cab.writeUInt32LE(0, 38);             // atributos externos
    cab.writeUInt32LE(offset, 42);        // onde está o cabeçalho local
    central.push(cab, nome);

    offset += local.length + nome.length + comprimido.length;
  }

  const dirBuf = Buffer.concat(central);
  const fim = Buffer.alloc(22);
  fim.writeUInt32LE(0x06054b50, 0);
  fim.writeUInt16LE(0, 4);
  fim.writeUInt16LE(0, 6);
  fim.writeUInt16LE(entradas.length, 8);
  fim.writeUInt16LE(entradas.length, 10);
  fim.writeUInt32LE(dirBuf.length, 12);
  fim.writeUInt32LE(offset, 16);
  fim.writeUInt16LE(0, 20);

  return Buffer.concat([Buffer.concat(locais), dirBuf, fim]);
}

// ---------- troca de texto ----------
/**
 * Aplica as trocas só no conteúdo de <w:t>, nunca na marcação.
 *
 * Dois modos, e o exato existe por um motivo concreto: quando os valores de uma
 * tabela deslizam (R$ 5→10, 10→20, 20→30), a troca por substring cascateia — a
 * célula que virou "R$ 10" seria pega pela regra seguinte e viraria "R$ 20".
 *
 *   "^texto$"  -> casa apenas se o run INTEIRO for exatamente isso (célula de
 *                 tabela, valor solto). Imune a cascata: cada run é trocado no
 *                 máximo uma vez.
 *   "texto"    -> substring, para trechos dentro de uma frase maior.
 */
function trocarNoTexto(xml, trocas) {
  const contagem = new Map(trocas.map((t) => [t.de, 0]));
  // O `(?:\s[^>]*)?` é essencial: `<w:t[^>]*>` casaria também `<w:tcPr>`,
  // `<w:tbl>` e `<w:tc>`, e o script sairia editando MARCAÇÃO como se fosse
  // texto. Exigindo `>` logo depois de `<w:t` ou um espaço, só o elemento de
  // texto de verdade entra.
  const saida = xml.replace(/(<w:t(?:\s[^>]*)?>)([\s\S]*?)(<\/w:t>)/g, (todo, abre, texto, fecha) => {
    let t = texto;
    let jaTrocado = false;
    for (const { de, para } of trocas) {
      const exato = de.startsWith('^') && de.endsWith('$');
      if (exato) {
        const alvo = de.slice(1, -1);
        if (!jaTrocado && t === alvo) {
          contagem.set(de, contagem.get(de) + 1);
          t = para;
          jaTrocado = true;   // trava a cascata
        }
      } else if (t.includes(de)) {
        contagem.set(de, contagem.get(de) + t.split(de).length - 1);
        t = t.split(de).join(para);
      }
    }
    return abre + t + fecha;
  });
  return { xml: saida, contagem };
}

// ---------- principal ----------
function main() {
  const [arquivo, ...pares] = process.argv.slice(2);
  if (!arquivo || !pares.length) {
    console.error('uso: node patch_docx.js <arquivo.docx> "de|para" ["de|para" ...]');
    process.exit(2);
  }
  const trocas = pares.map((p) => {
    const i = p.indexOf('|');
    if (i < 0) { console.error(`par sem "|": ${p}`); process.exit(2); }
    return { de: p.slice(0, i), para: p.slice(i + 1) };
  });

  const entradas = lerZip(fs.readFileSync(arquivo));
  const doc = entradas.find((e) => e.nome === 'word/document.xml');
  if (!doc) { console.error('não achei word/document.xml — isso é um .docx?'); process.exit(1); }

  const { xml, contagem } = trocarNoTexto(doc.dados.toString('utf8'), trocas);
  doc.dados = Buffer.from(xml, 'utf8');

  let faltou = 0;
  for (const { de, para } of trocas) {
    const n = contagem.get(de);
    if (!n) { faltou++; console.log(`  ⚠ NÃO ENCONTRADO: "${de}"`); }
    else console.log(`  ${n}x  "${de}" → "${para}"`);
  }

  fs.writeFileSync(arquivo, escreverZip(entradas));
  console.log(`\n${arquivo}\n${entradas.length} partes regravadas${faltou ? `, ${faltou} troca(s) sem efeito` : ''}.`);
  process.exit(faltou ? 1 : 0);
}

if (require.main === module) main();
module.exports = { lerZip, escreverZip, trocarNoTexto };
