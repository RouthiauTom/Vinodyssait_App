import {readdir,readFile,lstat} from 'node:fs/promises';
import assert from 'node:assert/strict';
const allowed=new Set(['index.html','sw.js','manifest.webmanifest','assets','fonts','icons']);
for(const entry of await readdir('dist'))assert(allowed.has(entry),`Fichier inattendu dans dist : ${entry}`);
async function inspect(dir){for(const entry of await readdir(dir)){const path=`${dir}/${entry}`;const info=await lstat(path);assert(!info.isSymbolicLink(),`Lien symbolique interdit : ${path}`);assert(!/(^\.env|^\.git$|\.zip$|\.csv$)/i.test(entry),`Référence source interdite : ${path}`);if(info.isDirectory())await inspect(path);}}
await inspect('dist');
const html=await readFile('dist/index.html','utf8');
assert(html.includes('./manifest.webmanifest'));assert(!/(?:src|href)="\/(?!\/)/.test(html),'Chemin absolu incompatible avec un sous-dossier Pages');
const manifest=JSON.parse(await readFile('dist/manifest.webmanifest','utf8'));
assert.equal(manifest.scope,'./');assert.equal(manifest.start_url,'./');
await readFile('dist/sw.js');
console.log('GitHub Pages : artefact statique contrôlé, références locales exclues, chemins relatifs valides.');
