const fs = require("fs");

const file = "/srv/apps/dashboard/server.js";
const bak = "/srv/apps/dashboard/server.js.bak";

if (!fs.existsSync(bak)) {
  fs.copyFileSync(file, bak);
  console.log(`Backed up ${file} to ${bak}`);
}

let code = fs.readFileSync(file, "utf8");

const target = `function requireAuth(req, res, next) {
  if (req.session && req.session.user) {
    return next();
  }`;

const replacement = `function requireAuth(req, res, next) {
  if (req.session && req.session.user) {
    return next();
  }
  // Allow unauthenticated access to favicon and manifest assets across all sub-apps
  if (
    req.path.endsWith("/favicon.svg") ||
    req.path.endsWith("/favicon.ico") ||
    req.path.includes("favicon") ||
    req.path.endsWith("/apple-touch-icon.png") ||
    req.path.endsWith("/site.webmanifest")
  ) {
    return next();
  }`;

if (code.includes(target) && !code.includes("Allow unauthenticated access to favicon")) {
  code = code.replace(target, replacement);
  fs.writeFileSync(file, code, "utf8");
  console.log("Successfully patched requireAuth in server.js");
} else if (code.includes("Allow unauthenticated access to favicon")) {
  console.log("requireAuth already patched in server.js");
} else {
  console.error("Could not find requireAuth target in server.js");
  process.exit(1);
}
