"""Lecture 7 demo architecture — official AWS / Kubernetes icons."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import math

ICON_DIR = Path(__file__).resolve().parent / "icons"
OUT = Path(__file__).resolve().parent / "lecture-7-architecture.png"

W, H = 3000, 1860
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


def card(base, draw, icon_name, cx, top, label, sub, size=88):
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


def polyline(draw, pts, color=INK, width=4):
    for i in range(len(pts) - 2):
        draw.line((*pts[i], *pts[i + 1]), fill=color, width=width)
    arrow(draw, *pts[-2], *pts[-1], color, width)


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
    d.text((48, 26), "Lecture 7  ·  Architecture of the class demo", font=font(40, True), fill=WHITE)
    d.text(
        (48, 76),
        "VPC notes-k8s  ·  10.7.0.0/16  ·  EKS lec07-eks  ·  notes-api:l7 from ECR  ·  Service type LoadBalancer",
        font=font(20),
        fill=(204, 251, 241),
    )

    # Top: two doors into the demo
    card(img, d, "user.png", 260, 145, "You (browser)", "http://EXTERNAL-IP/\nAdd note  ·  Show notes")
    card(img, d, "user.png", 620, 145, "CloudShell", "kubectl apply / get / logs")

    # EKS control plane (AWS computers — outside the VPC)
    round_rect(d, (880, 140, 1960, 430), 20, EKS_FILL, EKS_LINE, 4)
    paste(img, load_icon("eks.png", 64), 905, 155)
    d.text((980, 165), "EKS control plane  ·  lec07-eks", font=font(22, True), fill=EKS_LINE)
    d.text((980, 198), "AWS computers  ·  billed even with zero Pods  ·  public endpoint", font=font(16), fill=MUTED)
    card(img, d, "api.png", 1080, 235, "API server", "the only kubectl door")
    card(img, d, "etcd.png", 1380, 235, "etcd", "desired: replicas 1")
    card(img, d, "sched.png", 1700, 235, "Scheduler", "picks a node")
    pill(d, "DELETE THE CLUSTER", 1680, 155)

    # ECR (same Region, outside the VPC)
    round_rect(d, (2020, 140, 2940, 430), 20, ECR_FILL, ECR_LINE, 4)
    paste(img, load_icon("ecr.png", 64), 2045, 155)
    d.text((2125, 168), "ECR  ·  this Region  ·  not inside the VPC", font=font(20, True), fill=ECR_LINE)
    card(img, d, "ecr.png", 2480, 225, "notes-api:l7", "private repo  ·  HTML at GET /")

    arrow(d, 700, 220, 870, 220, EKS_LINE, 4)
    d.text((730, 188), "kubectl", font=font(16, True), fill=EKS_LINE)

    # IGW sits on the VPC door
    card(img, d, "igw.png", 260, 385, "Internet Gateway", "public door of the VPC")
    arrow(d, 260, 328, 260, 380, TEAL, 5)
    d.text((280, 340), "HTTP :80  (not :8080, not https)", font=font(16), fill=MUTED)

    # Image path in the corridor (no lines across titles)
    round_rect(d, (880, 450, 2940, 518), 12, (255, 247, 237), ECR_LINE, 2)
    d.text((910, 468), "Image path   ·   lec07-build  docker push :l7   →   ECR notes-api:l7   →   worker kubelet pulls :l7", font=font(18, True), fill=ECR_LINE)

    # VPC
    vpc = (70, 540, 2930, 1650)
    round_rect(d, vpc, 28, VPC_FILL, VPC_LINE, 5)
    paste(img, load_icon("vpc.png", 64), 95, 558)
    d.text((175, 565), "VPC   notes-k8s    10.7.0.0/16     DNS hostnames ON     no NAT today", font=font(26, True), fill=VPC_LINE)
    d.text(
        (175, 608),
        "On BOTH public subnets:  kubernetes.io/role/elb = 1     kubernetes.io/cluster/lec07-eks = shared     auto-assign public IPv4 ON",
        font=font(17),
        fill=MUTED,
    )

    # Load balancer inside the VPC (created by the Service, not the ALB wizard)
    round_rect(d, (120, 650, 1480, 900), 18, WHITE, TEAL, 3)
    card(img, d, "elb.png", 280, 670, "Load balancer (hostname)", "created by Service notes")
    pill(d, "DELETE WITH THE SERVICE", 470, 675)
    card(img, d, "svc.png", 980, 670, "Service  notes", "type: LoadBalancer\nselector  app=notes")
    d.text((160, 850), "EXTERNAL-IP  is a hostname  (*.elb.amazonaws.com)  — not one IP, not CLUSTER-IP, not the node.", font=font(17), fill=INK)
    d.text((160, 878), "PORT(S)  80:30xxx/TCP   ·   browser uses 80   ·   30xxx is NodePort on the workers", font=font(16), fill=MUTED)

    # Public A
    round_rect(d, (120, 930, 1480, 1450), 22, PUB_FILL, PUB_LINE, 4)
    d.text((150, 948), "Public subnet A   ·   one AZ", font=font(20, True), fill=PUB_LINE)

    round_rect(d, (150, 1000, 760, 1410), 16, WHITE, PUB_LINE, 3)
    d.text((175, 1018), "Worker node  (node group)", font=font(18, True), fill=INK)
    card(img, d, "ec2.png", 290, 1060, "t3.small", "kubelet + runtime")
    card(img, d, "pod.png", 580, 1060, "Pod notes-api", "replicas: 1  ·  :8080\nPython list in RAM")
    d.text((175, 1335), "Scheduler placed the Pod on ONE node.", font=font(16), fill=MUTED)
    d.text((175, 1363), "The other node can stay empty. That is normal.", font=font(16), fill=MUTED)

    round_rect(d, (790, 1000, 1450, 1410), 16, WHITE, (148, 163, 184), 3)
    d.text((815, 1018), "Build box  (not a Kubernetes node)", font=font(18, True), fill=INK)
    card(img, d, "ec2.png", 960, 1060, "lec07-build", "t3.micro  ·  SSH 22 My IP")
    card(img, d, "docker.png", 1260, 1060, "docker build / push", "tag notes-api:l7")
    d.text((815, 1335), "Windows has no Docker Desktop.", font=font(16), fill=MUTED)
    d.text((815, 1363), "This box only builds. You can terminate it.", font=font(16), fill=MUTED)

    # Public B
    round_rect(d, (1540, 650, 2890, 1450), 22, PUB_FILL, PUB_LINE, 4)
    d.text((1570, 668), "Public subnet B   ·   second AZ", font=font(20, True), fill=PUB_LINE)
    d.text((1570, 702), "Two AZs so EKS and the load balancer can create.", font=font(16), fill=MUTED)

    round_rect(d, (1570, 750, 2280, 1180), 16, WHITE, PUB_LINE, 3)
    card(img, d, "ec2.png", 1760, 790, "t3.small", "second worker  ·  Ready")
    card(img, d, "node.png", 2080, 790, "No notes-api Pod", "kubelet still runs here")
    d.text((1600, 1105), "Empty of your app. Still a node.", font=font(16), fill=MUTED)

    round_rect(d, (2320, 750, 2860, 1180), 16, WHITE, EKS_LINE, 3)
    d.text((2350, 770), "Not on these EC2s", font=font(18, True), fill=EKS_LINE)
    d.text((2350, 820), "API server / etcd / scheduler", font=font(17), fill=INK)
    d.text((2350, 852), "The ELB hostname", font=font(17), fill=INK)
    d.text((2350, 884), "The ECR repo", font=font(17), fill=INK)
    d.text((2350, 940), "Those live with EKS / AWS,", font=font(16), fill=MUTED)
    d.text((2350, 968), "not inside the node group.", font=font(16), fill=MUTED)

    round_rect(d, (1570, 1220, 2860, 1410), 16, WHITE, (148, 163, 184), 3)
    d.text((1600, 1240), "Traffic once the page loads", font=font(18, True), fill=TEAL)
    d.text((1600, 1288), "browser  →  ELB :80  →  worker node  →  Pod :8080  →  HTML", font=font(18), fill=INK)
    d.text((1600, 1328), "CLUSTER-IP 172.20.x.x is only inside the cluster. Do not type it in Chrome.", font=font(16), fill=MUTED)
    d.text((1600, 1360), "Notes live in that one process. Delete the Pod → extras are gone.", font=font(16), fill=MUTED)

    # IAM strip
    round_rect(d, (120, 1480, 2890, 1615), 16, WHITE, (148, 163, 184), 3)
    d.text((150, 1498), "Three IAM roles  (three different computers)   ·   no AWS keys in the Pod or the Dockerfile", font=font(20, True), fill=INK)
    d.text((150, 1548), "lec07-eks-cluster-role", font=font(17, True), fill=EKS_LINE)
    d.text((150, 1574), "EKS control plane  ·  AmazonEKSClusterPolicy", font=font(15), fill=MUTED)
    d.text((900, 1548), "lec07-eks-node-role", font=font(17, True), fill=PUB_LINE)
    d.text((900, 1574), "Worker EC2s  ·  ECR ReadOnly (pull :l7)", font=font(15), fill=MUTED)
    d.text((1680, 1548), "lec07-ec2-ecr", font=font(17, True), fill=ECR_LINE)
    d.text((1680, 1574), "Build micro  ·  ECR PowerUser (docker push)", font=font(15), fill=MUTED)

    # IGW into VPC / ELB
    arrow(d, 260, 528, 260, 665, TEAL, 5)

    # ELB down to the Pod (label sits in the 30px gap, left of the line)
    polyline(d, [(280, 900), (280, 955), (580, 955), (580, 1055)], TEAL, 4)

    # footer
    d.text(
        (48, 1680),
        "replicas: 1 so Add and Show share one list. Delete the Pod → Deployment starts a new Pod with empty extras.",
        font=font(18),
        fill=INK,
    )
    d.text(
        (48, 1718),
        "Cleanup order:  kubectl delete svc notes  →  delete node group  →  delete cluster lec07-eks  →  terminate lec07-build  →  delete VPC notes-k8s",
        font=font(18, True),
        fill=RED,
    )
    d.text(
        (48, 1762),
        "Lecture 7 demo  ·  Not created: NAT, ALB wizard, private node subnets, AKS/GKE  ·  Icons: AWS architecture set + Kubernetes",
        font=font(16),
        fill=MUTED,
    )
    d.text(
        (48, 1794),
        "Lecture 11 project is still one EC2 + GitHub Actions. This cluster is class-only and billed while it exists.",
        font=font(16),
        fill=MUTED,
    )

    rgb = Image.new("RGB", img.size, BG)
    rgb.paste(img, mask=img.split()[-1])
    rgb.save(OUT, "PNG", optimize=True)
    print("Wrote", OUT, OUT.stat().st_size)


if __name__ == "__main__":
    main()
