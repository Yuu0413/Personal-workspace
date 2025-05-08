import fetch from 'node-fetch';
import fs from 'fs';

async function callApi() {
    const res = await fetch("https://api.syosetu.com/novelapi/api/?out=json&of=t-w-s&lim=200");
    const json = await res.json();

    const novels = json.slice(1);

    fs.writeFileSync('OC/novel_info.json', JSON.stringify(novels, null, 2));
    console.log(`${novels.length} 件の小説データを保存しました`);
}

callApi();