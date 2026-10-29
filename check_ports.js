const http = require("http");

const ports = [
  { name: "Swarovski", port: 3006 },
  { name: "Barclays", port: 3004 },
  { name: "Maha C9000", port: 3005 },
  { name: "Gousto", port: 3002 },
  { name: "EV Calculator", port: 3001 },
  { name: "Movie & TV", port: 3003 }
];

async function check(url) {
  return new Promise((resolve) => {
    http.get(url, (res) => {
      resolve({ status: res.statusCode, contentType: res.headers["content-type"] });
    }).on("error", (e) => {
      resolve({ status: "ERR", error: e.message });
    });
  });
}

async function run() {
  for (const p of ports) {
    const svgRes = await check(`http://127.0.0.1:${p.port}/favicon.svg`);
    const icoRes = await check(`http://127.0.0.1:${p.port}/favicon.ico`);
    console.log(`${p.name} (Port ${p.port}):`);
    console.log(`  favicon.svg -> ${svgRes.status} (${svgRes.contentType || svgRes.error})`);
    console.log(`  favicon.ico -> ${icoRes.status} (${icoRes.contentType || icoRes.error})`);
  }
}

run();
