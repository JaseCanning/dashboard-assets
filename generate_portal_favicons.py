import os
from PIL import Image, ImageDraw

def create_portal_icon(size):
    # Supersample at 2x for clean antialiasing
    scale = 2
    dim = size * scale
    
    # 1. Background squircle with diagonal gradient (indigo-600 to violet-500)
    c1 = (79, 70, 229, 255)   # #4f46e5 (indigo-600)
    c2 = (139, 92, 246, 255)  # #8b5cf6 (violet-500)
    cmid = ((c1[0] + c2[0]) // 2, (c1[1] + c2[1]) // 2, (c1[2] + c2[2]) // 2, 255)
    
    # Fast 2x2 gradient resized with bicubic interpolation
    grad_base = Image.new('RGBA', (2, 2))
    # Bottom-left to top-right
    grad_base.putpixel((0, 0), cmid)  # top-left
    grad_base.putpixel((1, 0), c2)    # top-right (violet)
    grad_base.putpixel((0, 1), c1)    # bottom-left (indigo)
    grad_base.putpixel((1, 1), cmid)  # bottom-right
    grad_img = grad_base.resize((dim, dim), Image.Resampling.BICUBIC)
    
    # Squircle mask
    corner_radius = int(dim * 0.225)
    mask = Image.new('L', (dim, dim), 0)
    mask_draw = ImageDraw.Draw(mask)
    mask_draw.rounded_rectangle([0, 0, dim - 1, dim - 1], radius=corner_radius, fill=255)
    grad_img.putalpha(mask)
    
    # 2. Subtle light border
    border_draw = ImageDraw.Draw(grad_img)
    border_w = max(1, int(dim * 0.015))
    border_r = max(1, corner_radius - border_w)
    border_draw.rounded_rectangle(
        [border_w, border_w, dim - 1 - border_w, dim - 1 - border_w],
        radius=border_r,
        outline=(255, 255, 255, 45),
        width=border_w
    )
    
    # 3. Shapes
    content_size = dim * 0.58
    cx = dim / 2.0
    cy = dim / 2.0
    ox = cx - content_size / 2.0
    oy = cy - content_size / 2.0
    
    def to_canvas(vx, vy):
        return (ox + (vx / 512.0) * content_size, oy + (vy / 512.0) * content_size)
    
    white = (255, 255, 255, 255)
    shapes_canvas = Image.new('RGBA', (dim, dim), (0, 0, 0, 0))
    s_draw = ImageDraw.Draw(shapes_canvas)
    
    # Circle (bottom left)
    c_center = to_canvas(128, 384)
    c_radius = (128.0 / 512.0) * content_size
    s_draw.ellipse(
        [c_center[0] - c_radius, c_center[1] - c_radius, c_center[0] + c_radius, c_center[1] + c_radius],
        fill=white
    )
    
    # Square (bottom right)
    sq_tl = to_canvas(288, 272)
    sq_br = to_canvas(472, 456)
    sq_rad = max(1, int((40.0 / 512.0) * content_size))
    s_draw.rounded_rectangle([sq_tl[0], sq_tl[1], sq_br[0], sq_br[1]], radius=sq_rad, fill=white)
    
    # Triangle (top)
    p_top = to_canvas(288, 22)
    p_left = to_canvas(188, 192)
    p_right = to_canvas(388, 192)
    s_draw.polygon([p_top, p_left, p_right], fill=white)
    
    grad_img.alpha_composite(shapes_canvas)
    
    if scale > 1:
        return grad_img.resize((size, size), Image.Resampling.LANCZOS)
    return grad_img

def main():
    target_dir = os.path.dirname(os.path.abspath(__file__))
    sizes = [16, 32, 48, 64, 180, 192, 512]
    icons = {}
    for s in sizes:
        icon = create_portal_icon(s)
        icons[s] = icon
        if s == 16:
            icon.save(os.path.join(target_dir, "favicon-16x16.png"), format="PNG")
        elif s == 32:
            icon.save(os.path.join(target_dir, "favicon-32x32.png"), format="PNG")
        elif s == 180:
            icon.save(os.path.join(target_dir, "apple-touch-icon.png"), format="PNG")
        elif s == 192:
            icon.save(os.path.join(target_dir, "android-chrome-192x192.png"), format="PNG")
        elif s == 512:
            icon.save(os.path.join(target_dir, "android-chrome-512x512.png"), format="PNG")
            
    ico_sizes = [16, 32, 48, 64]
    ico_images = [icons[s] for s in ico_sizes]
    ico_images[0].save(
        os.path.join(target_dir, "favicon.ico"),
        format="ICO",
        sizes=[(s, s) for s in ico_sizes],
        append_images=ico_images[1:]
    )
    print("SUCCESS: All icons generated successfully.")

if __name__ == "__main__":
    main()
