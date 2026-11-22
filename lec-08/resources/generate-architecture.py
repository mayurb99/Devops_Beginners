"""Lecture 8 demo architecture — two Pods, one Service, ConfigMap + Secret."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import math

ICON_DIR = Path(__file__).resolve().parent / "icons"
OUT = Path(__file__).resolve().parent / "lecture-8-architecture.png"

W, H = 3000, 1760
BG = (248, 250, 252)
INK = (15, 23, 42)
MUTED = (71, 85, 105)
TEAL = (15, 118, 110)
WHITE = (255, 255, 255)
VPC_FILL = (245, 243, 255)
VPC_LINE = (124, 58, 237)
PUB_FILL = (236, 253, 245)
PUB_LINE = (5, 150, 105)
EKS_FILL = (239, 246, 255)
EKS_LINE = (37, 99, 235)
ECR_FILL = (255, 247, 237)
ECR_LINE = (234, 88, 12)
RED = (185, 28, 28)


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
    canvas.paste(im, ((size - im.width) // 2, (size - im.height) // 2), im)
    return canvas


def paste(base, icon, x, y):
    base.alpha_composite(icon, (int(x), int(y)))


def center_text(draw, text, cx, y, f, fill=INK):
    box = draw.textbbox((0, 0), text, font=f)
    draw.text((cx - (box[2] - box[0]) / 2, y), text, font=f, fill=fill)


def card(base, draw, icon_name, cx, top, label, sub, size=80):
    icon = load_icon(icon_name, size)
    paste(base, icon, cx - size / 2, top)
    center_text(draw, label, cx, top + size + 6, font(20, True))
    if sub:
        for i, line in enumerate(sub.split("\n")):
            center_text(draw, line, cx, top + size + 32 + i * 24, font(16), MUTED)
    return (cx, top + size / 2)


def arrow(draw, x1, y1, x2, y2, color=INK, width=4):
    draw.line((x1, y1, x2, y2), fill=color, width=width)
    ang = math.atan2(y2 - y1, x2 - x1)
    L = 16
    for d in (2.5, -2.5):
        ax = x2 - L * math.cos(ang + d * 0.28)
        ay = y2 - L * math.sin(ang + d * 0.28)
        draw.line((x2, y2, ax, ay), fill=color, width=width)


def pill(draw, text, x, y, fill=(254, 226, 226), fg=RED):
    f = font(15, True)
    box = draw.textbbox((0, 0), text, font=f)
    tw, th = box[2] - box[0], box[3] - box[1]
    round_rect(draw, (x, y, x + tw + 24, y + th + 12), 10, fill)
    draw.text((x + 12, y + 4), text, font=f, fill=fg)


def main():
    img = Image.new("RGBA", (W, H), BG + (255,))
    d = ImageDraw.Draw(img)

    d.rectangle((0, 0, W, 118), fill=TEAL)
    d.text((48, 26), "Lecture 8  ·  Architecture of the class demo", font=font(40, True), fill=WHITE)
    d.text((48, 76), "Same VPC and EKS as lecture 7  ·  notes-api:l8  ·  replicas 2  ·  ConfigMap + Secret  ·  one LoadBalancer URL", font=font(20), fill=(204, 251, 241))

    card(img, d, "user.png", 240, 150, "You (browser)", "http://EXTERNAL-IP/\nAdd  ·  Show  ·  watch Pod name")
    card(img, d, "user.png", 620, 150, "CloudShell", "apply / describe / logs\nrollout undo")

    round_rect(d, (900, 140, 1960, 420), 20, EKS_FILL, EKS_LINE, 4)
    paste(img, load_icon("eks.png", 60), 925, 155)
    d.text((1000, 168), "EKS control plane  ·  lec07-eks  (reuse or recreate)", font=font(20, True), fill=EKS_LINE)
    card(img, d, "api.png", 1120, 230, "API server", "kubectl door")
    card(img, d, "rs.png", 1440, 230, "ReplicaSet", "keep 2 Pods")
    card(img, d, "sched.png", 1760, 230, "Scheduler", "place A and B")
    pill(d, "DELETE THE CLUSTER", 1688, 155)

    round_rect(d, (2020, 140, 2940, 420), 20, ECR_FILL, ECR_LINE, 4)
    paste(img, load_icon("ecr.png", 60), 2045, 160)
    d.text((2125, 175), "ECR  ·  notes-api:l8", font=font(20, True), fill=ECR_LINE)
    card(img, d, "ecr.png", 2480, 230, "image has Python", "title comes from ConfigMap")

    arrow(d, 700, 220, 890, 220, EKS_LINE, 4)
    d.text((740, 188), "kubectl", font=font(16, True), fill=EKS_LINE)

    vpc = (70, 460, 2930, 1540)
    round_rect(d, vpc, 28, VPC_FILL, VPC_LINE, 5)
    paste(img, load_icon("vpc.png", 56), 95, 480)
    d.text((165, 490), "VPC  notes-k8s   10.7.0.0/16   two public AZs   no NAT   same as lecture 7", font=font(24, True), fill=VPC_LINE)

    round_rect(d, (110, 560, 1000, 980), 18, WHITE, TEAL, 3)
    card(img, d, "elb.png", 280, 590, "Load balancer", "created by Service notes")
    card(img, d, "svc.png", 720, 590, "Service  notes", "one hostname  ·  port 80")
    d.text((150, 860), "Each click can land on Pod A or Pod B.", font=font(17), fill=INK)
    d.text((150, 892), "That is why a note can vanish on Show.", font=font(17), fill=MUTED)
    pill(d, "DELETE WITH THE SERVICE", 150, 930)

    round_rect(d, (1040, 560, 1960, 980), 18, PUB_FILL, PUB_LINE, 4)
    d.text((1070, 580), "Worker nodes  ·  two t3.small", font=font(20, True), fill=PUB_LINE)
    card(img, d, "pod.png", 1260, 640, "Pod A", "its own Python list")
    card(img, d, "pod.png", 1680, 640, "Pod B", "a different list")
    d.text((1070, 900), "replicas: 2. Footer Pod name tells you which one answered.", font=font(17), fill=INK)

    round_rect(d, (2000, 560, 2890, 980), 18, WHITE, (148, 163, 184), 3)
    d.text((2030, 580), "Not inside the image", font=font(20, True), fill=INK)
    d.text((2030, 640), "ConfigMap  notes-config", font=font(18, True), fill=TEAL)
    d.text((2030, 672), "PAGE_TITLE  ·  PAGE_SUB", font=font(16), fill=MUTED)
    d.text((2030, 720), "Secret  notes-secret", font=font(18, True), fill=ECR_LINE)
    d.text((2030, 752), "NOTES_TOKEN  (dummy, not an AWS key)", font=font(16), fill=MUTED)
    d.text((2030, 820), "envFrom attaches both as env vars.", font=font(16), fill=INK)
    d.text((2030, 852), "rollout restart after you edit the ConfigMap.", font=font(16), fill=MUTED)
    d.text((2030, 900), "Page prints both: ConfigMap title and dummy Secret.", font=font(16), fill=MUTED)

    round_rect(d, (110, 1020, 1480, 1480), 18, WHITE, (148, 163, 184), 3)
    d.text((140, 1040), "What you prove in the browser", font=font(22, True), fill=INK)
    d.text((140, 1100), "1. Refresh / Show  →  Pod name flips  (A then B).", font=font(18), fill=INK)
    d.text((140, 1144), "2. Add a unique line. Show again. Sometimes it is gone.", font=font(18), fill=INK)
    d.text((140, 1188), "3. Edit ConfigMap title  →  rollout restart  →  heading changes.", font=font(18), fill=INK)
    d.text((140, 1232), "4. Wrong tag → ImagePullBackOff.  CRASH=1 → CrashLoopBackOff.", font=font(18), fill=INK)
    d.text((140, 1276), "5. memory request 8Gi → Pending.  rollout undo → healthy again.", font=font(18), fill=INK)
    d.text((140, 1350), "kubectl describe  and  kubectl logs  — do not guess.", font=font(18, True), fill=TEAL)

    round_rect(d, (1540, 1020, 2890, 1480), 18, WHITE, ECR_LINE, 3)
    d.text((1570, 1040), "Build box  (not a node)  ·  lec08-build", font=font(22, True), fill=INK)
    card(img, d, "ec2.png", 1780, 1110, "t3.micro", "SSH 22 My IP")
    card(img, d, "docker.png", 2260, 1110, "docker build / push", "tag notes-api:l8")
    d.text((1570, 1360), "Windows has no Docker Desktop. This box only builds.", font=font(16), fill=MUTED)
    d.text((1570, 1394), "Lecture 7 image cannot read PAGE_TITLE. You need :l8.", font=font(16), fill=MUTED)

    arrow(d, 240, 330, 240, 555, TEAL, 4)
    arrow(d, 720, 980, 1260, 980, TEAL, 3)
    arrow(d, 720, 980, 1680, 980, TEAL, 3)

    d.text((48, 1570), "Notes still live in process RAM. No database today. Lecture 11 project is still one EC2, not this cluster.", font=font(18), fill=INK)
    d.text((48, 1610), "Cleanup: kubectl delete svc notes  →  node group  →  cluster lec07-eks  →  terminate lec08-build  →  VPC", font=font(18, True), fill=RED)
    d.text((48, 1658), "Lecture 8 demo  ·  Not created: NAT, ALB wizard, Helm required, RBAC lab, AKS/GKE  ·  Icons: AWS + Kubernetes", font=font(16), fill=MUTED)

    rgb = Image.new("RGB", img.size, BG)
    rgb.paste(img, mask=img.split()[-1])
    rgb.save(OUT, "PNG", optimize=True)
    print("Wrote", OUT, OUT.stat().st_size)


if __name__ == "__main__":
    main()
