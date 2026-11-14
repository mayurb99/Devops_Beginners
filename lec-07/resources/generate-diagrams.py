"""Lecture 7 diagrams — official AWS / Kubernetes / Azure / GCP icons."""
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
ORANGE = (180, 83, 9)
AWS = (15, 23, 42)
AZURE = (0, 90, 158)
GCP = (26, 115, 232)


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


def arrow(draw, x1, y1, x2, y2, color=TEAL, width=5):
    draw.line((x1, y1, x2, y2), fill=color, width=width)
    ang = math.atan2(y2 - y1, x2 - x1)
    L = 18
    for d in (2.4, -2.4):
        ax = x2 - L * math.cos(ang + d * 0.28)
        ay = y2 - L * math.sin(ang + d * 0.28)
        draw.line((x2, y2, ax, ay), fill=color, width=width)


def header(draw, w, title, sub):
    draw.rectangle((0, 0, w, 110), fill=TEAL)
    draw.text((48, 22), title, font=font(36, True), fill=WHITE)
    draw.text((48, 70), sub, font=font(20), fill=(204, 251, 241))


def save(img, name):
    rgb = Image.new("RGB", img.size, BG)
    rgb.paste(img, mask=img.split()[-1])
    out = OUT_DIR / name
    rgb.save(out, "PNG", optimize=True)
    print("Wrote", out, out.stat().st_size)


def fargate_vs_k8s():
    W, H = 2800, 980
    img = Image.new("RGBA", (W, H), BG + (255,))
    d = ImageDraw.Draw(img)
    header(d, W, "Lecture 6 ran one container. Lecture 7 runs a cluster.", "Fargate is still correct for one task. Kubernetes is for many copies, restarts, and a stable door.")

    round_rect(d, (80, 160, 1360, 900), 24, AWS, None, 0)
    paste(img, load_icon("fargate.png", 110), 140, 200)
    d.text((280, 220), "Fargate (lecture 6)", font=font(32, True), fill=WHITE)
    d.text((280, 270), "One image. One task. You do not SSH.", font=font(22), fill=(148, 163, 184))
    for i, t in enumerate([
        "You gave AWS the ECR URI :l6.",
        "AWS started one container.",
        "If it died, a service started another copy — still one at a time today.",
        "No built-in “keep 3, roll to a new tag, undo”.",
        "Fine for a single notes-api demo.",
    ]):
        d.text((140, 370 + i * 80), "•  " + t, font=font(24), fill=(226, 232, 240))

    round_rect(d, (1440, 160, 2720, 900), 24, (236, 253, 245), TEAL, 4)
    paste(img, load_icon("eks.png", 110), 1500, 200)
    d.text((1640, 220), "Kubernetes / EKS (today)", font=font(32, True), fill=INK)
    d.text((1640, 270), "A control plane plus worker computers.", font=font(22), fill=MUTED)
    for i, t in enumerate([
        "You describe the desired state in YAML.",
        "Deployment keeps N Pods of notes-api.",
        "If you delete one Pod, a new one appears.",
        "Service gives one URL while Pod IPs change.",
        "Same notes-api image from ECR.",
    ]):
        d.text((1500, 370 + i * 80), "•  " + t, font=font(24), fill=INK)
    save(img, "fargate-vs-k8s.png")


def cluster():
    W, H = 2800, 1100
    img = Image.new("RGBA", (W, H), BG + (255,))
    d = ImageDraw.Draw(img)
    header(d, W, "A cluster is two parts: brain and workers", "You do not install etcd yourself. EKS runs the control plane. You add worker nodes.")

    round_rect(d, (80, 160, 1360, 1040), 24, WHITE, AWS, 4)
    d.rectangle((80, 160, 1360, 240), fill=AWS)
    center_text(d, "Control plane  (EKS creates this)", 720, 180, font(26, True), WHITE)
    items = [
        ("api.png", "API server", "The only door. kubectl talks here."),
        ("etcd.png", "etcd", "The cluster’s memory: what should be running."),
        ("sched.png", "Scheduler", "Picks a node for each new Pod."),
        ("c-c-m.png", "Controller manager", "Watches desired vs actual. Fixes drift."),
    ]
    for i, (ic, title, sub) in enumerate(items):
        y = 280 + i * 180
        paste(img, load_icon(ic, 88), 140, y)
        d.text((260, y + 8), title, font=font(26, True), fill=INK)
        d.text((260, y + 52), sub, font=font(20), fill=MUTED)

    round_rect(d, (1440, 160, 2720, 1040), 24, WHITE, TEAL, 4)
    d.rectangle((1440, 160, 2720, 240), fill=TEAL)
    center_text(d, "Worker node  (your node group)", 2080, 180, font(26, True), WHITE)
    items = [
        ("node.png", "Node", "An EC2 computer in your VPC. t3.small today."),
        ("kubelet.png", "kubelet", "Agent on the node. Starts what the API asked."),
        ("docker.png", "Container runtime", "Runs the notes-api container inside a Pod."),
        ("pod.png", "Your Pod", "notes-api listening on 0.0.0.0:8080."),
    ]
    for i, (ic, title, sub) in enumerate(items):
        y = 280 + i * 180
        paste(img, load_icon(ic, 88), 1500, y)
        d.text((1620, y + 8), title, font=font(26, True), fill=INK)
        d.text((1620, y + 52), sub, font=font(20), fill=MUTED)
    save(img, "cluster.png")


