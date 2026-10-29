# Jason Canning Portal Dashboard Favicon

These favicon assets match the branding and visual identity of the **Jason Canning Personal Application Gateway** (`https://jasoncanning.uk`):
- **Colors**: Vibrant gradient from Indigo (`#4f46e5`) to Violet (`#8b5cf6`).
- **Icon**: Crisp white FontAwesome `fa-shapes` geometric cluster (circle, square, and triangle) on a modern rounded squircle container.
- **Form-factors**: Scalable vector SVG (`favicon.svg`), multi-size Windows/browser ICO (`favicon.ico`), 32x32 & 16x16 PNGs, 180x180 Apple touch icon, and Web App manifest.

---

## 🚀 How to deploy to your Proxmox server (`/srv/apps/`)

### Option 1: SCP / Copy from this machine to the Proxmox server
From your PowerShell terminal on this machine:
```powershell
# Copy the assets to your gateway's public static folder on Proxmox
scp "C:\Projects\Personal Projects\dashboard-assets\favicon*" jason@10.0.0.207:/srv/apps/gateway/public/
scp "C:\Projects\Personal Projects\dashboard-assets\apple-touch-icon.png" jason@10.0.0.207:/srv/apps/gateway/public/
scp "C:\Projects\Personal Projects\dashboard-assets\site.webmanifest" jason@10.0.0.207:/srv/apps/gateway/public/
```
*(Adjust `/srv/apps/gateway/public/` to match your gateway service folder if named differently, e.g., `/srv/apps/portal/public/`)*

---

### Option 2: Add to your Gateway's HTML `<head>`
In your gateway's `login.html` and `dashboard.html` (or `index.html`), add these links inside `<head>`:

```html
<!-- Favicons -->
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<link rel="alternate icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
<link rel="alternate icon" type="image/png" sizes="16x16" href="/favicon-16x16.png">
<link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<meta name="theme-color" content="#4f46e5">
```

---

### Option 3: Express Backend Route (if not using express.static)
If your gateway Express app handles static files manually, ensure it serves the static files or has direct routes:
```javascript
import path from 'path';

// Serve public directory
app.use(express.static(path.join(__dirname, 'public')));

// Or explicit fallback route
app.get('/favicon.ico', (req, res) => res.sendFile(path.join(__dirname, 'public', 'favicon.ico')));
app.get('/favicon.svg', (req, res) => res.sendFile(path.join(__dirname, 'public', 'favicon.svg')));
```
