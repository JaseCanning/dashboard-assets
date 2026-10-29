const fs = require('fs');

const faviconBlock = `  <!-- Favicons -->
  <link rel="icon" type="image/svg+xml" href="/favicon.svg">
  <link rel="alternate icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
  <link rel="alternate icon" type="image/png" sizes="16x16" href="/favicon-16x16.png">
  <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
  <link rel="manifest" href="/site.webmanifest">
  <meta name="theme-color" content="#4f46e5">`;

const files = [
  '/srv/apps/dashboard/public/login.html',
  '/srv/apps/dashboard/public/index.html'
];

for (const f of files) {
  if (!fs.existsSync(f)) {
    console.error('File not found:', f);
    continue;
  }
  let html = fs.readFileSync(f, 'utf8');
  if (html.includes('href="/favicon.svg"')) {
    console.log(f, 'already contains favicon link block.');
    continue;
  }
  
  // Insert immediately after </title>
  if (html.includes('</title>')) {
    html = html.replace('</title>', '</title>\n' + faviconBlock);
    fs.writeFileSync(f, html, 'utf8');
    console.log('Successfully updated:', f);
  } else {
    console.warn('Could not find </title> in:', f);
  }
}