def objects():
    W, H = 2800, 980
    img = Image.new("RGBA", (W, H), BG + (255,))
    d = ImageDraw.Draw(img)
    header(d, W, "Four objects you will actually use", "You apply YAML. Kubernetes creates the ones underneath.")

    cards = [
        ("pod.png", "Pod", "Smallest unit that runs.\nOne notes-api container today.\nGets its own IP inside the cluster.\nDies → that IP is gone."),
        ("rs.png", "ReplicaSet", "“Keep this many Pods.”\nYou rarely create it by hand.\nA Deployment owns it.\nDeletes extra Pods, makes missing ones."),
        ("deploy.png", "Deployment", "The object you apply.\nOwns the ReplicaSet.\nreplicas: 1 today.\nLater: roll to a new image."),
        ("svc.png", "Service", "Stable name + port.\nSelects Pods by label app=notes.\nLoadBalancer → public URL.\nBrowser talks here, not to a Pod IP."),
    ]
    for i, (ic, title, body) in enumerate(cards):
        x = 70 + i * 680
        round_rect(d, (x, 180, x + 640, 900), 22, WHITE, TEAL, 3)
        paste(img, load_icon(ic, 100), x + 270, 210)
        center_text(d, title, x + 320, 330, font(28, True), INK)
        yy = 400
        for line in body.split("\n"):
            center_text(d, line, x + 320, yy, font(20), MUTED)
            yy += 42
    save(img, "four-objects.png")


def labels():
    W, H = 2800, 900
    img = Image.new("RGBA", (W, H), BG + (255,))
    d = ImageDraw.Draw(img)
    header(d, W, "A Service finds Pods by label — not by IP", "selector app: notes  matches  template labels app: notes")

    round_rect(d, (80, 180, 900, 820), 22, WHITE, TEAL, 4)
    paste(img, load_icon("svc.png", 96), 442, 220)
    center_text(d, "Service  notes", 490, 340, font(26, True), INK)
    center_text(d, "selector: app = notes", 490, 400, font(22), MUTED)
    center_text(d, "port 80  →  target 8080", 490, 450, font(22), MUTED)
    center_text(d, "type: LoadBalancer", 490, 510, font(22, True), TEAL)

    arrow(d, 920, 500, 1180, 500)

    for i, name in enumerate(["Pod A", "Pod B (not today)"]):
        y = 200 + i * 320
        fill = (236, 253, 245) if i == 0 else (248, 250, 252)
        line = TEAL if i == 0 else (203, 213, 225)
        round_rect(d, (1200, y, 2000, y + 280), 22, fill, line, 4)
        paste(img, load_icon("pod.png", 80), 1260, y + 40)
        d.text((1380, y + 50), name, font=font(26, True), fill=INK)
        d.text((1380, y + 110), "label  app = notes" if i == 0 else "if it had a different label, Service would ignore it", font=font(20), fill=MUTED)
        d.text((1380, y + 160), "containerPort 8080", font=font(20), fill=MUTED)

    round_rect(d, (2120, 180, 2720, 820), 22, AWS, None, 0)
    paste(img, load_icon("user.png", 80), 2350, 260)
    center_text(d, "Your browser", 2420, 370, font(24, True), WHITE)
    center_text(d, "http://EXTERNAL-IP/", 2420, 440, font(22), (148, 163, 184))
    center_text(d, "Add note  /  Show notes", 2420, 510, font(22), (148, 163, 184))
    center_text(d, "Never uses the Pod IP", 2420, 600, font(20, True), (94, 234, 212))
    save(img, "labels.png")


