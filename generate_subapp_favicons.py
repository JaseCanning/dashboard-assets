import os
from PIL import Image, ImageDraw

def create_gradient_squircle(dim, c1, c2, border_color=(255, 255, 255, 45)):
    cmid = ((c1[0] + c2[0]) // 2, (c1[1] + c2[1]) // 2, (c1[2] + c2[2]) // 2, 255)
    grad_base = Image.new('RGBA', (2, 2))
    grad_base.putpixel((0, 0), cmid)
    grad_base.putpixel((1, 0), c2)
    grad_base.putpixel((0, 1), c1)
    grad_base.putpixel((1, 1), cmid)
    grad_img = grad_base.resize((dim, dim), Image.Resampling.BICUBIC)
    
    corner_radius = int(dim * 0.225)
    mask = Image.new('L', (dim, dim), 0)
    mask_draw = ImageDraw.Draw(mask)
    mask_draw.rounded_rectangle([0, 0, dim - 1, dim - 1], radius=corner_radius, fill=255)
    grad_img.putalpha(mask)
    
    border_draw = ImageDraw.Draw(grad_img)
    border_w = max(1, int(dim * 0.015))
    border_r = max(1, corner_radius - border_w)
    border_draw.rounded_rectangle(
        [border_w, border_w, dim - 1 - border_w, dim - 1 - border_w],
        radius=border_r,
        outline=border_color,
        width=border_w
    )
    return grad_img

def draw_swarovski(size):
    scale = 2
    dim = size * scale
    c1 = (4, 47, 46, 255)     # #042f2e
    c2 = (15, 118, 110, 255)  # #0f766e
    img = create_gradient_squircle(dim, c1, c2, (94, 234, 212, 70))
    draw = ImageDraw.Draw(img)
    
    # Diamond gem
    cx, cy = dim / 2.0, dim / 2.0
    r = dim * 0.30
    # Top table
    top_y = cy - r
    mid_y = cy - r * 0.3
    bot_y = cy + r
    
    w_top = r * 0.7
    w_mid = r * 1.1
    
    # Draw facets
    table = [(cx - w_top, top_y), (cx + w_top, top_y), (cx + w_mid * 0.8, mid_y), (cx - w_mid * 0.8, mid_y)]
    draw.polygon(table, fill=(255, 255, 255, 240))
    # Bottom pavilion
    left_bot = [(cx - w_mid * 0.8, mid_y), (cx, mid_y), (cx, bot_y)]
    right_bot = [(cx, mid_y), (cx + w_mid * 0.8, mid_y), (cx, bot_y)]
    draw.polygon(left_bot, fill=(45, 212, 191, 230))
    draw.polygon(right_bot, fill=(20, 184, 166, 240))
    
    if scale > 1:
        return img.resize((size, size), Image.Resampling.LANCZOS)
    return img

def draw_barclays(size):
    scale = 2
    dim = size * scale
    c1 = (0, 57, 93, 255)     # #00395d
    c2 = (2, 132, 199, 255)   # #0284c7
    img = create_gradient_squircle(dim, c1, c2, (255, 255, 255, 45))
    draw = ImageDraw.Draw(img)
    
    # Card
    w = dim * 0.65
    h = dim * 0.45
    x0 = (dim - w) / 2.0
    y0 = (dim - h) / 2.0
    x1 = x0 + w
    y1 = y0 + h
    draw.rounded_rectangle([x0, y0, x1, y1], radius=int(dim * 0.05), fill=(255, 255, 255, 255))
    # Card stripe
    s_h = h * 0.22
    s_y = y0 + h * 0.2
    draw.rectangle([x0, s_y, x1, s_y + s_h], fill=(14, 165, 233, 255))
    # Card chip
    c_w = w * 0.18
    c_h = h * 0.22
    c_x = x0 + w * 0.12
    c_y = y0 + h * 0.55
    draw.rounded_rectangle([c_x, c_y, c_x + c_w, c_y + c_h], radius=int(dim * 0.02), fill=(245, 158, 11, 255))
    
    if scale > 1:
        return img.resize((size, size), Image.Resampling.LANCZOS)
    return img

def draw_maha(size):
    scale = 2
    dim = size * scale
    c1 = (9, 13, 22, 255)     # #090d16
    c2 = (30, 58, 138, 255)   # #1e3a8a
    img = create_gradient_squircle(dim, c1, c2, (56, 189, 248, 70))
    draw = ImageDraw.Draw(img)
    
    # Battery terminal
    t_w = dim * 0.14
    t_h = dim * 0.08
    tx = (dim - t_w) / 2.0
    ty = dim * 0.15
    draw.rounded_rectangle([tx, ty, tx + t_w, ty + t_h], radius=int(dim * 0.02), fill=(203, 213, 225, 255))
    
    # Battery body
    b_w = dim * 0.44
    b_h = dim * 0.62
    bx = (dim - b_w) / 2.0
    by = ty + t_h
    draw.rounded_rectangle([bx, by, bx + b_w, by + b_h], radius=int(dim * 0.05), fill=(30, 41, 59, 255), outline=(255, 255, 255, 255), width=max(1, int(dim * 0.03)))
    
    # Charge bars (green)
    bar_w = b_w * 0.75
    bar_h = b_h * 0.18
    bar_x = (dim - bar_w) / 2.0
    for i in range(3):
        bar_y = by + b_h - (i + 1) * (bar_h * 1.35) - b_h * 0.08
        draw.rounded_rectangle([bar_x, bar_y, bar_x + bar_w, bar_y + bar_h], radius=int(dim * 0.02), fill=(74, 222, 128, 255))
        
    if scale > 1:
        return img.resize((size, size), Image.Resampling.LANCZOS)
    return img

def draw_gousto(size):
    scale = 2
    dim = size * scale
    c1 = (220, 38, 38, 255)   # #dc2626
    c2 = (249, 115, 22, 255)  # #f97316
    img = create_gradient_squircle(dim, c1, c2, (255, 255, 255, 45))
    draw = ImageDraw.Draw(img)
    
    cx, cy = dim / 2.0, dim / 2.0
    # Chef hat puffs
    r_center = dim * 0.18
    r_side = dim * 0.14
    # Center circle
    draw.ellipse([cx - r_center, cy - r_center * 1.3, cx + r_center, cy + r_center * 0.7], fill=(255, 255, 255, 255))
    # Left puff
    draw.ellipse([cx - r_center * 1.3, cy - r_side * 0.8, cx - r_center * 1.3 + 2 * r_side, cy + r_side * 1.2], fill=(255, 255, 255, 255))
    # Right puff
    draw.ellipse([cx + r_center * 1.3 - 2 * r_side, cy - r_side * 0.8, cx + r_center * 1.3, cy + r_side * 1.2], fill=(255, 255, 255, 255))
    # Base band
    band_w = dim * 0.44
    band_h = dim * 0.12
    bx = (dim - band_w) / 2.0
    by = cy + dim * 0.12
    draw.rounded_rectangle([bx, by, bx + band_w, by + band_h], radius=int(dim * 0.03), fill=(255, 255, 255, 255))
    
    if scale > 1:
        return img.resize((size, size), Image.Resampling.LANCZOS)
    return img

def draw_ev(size):
    scale = 2
    dim = size * scale
    c1 = (4, 120, 87, 255)    # #047857
    c2 = (16, 185, 129, 255)  # #10b981
    img = create_gradient_squircle(dim, c1, c2, (255, 255, 255, 45))
    draw = ImageDraw.Draw(img)
    
    # Prongs
    p_w = dim * 0.08
    p_h = dim * 0.16
    draw.rounded_rectangle([dim * 0.35, dim * 0.14, dim * 0.35 + p_w, dim * 0.14 + p_h], radius=int(dim * 0.02), fill=(226, 232, 240, 255))
    draw.rounded_rectangle([dim * 0.57, dim * 0.14, dim * 0.57 + p_w, dim * 0.14 + p_h], radius=int(dim * 0.02), fill=(226, 232, 240, 255))
    # Plug body
    b_w = dim * 0.45
    b_h = dim * 0.40
    bx = (dim - b_w) / 2.0
    by = dim * 0.28
    draw.rounded_rectangle([bx, by, bx + b_w, by + b_h], radius=int(dim * 0.06), fill=(255, 255, 255, 255))
    
    # Lightning bolt (yellow)
    cx, cy = dim / 2.0, by + b_h / 2.0
    bolt = [
        (cx + dim * 0.03, cy - dim * 0.14),
        (cx - dim * 0.08, cy),
        (cx, cy),
        (cx - dim * 0.03, cy + dim * 0.14),
        (cx + dim * 0.08, cy),
        (cx, cy)
    ]
    draw.polygon(bolt, fill=(234, 179, 8, 255))
    
    if scale > 1:
        return img.resize((size, size), Image.Resampling.LANCZOS)
    return img

def draw_movies(size):
    scale = 2
    dim = size * scale
    c1 = (30, 27, 75, 255)    # #1e1b4b
    c2 = (67, 56, 202, 255)   # #4338ca
    img = create_gradient_squircle(dim, c1, c2, (255, 255, 255, 45))
    draw = ImageDraw.Draw(img)
    
    # Clapperboard lower body
    w = dim * 0.62
    h = dim * 0.38
    x0 = (dim - w) / 2.0
    y0 = dim * 0.40
    x1 = x0 + w
    y1 = y0 + h
    draw.rounded_rectangle([x0, y0, x1, y1], radius=int(dim * 0.04), fill=(255, 255, 255, 245))
    
    # Play triangle inside
    cx, cy = dim / 2.0, y0 + h / 2.0
    tr = [
        (cx - dim * 0.06, cy - dim * 0.08),
        (cx + dim * 0.08, cy),
        (cx - dim * 0.06, cy + dim * 0.08)
    ]
    draw.polygon(tr, fill=(245, 158, 11, 255))
    
    # Clapperboard top bar
    tb_h = dim * 0.12
    tb_y = y0 - tb_h - dim * 0.02
    draw.rounded_rectangle([x0, tb_y, x1, tb_y + tb_h], radius=int(dim * 0.02), fill=(15, 23, 42, 255))
    # Stripes
    for i in range(4):
        sx = x0 + w * 0.12 + i * (w * 0.22)
        draw.polygon([(sx, tb_y), (sx + w * 0.06, tb_y), (sx, tb_y + tb_h), (sx - w * 0.06, tb_y + tb_h)], fill=(245, 158, 11, 255))
        
    if scale > 1:
        return img.resize((size, size), Image.Resampling.LANCZOS)
    return img

def generate_ico(app_name, draw_fn, output_dir):
    sizes = [16, 32, 48, 64]
    imgs = [draw_fn(s) for s in sizes]
    ico_path = os.path.join(output_dir, "favicon.ico")
    imgs[0].save(
        ico_path,
        format="ICO",
        sizes=[(s, s) for s in sizes],
        append_images=imgs[1:]
    )
    print(f"Generated {ico_path}")

def main():
    base_dir = r"C:\Projects\Personal Projects"
    apps = {
        "swarovski-collection": (draw_swarovski, os.path.join(base_dir, "Swarovski-Collection", "public")),
        "barclays-transactions": (draw_barclays, os.path.join(base_dir, "barclays-transactions", "public")),
        "maha-c9000-battery-charger": (draw_maha, os.path.join(base_dir, "Maha-C9000-Battery-Charger-Help", "public")),
        "gousto-recipe-search": (draw_gousto, os.path.join(base_dir, "Gousto-Recipe-Search")),
        "ev-charging-cost-calculator": (draw_ev, os.path.join(base_dir, "EV-Charging-Cost-Calculator", "public")),
        "movie-and-tv-database": (draw_movies, os.path.join(base_dir, "movie-and-tv-database", "public")),
    }
    
    for app_name, (draw_fn, out_dir) in apps.items():
        os.makedirs(out_dir, exist_ok=True)
        generate_ico(app_name, draw_fn, out_dir)

if __name__ == "__main__":
    main()
