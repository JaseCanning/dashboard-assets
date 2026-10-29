const fs = require("fs");
const path = require("path");

const targets = [
  {
    name: "Swarovski Collection",
    file: "/srv/apps/swarovski-collection/public/index.html",
    themeColor: "#0f766e"
  },
  {
    name: "Barclays Transactions",
    file: "/srv/apps/barclays-transactions/public/index.html",
    themeColor: "#0284c7"
  },
  {
    name: "Maha C9000",
    file: "/srv/apps/maha-c9000-battery-charger/public/index.html",
    themeColor: "#1e3a8a"
  },
  {
    name: "Gousto Recipe Search",
    file: "/srv/apps/gousto-recipe-search/index.html",
    themeColor: "#dc2626"
  },
  {
    name: "EV Charging Cost Calculator",
    file: "/srv/apps/ev-charging-cost-calculator/dist/index.html",
    themeColor: "#10b981"
  },
  {
    name: "Movie & TV Database",
    file: "/srv/apps/movie-and-tv-database/dist/index.html",
    themeColor: "#4338ca"
  }
];

for (const t of targets) {
  if (!fs.existsSync(t.file)) {
    console.error(`File not found: ${t.file}`);
    continue;
  }
  
  // Create backup
  const bak = `${t.file}.bak`;
  if (!fs.existsSync(bak)) {
    fs.copyFileSync(t.file, bak);
    console.log(`Backed up ${t.file} to ${bak}`);
  }
  
  let html = fs.readFileSync(t.file, "utf8");
  
  // Remove any existing favicon or theme-color tags
  html = html.replace(/<link[^>]+rel=["'](?:shortcut )?icon["'][^>]*>\s*/gi, "");
  html = html.replace(/<link[^>]+rel=["']alternate icon["'][^>]*>\s*/gi, "");
  html = html.replace(/<meta[^>]+name=["']theme-color["'][^>]*>\s*/gi, "");
  
  const faviconBlock = `  <link rel="icon" type="image/svg+xml" href="./favicon.svg" />\n  <link rel="alternate icon" href="./favicon.ico" />\n  <meta name="theme-color" content="${t.themeColor}" />\n`;
  
  if (html.includes("<head>")) {
    html = html.replace("<head>", `<head>\n${faviconBlock}`);
  } else if (html.includes("<head ")) {
    html = html.replace(/<head[^>]*>/, `$& \n${faviconBlock}`);
  } else {
    console.error(`No <head> tag in ${t.file}`);
    continue;
  }
  
  fs.writeFileSync(t.file, html, "utf8");
  console.log(`Updated ${t.name} (${t.file})`);
}