def path():
    W, H = 2800, 980
    img = Image.new("RGBA", (W, H), BG + (255,))
    d = ImageDraw.Draw(img)
    header(d, W, "Today’s path  ·  VPC → ECR → EKS → your browser", "Service type LoadBalancer publishes a hostname. You do not create an ALB by hand.")

    steps = [
        ("vpc.png", "1. VPC", "2 public subnets\n2 AZs  ·  IGW\nno NAT today"),
        ("ecr.png", "2. ECR", "notes-api:l7\nprivate repo\nthis Region"),
        ("docker.png", "3. Build", "tiny EC2\ndocker build\ndocker push"),
        ("eks.png", "4. EKS", "control plane\n+ node group\npublic endpoint"),
        ("svc.png", "5. Service", "LoadBalancer\nport 80 → 8080\nEXTERNAL-IP"),
        ("user.png", "6. Browser", "HTML page\nAdd / Show notes\nsame process RAM"),
    ]
    for i, (ic, title, sub) in enumerate(steps):
        x = 60 + i * 455
        round_rect(d, (x, 200, x + 420, 720), 20, WHITE, TEAL, 3)
        paste(img, load_icon(ic, 96), x + 162, 240)
        center_text(d, title, x + 210, 360, font(24, True), INK)
        yy = 430
        for line in sub.split("\n"):
            center_text(d, line, x + 210, yy, font(20), MUTED)
            yy += 40
        if i < 5:
            arrow(d, x + 430, 460, x + 450, 460)
    d.text((80, 800), "EKS control plane is billed even with zero Pods. Delete the cluster before you leave. The LoadBalancer hostname dies with the Service.", font=font(22), fill=ORANGE)
    save(img, "today-path.png")


def clouds():
    W, H = 2800, 980
    img = Image.new("RGBA", (W, H), BG + (255,))
    d = ImageDraw.Draw(img)
    header(d, W, "Same Kubernetes. Three managed names.", "YAML (Pod, Deployment, Service) is the same. The control-plane product name changes.")
    cols = [
        (120, AWS, "AWS (you click today)", "eks.png", "EKS", "Elastic Kubernetes Service.\nAWS runs the API server.\nYou add nodes in your VPC."),
        (980, AZURE, "Azure (name only)", "aks.png", "AKS", "Azure Kubernetes Service.\nSame kubectl. Same YAML.\nYou do not open Azure today."),
        (1840, GCP, "GCP (name only)", "gke.png", "GKE", "Google Kubernetes Engine.\nSame kubectl. Same YAML.\nYou do not open GCP today."),
    ]
    for x, color, title, ic, name, body in cols:
        round_rect(d, (x, 160, x + 840, 900), 24, WHITE, color, 4)
        d.rectangle((x, 160, x + 840, 250), fill=color)
        center_text(d, title, x + 420, 185, font(26, True), WHITE)
        paste(img, load_icon(ic, 110), x + 365, 300)
        center_text(d, name, x + 420, 440, font(32, True), INK)
        yy = 530
        for line in body.split("\n"):
            center_text(d, line, x + 420, yy, font(22), MUTED)
            yy += 50
    save(img, "three-clouds.png")


def memory():
    W, H = 2800, 900
    img = Image.new("RGBA", (W, H), BG + (255,))
    d = ImageDraw.Draw(img)
    header(d, W, "Where a note lives  ·  no database", "POST appends a Python list inside that one process. Restart the Pod and the extra notes are gone.")
    round_rect(d, (80, 180, 1360, 820), 24, (236, 253, 245), TEAL, 4)
    paste(img, load_icon("pod.png", 100), 140, 220)
    d.text((280, 240), "Today: replicas 1", font=font(30, True), fill=INK)
    d.text((140, 360), "Browser Add note  →  this Pod’s RAM", font=font(24), fill=MUTED)
    d.text((140, 430), "Browser Show notes  →  the same list", font=font(24), fill=MUTED)
    d.text((140, 500), "You will see the new line on the page.", font=font(24), fill=TEAL)
    round_rect(d, (1440, 180, 2720, 820), 24, (255, 247, 237), ORANGE, 4)
    paste(img, load_icon("rs.png", 100), 1500, 220)
    d.text((1640, 240), "Later (lecture 8): replicas 2", font=font(30, True), fill=INK)
    d.text((1500, 360), "Two Pods = two separate lists.", font=font(24), fill=MUTED)
    d.text((1500, 430), "Add can land on Pod A. Show can land on Pod B.", font=font(24), fill=MUTED)
    d.text((1500, 500), "The note looks missing. RAM was never shared.", font=font(24), fill=ORANGE)
    d.text((1500, 600), "A real database would sit outside both Pods.", font=font(22), fill=MUTED)
    save(img, "memory.png")


if __name__ == "__main__":
    fargate_vs_k8s()
    cluster()
    objects()
    labels()
    path()
    clouds()
    memory()
