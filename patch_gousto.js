const fs = require("fs");

const file = "/srv/apps/gousto-recipe-search/mcp_server.py";
const bak = "/srv/apps/gousto-recipe-search/mcp_server.py.bak";

if (!fs.existsSync(bak)) {
  fs.copyFileSync(file, bak);
  console.log(`Backed up ${file} to ${bak}`);
}

let content = fs.readFileSync(file, "utf8");

if (!content.includes("favicon_svg_endpoint")) {
  const target = `INDEX_HTML_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "index.html")`;
  const addition = `INDEX_HTML_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "index.html")
FAVICON_SVG_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "favicon.svg")
FAVICON_ICO_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "favicon.ico")


@server.custom_route("/favicon.svg", methods=["GET"])
async def favicon_svg_endpoint(request: Request):
    """Serve favicon.svg."""
    if os.path.exists(FAVICON_SVG_PATH):
        return FileResponse(FAVICON_SVG_PATH, media_type="image/svg+xml")
    return Response(status_code=404)


@server.custom_route("/favicon.ico", methods=["GET"])
async def favicon_ico_endpoint(request: Request):
    """Serve favicon.ico."""
    if os.path.exists(FAVICON_ICO_PATH):
        return FileResponse(FAVICON_ICO_PATH, media_type="image/x-icon")
    elif os.path.exists(FAVICON_SVG_PATH):
        return FileResponse(FAVICON_SVG_PATH, media_type="image/svg+xml")
    return Response(status_code=404)`;

  content = content.replace(target, addition);
  fs.writeFileSync(file, content, "utf8");
  console.log("Successfully patched mcp_server.py with favicon endpoints.");
} else {
  console.log("Favicon endpoints already present in mcp_server.py.");
}
