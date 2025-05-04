const fetch = require("node-fetch");
const iconv = require("iconv-lite");

const url = "https://api.syosetu.com/novelapi/api/";

fetch(url)
    .then(res => res.buffer())
    .then(buffer => {
    const decoded = iconv.decode(buffer, "Shift_JIS");
    // 余計な先頭行（ヘッダーやBOM）があるか確認
    const jsonStart = decoded.indexOf("[");
    if (jsonStart === -1) {
        throw new Error("JSONの開始位置が見つかりません");
    }
    const jsonText = decoded.slice(jsonStart);
    return JSON.parse(jsonText);
    })
    .then(data => {
    console.log("取得したデータ:", data);
    })
    .catch(err => {
    console.error("エラーが発生しました:", err);
    });