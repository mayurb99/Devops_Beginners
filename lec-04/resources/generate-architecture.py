"""Lecture 4 architecture PNG using official AWS icons (mingrammer/diagrams pack)."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter

ICON_DIR = Path(__file__).resolve().parent / "aws-icons"
OUT = Path(__file__).resolve().parent / "lecture-4-architecture.png"

W, H = 2800, 1760
BG = (248, 250, 252)
INK = (15, 23, 42)
MUTED = (71, 85, 105)
TEAL = (15, 118, 110)
ORANGE = (255, 153, 0)
WHITE = (255, 255, 255)
VPC_FILL = (245, 243, 255)
VPC_LINE = (124, 58, 237)
PUB_FILL = (236, 253, 245)
PUB_LINE = (5, 150, 105)
PRIV_FILL = (239, 246, 255)
PRIV_LINE = (37, 99, 235)
S3_FILL = (255, 247, 237)
S3_LINE = (234, 88, 12)


def font(size, bold=False):
    name = "segoeuib.ttf" if bold else "segoeui.ttf"
    for p in (
        rf"C:\Windows\Fonts\{name}",
        r"C:\Windows\Fonts\arialbd.ttf" if bold else r"C:\Windows\Fonts\arial.ttf",
        r"C:\Windows\Fonts\calibrib.ttf" if bold else r"C:\Windows\Fonts\calibri.ttf",
    ):
        try:
            return ImageFont.truetype(p, size)
        except OSError:
            continue
    return ImageFont.load_default()


def round_rect(draw, xy, r, fill, outline=None, width=3):
    draw.rounded_rectangle(xy, radius=r, fill=fill, outline=outline, width=width)


def load_icon(name, size):
    im = Image.open(ICON_DIR / name).convert("RGBA")
    im.thumbnail((size, size), Image.Resampling.LANCZOS)
    canvas = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    x = (size - im.width) // 2
    y = (size - im.height) // 2
    canvas.paste(im, (x, y), im)
    return canvas


def paste(base, icon, x, y):
    base.alpha_composite(icon, (int(x), int(y)))


def center_text(draw, text, cx, y, f, fill=INK):
    box = draw.textbbox((0, 0), text, font=f)
    tw = box[2] - box[0]
    draw.text((cx - tw / 2, y), text, font=f, fill=fill)


def card(base, draw, icon_name, cx, top, label, sub, size=96):
    icon = load_icon(icon_name, size)
    paste(base, icon, cx - size / 2, top)
    f1, f2 = font(22, True), font(18)
    center_text(draw, label, cx, top + size + 6, f1)
    if sub:
        center_text(draw, sub, cx, top + size + 32, f2, MUTED)
    return (cx, top + size / 2)


def arrow(draw, x1, y1, x2, y2, color=INK, width=4):
    draw.line((x1, y1, x2, y2), fill=color, width=width)
    import math
    ang = math.atan2(y2 - y1, x2 - x1)
    L = 16
    for d in (2.5, -2.5):
        ax = x2 - L * math.cos(ang + d * 0.28)
        ay = y2 - L * math.sin(ang + d * 0.28)
        draw.line((x2, y2, ax, ay), fill=color, width=width)


def pill(draw, text, x, y, fill=ORANGE, fg=INK):
    f = font(16, True)
    box = draw.textbbox((0, 0), text, font=f)
    tw, th = box[2] - box[0], box[3] - box[1]
    pad_x, pad_y = 12, 6
    round_rect(draw, (x, y, x + tw + pad_x * 2, y + th + pad_y * 2), 10, fill)
    draw.text((x + pad_x, y + pad_y - 2), text, font=f, fill=fg)


def main():
    img = Image.new("RGBA", (W, H), BG + (255,))
    d = ImageDraw.Draw(img)

    d.rectangle((0, 0, W, 118), fill=TEAL)
    d.text((48, 28), "Lecture 4  ·  Architecture of the class demo", font=font(42, True), fill=WHITE)
    d.text((48, 78), "VPC notes-net  ·  10.0.0.0/16  ·  AWS console  ·  official AWS architecture icons", font=font(22), fill=(204, 251, 241))

    # Internet
    internet_cx, internet_top = 1400, 150
    card(img, d, "internet.png", internet_cx, internet_top, "Internet", "your browser / home IP")
    card(img, d, "users.png", 1180, 158, "You", "HTTPS later; HTTP :80 today")

    igw_cx, igw_top = 1400, 330
    arrow(d, internet_cx, 278, igw_cx, igw_top - 4, TEAL, 5)
    card(img, d, "igw.png", igw_cx, igw_top, "Internet Gateway", "notes-igw  ·  public door")

    # VPC
    vpc = (70, 520, 2730, 1320)
    round_rect(d, vpc, 28, VPC_FILL, VPC_LINE, 5)
    paste(img, load_icon("vpc.png", 72), 90, 538)
    d.text((175, 548), "VPC   notes-net    10.0.0.0/16", font=font(28, True), fill=VPC_LINE)
    d.text((175, 586), "NACL notes-nacl on the subnets (allow all for class)   ·   DNS hostnames ON", font=font(18), fill=MUTED)

    # Public cluster
    pub = (100, 640, 1780, 1270)
    round_rect(d, pub, 22, PUB_FILL, PUB_LINE, 4)
    paste(img, load_icon("public-subnet.png", 56), 120, 656)
    d.text((185, 662), "Public subnets  (2 AZs)   ·   Auto-assign public IPv4 ON   ·   0.0.0.0/0  →  IGW", font=font(22, True), fill=PUB_LINE)
    d.text((185, 694), "public-a and public-b  ·  ALB needs two AZs", font=font(18), fill=MUTED)

    # ALB
    alb_cx = 940
    card(img, d, "alb.png", alb_cx, 730, "Application Load Balancer", "hello-alb  ·  HTTP :80  ·  billed")
    pill(d, "DELETE SAME DAY", 1088, 748, (254, 226, 226), (185, 28, 28))

    # two EC2s
    a_cx, b_cx = 520, 1360
    card(img, d, "ec2.png", a_cx, 980, "hello-a", "public EC2  ·  Hello APP-A  ·  :80")
    card(img, d, "ec2.png", b_cx, 980, "hello-b", "public EC2  ·  Hello APP-B  ·  :80")
    pill(d, "Elastic IP on hello-a  ·  stays after stop/start", a_cx - 120, 1168, (254, 243, 199), INK)

    arrow(d, alb_cx - 40, 900, a_cx, 970, PUB_LINE, 4)
    arrow(d, alb_cx + 40, 900, b_cx, 970, PUB_LINE, 4)
    d.text((680, 918), "target group hello-tg  ·  refresh the ALB URL to see A then B", font=font(18), fill=MUTED)

    # NAT in public
    nat_cx = 1640
    card(img, d, "nat.png", nat_cx, 740, "NAT Gateway", "notes-nat  ·  sits in PUBLIC  ·  billed")

    # Private
    priv = (1840, 640, 2700, 1270)
    round_rect(d, priv, 22, PRIV_FILL, PRIV_LINE, 4)
    paste(img, load_icon("private-subnet.png", 56), 1860, 656)
    d.text((1925, 662), "Private subnet", font=font(22, True), fill=PRIV_LINE)
    d.text((1925, 694), "no public IP  ·  no 0.0.0.0/0 until K", font=font(18), fill=MUTED)

    card(img, d, "ec2.png", 2270, 800, "private-nat-test", "private EC2  ·  sg-private")
    card(img, d, "endpoint.png" if (ICON_DIR / "endpoint.png").exists() else "igw.png", 2270, 1040, "Instance Connect Endpoint", "console SSH into private")

    # NAT flow
    arrow(d, 2140, 920, 1720, 820, PRIV_LINE, 4)
    d.text((1980, 860), "after K:", font=font(18, True), fill=PRIV_LINE)
    d.text((1980, 886), "0.0.0.0/0 → NAT → IGW", font=font(18), fill=PRIV_LINE)
    d.text((1980, 912), "out only, not in", font=font(16), fill=MUTED)

    # IGW to VPC
    arrow(d, igw_cx, 470, igw_cx, 520, TEAL, 5)

    # S3 + Lambda strip
    s3box = (100, 1360, 1780, 1688)
    round_rect(d, s3box, 22, S3_FILL, S3_LINE, 4)
    d.text((130, 1380), "Storage + event  (outside the VPC picture, same Region)", font=font(22, True), fill=S3_LINE)

    card(img, d, "s3.png", 380, 1440, "S3 bucket", "notes-lab-…  ·  Block public access ON")
    card(img, d, "lambda.png", 980, 1440, "Lambda  notes-s3-logger", "Python  ·  trigger: object created")
    arrow(d, 500, 1520, 860, 1520, S3_LINE, 5)
    d.text((620, 1478), "upload hello.txt", font=font(18, True), fill=S3_LINE)
    d.text((1180, 1578), "CloudWatch logs show the object key", font=font(18), fill=MUTED)

    # SG legend
    sgbox = (1840, 1360, 2700, 1688)
    round_rect(d, sgbox, 22, WHITE, (148, 163, 184), 3)
    d.text((1870, 1380), "Security groups (instance firewall)", font=font(22, True), fill=INK)
    d.text((1870, 1424), "sg-hello", font=font(20, True), fill=TEAL)
    d.text((1870, 1454), "Inbound HTTP :80 from 0.0.0.0/0", font=font(18), fill=MUTED)
    d.text((1870, 1482), "then SSH :22 from My IP  (not 0.0.0.0/0)", font=font(18), fill=MUTED)
    d.text((1870, 1524), "sg-private", font=font(20, True), fill=PRIV_LINE)
    d.text((1870, 1554), "SSH :22 from 10.0.0.0/16 only", font=font(18), fill=MUTED)
    d.text((1870, 1594), "ALB uses sg-hello.  NAT + ALB = delete same day.", font=font(18, True), fill=(185, 28, 28))

    # footer
    d.text((48, 1710), "Lecture 4 demo  ·  Not created: RDS, EFS, EKS, Fargate  ·  Icons: AWS architecture icon set", font=font(16), fill=MUTED)

    rgb = Image.new("RGB", img.size, BG)
    rgb.paste(img, mask=img.split()[-1])
    rgb.save(OUT, "PNG", optimize=True)
    print("Wrote", OUT, OUT.stat().st_size)


if __name__ == "__main__":
    main()
