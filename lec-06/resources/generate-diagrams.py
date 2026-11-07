"""Lecture 6 diagrams using official AWS / Azure / GCP architecture icons."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import math

ICON_DIR = Path(__file__).resolve().parent / "icons"
OUT_DIR = Path(__file__).resolve().parent

BG = (248, 250, 252)
INK = (15, 23, 42)
MUTED = (71, 85, 105)
TEAL = (15, 118, 110)
WHITE = (255, 255, 255)
AWS = (15, 23, 42)
AZURE = (0, 90, 158)
GCP = (26, 115, 232)
ORANGE = (180, 83, 9)


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
    draw.text((cx - (box[2] - box[0]) / 2, y), text, font=f, fill=fill)


def arrow(draw, x1, y1, x2, y2, color=INK, width=5):
    draw.line((x1, y1, x2, y2), fill=color, width=width)
    ang = math.atan2(y2 - y1, x2 - x1)
    L = 18
    for d in (2.4, -2.4):
        ax = x2 - L * math.cos(ang + d * 0.28)
        ay = y2 - L * math.sin(ang + d * 0.28)
        draw.line((x2, y2, ax, ay), fill=color, width=width)


def header(draw, w, title, sub):
    draw.rectangle((0, 0, w, 110), fill=TEAL)
    draw.text((48, 22), title, font=font(38, True), fill=WHITE)
    draw.text((48, 70), sub, font=font(20), fill=(204, 251, 241))


def save(img, name):
    rgb = Image.new("RGB", img.size, BG)
    rgb.paste(img, mask=img.split()[-1])
    out = OUT_DIR / name
    rgb.save(out, "PNG", optimize=True)
    print("Wrote", out, out.stat().st_size)


def step_card(base, draw, cx, top, icon, title, sub, fill=WHITE, line=TEAL, isize=88):
    w, h = 360, 280
    x0, y0 = cx - w / 2, top
    round_rect(draw, (x0, y0, x0 + w, y0 + h), 22, fill, line, 3)
    ic = load_icon(icon, isize)
    paste(base, ic, cx - isize / 2, y0 + 28)
    center_text(draw, title, cx, y0 + 130, font(22, True), INK)
    for i, line_t in enumerate(sub.split("\n")):
        center_text(draw, line_t, cx, y0 + 168 + i * 28, font(18), MUTED)
    return (x0 + w, y0 + h / 2)


def path_diagram():
    W, H = 2800, 980
    img = Image.new("RGBA", (W, H), BG + (255,))
    d = ImageDraw.Draw(img)
    header(d, W, "Lecture 6  ·  Today’s path", "Same image notes-api:l6  ·  Hub is a second shelf  ·  Fargate pulls ECR")

    y = 200
    xs = [280, 840, 1400, 1960, 2520]
    labels = [
        ("docker.png", "1. Build on EC2", "docker build -t\nnotes-api:l6 ."),
        ("docker.png", "2. Docker Hub", "YOURHUB/\nnotes-api:l6"),
        ("ecr.png", "3. Amazon ECR", "this account,\nthis Region"),
        ("fargate.png", "4. Fargate", "no SSH\npulls ECR :l6"),
        ("user.png", "5. Your laptop", "curl /health\non public IP"),
    ]
    mids = []
    for cx, (icon, title, sub) in zip(xs, labels):
        _, midy = None, y + 140
        step_card(img, d, cx, y, icon, title, sub)
        mids.append((cx, midy))

    for i in range(len(mids) - 1):
        x1 = mids[i][0] + 180
        x2 = mids[i + 1][0] - 180
        arrow(d, x1, mids[i][1], x2, mids[i + 1][1], TEAL, 6)

    d.text((120, 530), "push", font=font(18, True), fill=TEAL)
    d.text((1080, 530), "push", font=font(18, True), fill=TEAL)
    d.text((1640, 530), "pull", font=font(18, True), fill=TEAL)
    d.text((2200, 530), "HTTP :8080", font=font(18, True), fill=TEAL)

    round_rect(d, (80, 620, 2720, 900), 20, WHITE, (226, 232, 240), 3)
    d.text((120, 650), "Remember", font=font(24, True), fill=INK)
    d.text((120, 700), "Fargate does not pull Docker Hub today. The task image is the ECR URI with tag :l6.", font=font(22), fill=MUTED)
    d.text((120, 746), "Azure same job: ACR  +  Container Apps.    GCP same job: Artifact Registry  +  Cloud Run.", font=font(22), fill=MUTED)
    d.text((120, 792), "Lecture 11 project still runs Docker on one EC2. Delete Fargate before you leave.", font=font(22), fill=ORANGE)
    save(img, "path.png")


def clouds_diagram():
    W, H = 2800, 1100
    img = Image.new("RGBA", (W, H), BG + (255,))
    d = ImageDraw.Draw(img)
    header(d, W, "Same two jobs  ·  three cloud names", "We click AWS today. Azure and GCP names are for interviews — no Azure/GCP lab.")

    cols = [
        (120, AWS, "AWS (today)", "ecr.png", "Amazon ECR", "Private shelf in your account", "fargate.png", "ECS / Fargate", "Run the image. No SSH."),
        (980, AZURE, "Azure (names)", "acr.png", "ACR", "Azure Container Registry", "container-apps.png", "Container Apps", "ACI is the older one-container name."),
        (1840, GCP, "GCP (names)", "artifact-registry.png", "Artifact Registry", "Replaced Container Registry (GCR)", "cloudrun.png", "Cloud Run", "HTTPS URL in front of a container."),
    ]
    for x, color, title, r_icon, r_name, r_sub, run_icon, run_name, run_sub in cols:
        round_rect(d, (x, 160, x + 840, 1020), 24, WHITE, color, 4)
        d.rectangle((x, 160, x + 840, 240), fill=color)
        center_text(d, title, x + 420, 180, font(28, True), WHITE)

        d.text((x + 48, 280), "1. Shelf (registry)", font=font(20, True), fill=MUTED)
        ic = load_icon(r_icon, 96)
        paste(img, ic, x + 48, 330)
        d.text((x + 170, 348), r_name, font=font(26, True), fill=INK)
        d.text((x + 170, 392), r_sub, font=font(20), fill=MUTED)

        d.line((x + 48, 470, x + 792, 470), fill=(226, 232, 240), width=3)

        d.text((x + 48, 500), "2. Run without picking a VM", font=font(20, True), fill=MUTED)
        ic2 = load_icon(run_icon, 96)
        paste(img, ic2, x + 48, 550)
        d.text((x + 170, 568), run_name, font=font(26, True), fill=INK)
        d.text((x + 170, 612), run_sub, font=font(20), fill=MUTED)

        d.line((x + 48, 700, x + 792, 700), fill=(226, 232, 240), width=3)
        d.text((x + 48, 740), "Kubernetes (later, not today)", font=font(20, True), fill=MUTED)
        k8s = {"AWS (today)": "EKS  —  we use kind, not EKS", "Azure (names)": "AKS  —  named only", "GCP (names)": "GKE  —  named only"}
        d.text((x + 48, 786), k8s[title], font=font(22, True), fill=color)
        d.text((x + 48, 840), "This course: kind on a laptop (lectures 7–8).", font=font(20), fill=MUTED)

    save(img, "three-clouds.png")


def contrast_diagram():
    W, H = 2800, 980
    img = Image.new("RGBA", (W, H), BG + (255,))
    d = ImageDraw.Draw(img)
    header(d, W, "Two ways to run the same image", "Left = lectures 5 and 6 build box. Right = today’s Fargate demo.")

    round_rect(d, (80, 160, 1360, 900), 24, (15, 23, 42), None, 0)
    ic = load_icon("ec2.png", 110)
    paste(img, ic, 140, 200)
    d.text((280, 220), "Docker on an EC2", font=font(32, True), fill=WHITE)
    d.text((280, 270), "You operate a computer", font=font(22), fill=(148, 163, 184))
    lines = [
        "Launch a t3.micro. SSH in.",
        "sudo docker build  and  docker run",
        "curl http://127.0.0.1:8080/health  on the box",
        "Security group: 22 from My IP. 8080 stays closed.",
        "You see docker logs in the SSH window.",
        "Lecture 11 project uses this pattern.",
    ]
    for i, t in enumerate(lines):
        d.text((140, 360 + i * 70), "•  " + t, font=font(24), fill=(226, 232, 240))

    round_rect(d, (1440, 160, 2720, 900), 24, (236, 253, 245), TEAL, 4)
    ic = load_icon("fargate.png", 110)
    paste(img, ic, 1500, 200)
    d.text((1640, 220), "Fargate (ECS)", font=font(32, True), fill=INK)
    d.text((1640, 270), "You operate a recipe", font=font(22), fill=MUTED)
    lines = [
        "No extra EC2 for the app. No SSH.",
        "Task definition names the ECR URI :l6.",
        "curl the task public IP from Windows.",
        "Security group: 8080 for this hour only.",
        "Logs live in CloudWatch.",
        "Delete the service before you stand up.",
    ]
    for i, t in enumerate(lines):
        d.text((1500, 360 + i * 70), "•  " + t, font=font(24), fill=INK)

    save(img, "ec2-vs-fargate.png")


def hub_ecr_diagram():
    W, H = 2800, 900
    img = Image.new("RGBA", (W, H), BG + (255,))
    d = ImageDraw.Draw(img)
    header(d, W, "Two shelves  ·  one local image", "tag once for Hub, tag once for ECR. Same notes-api:l6 bits.")

    # local
    round_rect(d, (80, 180, 720, 820), 24, (15, 23, 42), None, 0)
    ic = load_icon("docker.png", 100)
    paste(img, ic, 350, 230)
    center_text(d, "On this EC2", 400, 360, font(26, True), WHITE)
    center_text(d, "notes-api:l6", 400, 420, font(28, True), (94, 234, 212))
    center_text(d, "docker images", 400, 480, font(20), (148, 163, 184))
    center_text(d, "docker build created it", 400, 530, font(20), (148, 163, 184))

    arrow(d, 740, 400, 920, 320, TEAL, 6)
    arrow(d, 740, 520, 920, 600, TEAL, 6)
    d.text((760, 250), "docker tag", font=font(18, True), fill=TEAL)
    d.text((760, 270), "+ push", font=font(18, True), fill=TEAL)
    d.text((760, 640), "docker tag", font=font(18, True), fill=TEAL)
    d.text((760, 660), "+ push", font=font(18, True), fill=TEAL)

    round_rect(d, (940, 180, 1780, 500), 24, WHITE, (14, 165, 233), 4)
    ic = load_icon("docker.png", 90)
    paste(img, ic, 980, 220)
    d.text((1100, 230), "Docker Hub", font=font(28, True), fill=INK)
    d.text((1100, 278), "hub.docker.com", font=font(20), fill=MUTED)
    d.text((980, 360), "YOURHUB/notes-api:l6", font=font(24, True), fill=(3, 105, 161))
    d.text((980, 410), "Token login. Optional later. Fargate ignores this.", font=font(20), fill=MUTED)

    round_rect(d, (940, 540, 1780, 820), 24, WHITE, TEAL, 4)
    ic = load_icon("ecr.png", 90)
    paste(img, ic, 980, 570)
    d.text((1100, 580), "Amazon ECR", font=font(28, True), fill=INK)
    d.text((1100, 628), "this AWS account + Region", font=font(20), fill=MUTED)
    d.text((980, 700), "ACCOUNT.dkr.ecr.REGION…/notes-api:l6", font=font(22, True), fill=TEAL)
    d.text((980, 748), "IAM login. Fargate pulls from here.", font=font(20), fill=MUTED)

    round_rect(d, (1880, 180, 2720, 820), 24, (236, 253, 245), TEAL, 4)
    ic = load_icon("fargate.png", 100)
    paste(img, ic, 2200, 240)
    center_text(d, "Fargate task", 2300, 370, font(28, True), INK)
    center_text(d, "Image URI = ECR :l6", 2300, 440, font(24, True), TEAL)
    center_text(d, "Not the Hub URL", 2300, 500, font(22), MUTED)
    ic2 = load_icon("cloudwatch.png", 72)
    paste(img, ic2, 2264, 580)
    center_text(d, "Logs → CloudWatch", 2300, 670, font(20), MUTED)
    center_text(d, "No SSH", 2300, 720, font(20, True), ORANGE)

    save(img, "hub-ecr.png")


if __name__ == "__main__":
    path_diagram()
    clouds_diagram()
    contrast_diagram()
    hub_ecr_diagram()
