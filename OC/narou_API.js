import fetch from 'node-fetch';

async function callApi() {
    const res = await fetch("https://api.syosetu.com/novelapi/api/?of=t-w-s&lim=200");
    const text = await res.text();
    console.log(text);
}

callApi();