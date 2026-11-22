"""Lecture 8 beginner diagrams — official AWS / Kubernetes icons."""
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


def path():
    W, H = 2800, 980
    img = Image.new("RGBA", (W, H), BG + (255,))
    d = ImageDraw.Draw(img)
    header(d, W, "Today’s path  ·  same cluster, new behaviour", "You already know apply / get / browser. Today you change copies, settings, and a broken Pod.")
    steps = [
        ("eks.png", "1. Cluster", "reuse lec07-eks\nor recreate it\nthen let it cook"),
        ("docker.png", "2. Image :l8", "tiny EC2\nPAGE_TITLE from env\npush to ECR"),
        ("rs.png", "3. replicas 2", "two Pods\none Service URL\ntwo Python lists"),
        ("api.png", "4. ConfigMap", "change the title\nrollout restart\nno new docker build"),
        ("pod.png", "5. Break + undo", "ImagePullBackOff\nCrashLoopBackOff\nPending → undo"),
        ("user.png", "6. Delete", "Service first\nthen node group\nthen the cluster"),
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
    d.text((80, 800), "EKS is billed while it exists. Delete it before you leave — same rule as lecture 7.", font=font(22), fill=ORANGE)
    save(img, "today-path.png")


def two_lists():
    W, H = 2800, 980
    img = Image.new("RGBA", (W, H), BG + (255,))
    d = ImageDraw.Draw(img)
    header(d, W, "One URL. Two Pods. Two memories.", "The Service picks a Pod for each click. RAM is not shared.")

    round_rect(d, (80, 160, 720, 900), 22, AWS, None, 0)
    paste(img, load_icon("user.png", 90), 315, 220)
    center_text(d, "Your browser", 400, 340, font(26, True), WHITE)
    center_text(d, "http://EXTERNAL-IP/", 400, 410, font(22), (148, 163, 184))
    center_text(d, "Add note", 400, 500, font(22, True), (94, 234, 212))
    center_text(d, "Show notes", 400, 560, font(22, True), (94, 234, 212))
    center_text(d, "Watch the Pod name", 400, 680, font(20), (148, 163, 184))
    center_text(d, "in the footer.", 400, 720, font(20), (148, 163, 184))

    arrow(d, 740, 480, 920, 480)

    round_rect(d, (940, 300, 1480, 700), 22, WHITE, TEAL, 4)
    paste(img, load_icon("svc.png", 88), 1166, 330)
    center_text(d, "Service  notes", 1210, 440, font(24, True), INK)
    center_text(d, "one hostname", 1210, 500, font(20), MUTED)
    center_text(d, "picks A or B per request", 1210, 550, font(20), MUTED)

    arrow(d, 1500, 400, 1680, 280)
    arrow(d, 1500, 560, 1680, 680)

    round_rect(d, (1700, 160, 2720, 480), 22, (236, 253, 245), TEAL, 4)
    paste(img, load_icon("pod.png", 80), 1760, 190)
    d.text((1870, 200), "Pod A   notes-aaaa", font=font(26, True), fill=INK)
    d.text((1760, 300), "Python list in THIS process", font=font(22), fill=MUTED)
    d.text((1760, 360), "1 Linux   2 REST APIs   + your extra line", font=font(22), fill=TEAL)

    round_rect(d, (1700, 540, 2720, 900), 22, (255, 247, 237), ORANGE, 4)
    paste(img, load_icon("pod.png", 80), 1760, 570)
    d.text((1870, 580), "Pod B   notes-bbbb", font=font(26, True), fill=INK)
    d.text((1760, 670), "A different Python list", font=font(22), fill=MUTED)
    d.text((1760, 730), "1 Linux   2 REST APIs   (extra line missing)", font=font(22), fill=ORANGE)
    save(img, "two-lists.png")


def config_vs_image():
    W, H = 2800, 980
    img = Image.new("RGBA", (W, H), BG + (255,))
    d = ImageDraw.Draw(img)
    header(d, W, "The image is the app. The ConfigMap is the heading.", "You already know docker build. Today you change text without a new image.")

    round_rect(d, (80, 160, 1360, 900), 24, WHITE, (148, 163, 184), 4)
    paste(img, load_icon("docker.png", 100), 140, 200)
    d.text((280, 220), "Inside notes-api:l8  (the image)", font=font(28, True), fill=INK)
    for i, t in enumerate([
        "Python that serves the HTML page",
        "Listens on 0.0.0.0:8080",
        "Reads PAGE_TITLE when it starts",
        "You built this once on the tiny EC2",
        "Changing the title does not need docker build",
    ]):
        d.text((140, 360 + i * 80), "•  " + t, font=font(24), fill=MUTED)

    round_rect(d, (1440, 160, 2720, 900), 24, (236, 253, 245), TEAL, 4)
    paste(img, load_icon("api.png", 100), 1500, 200)
    d.text((1640, 220), "ConfigMap  notes-config", font=font(28, True), fill=INK)
    for i, t in enumerate([
        "PAGE_TITLE: notes-api",
        "PAGE_SUB: Two Pods mean two lists.",
        "Attached as env vars (envFrom)",
        "kubectl edit → change the title",
        "rollout restart → Pods reread it",
    ]):
        d.text((1500, 360 + i * 80), "•  " + t, font=font(24), fill=INK)
    save(img, "config-vs-image.png")


def secret_vs_config():
    W, H = 2800, 900
    img = Image.new("RGBA", (W, H), BG + (255,))
    d = ImageDraw.Draw(img)
    header(d, W, "ConfigMap vs Secret — same idea, different object", "Secret is still visible to anyone with kubectl. Base64 is not encryption.")

    round_rect(d, (80, 180, 1360, 820), 24, (236, 253, 245), TEAL, 4)
    d.text((140, 220), "ConfigMap", font=font(32, True), fill=TEAL)
    d.text((140, 300), "Settings you would not mind in a screenshot.", font=font(22), fill=MUTED)
    d.text((140, 400), "PAGE_TITLE = Lecture 8 notes", font=font(24, True), fill=INK)
    d.text((140, 470), "kubectl get configmap  shows the words.", font=font(22), fill=MUTED)
    d.text((140, 560), "Today: the heading on the HTML page.", font=font(22), fill=INK)

    round_rect(d, (1440, 180, 2720, 820), 24, (255, 247, 237), ORANGE, 4)
    d.text((1500, 220), "Secret", font=font(32, True), fill=ORANGE)
    d.text((1500, 300), "A dummy class token. Not an AWS key.", font=font(22), fill=MUTED)
    d.text((1500, 400), "NOTES_TOKEN  →  stored as base64", font=font(24, True), fill=INK)
    d.text((1500, 470), "The page prints the dummy token so you see the app read it.", font=font(22), fill=MUTED)
    d.text((1500, 540), "A real app would not print this. Not an AWS key.", font=font(20), fill=MUTED)
    save(img, "secret-vs-config.png")


def crash_states():
    W, H = 2800, 980
    img = Image.new("RGBA", (W, H), BG + (255,))
    d = ImageDraw.Draw(img)
    header(d, W, "Three unhappy states  ·  read Events, do not guess", "kubectl describe pod  and  kubectl logs  are the two tools today.")

    cards = [
        ((239, 246, 255), (37, 99, 235), "Pending", "The Pod has no node yet.", [
            "Today: memory request 8Gi.",
            "The t3.small cannot fit it.",
            "Events: Insufficient memory.",
            "It is waiting. It did not crash.",
        ]),
        ((255, 247, 237), ORANGE, "ImagePullBackOff", "The node cannot pull the image.", [
            "Today: tag :no-such-tag.",
            "ECR has :l8, not that tag.",
            "Events: Failed to pull image.",
            "Fix the URI, then undo.",
        ]),
        ((254, 226, 226), RED, "CrashLoopBackOff", "The process starts, then exits.", [
            "Today: CRASH=1.",
            "Python prints one line and dies.",
            "kubelet tries again, then waits.",
            "kubectl logs shows the line.",
        ]),
    ]
    for i, (fill, line, title, one, bullets) in enumerate(cards):
        x = 80 + i * 900
        round_rect(d, (x, 160, x + 840, 900), 24, fill, line, 4)
        center_text(d, title, x + 420, 200, font(30, True), line)
        center_text(d, one, x + 420, 270, font(22), INK)
        yy = 380
        for t in bullets:
            d.text((x + 80, yy), "•  " + t, font=font(22), fill=INK)
            yy += 90
    save(img, "crash-states.png")


def rollout():
    W, H = 2800, 900
    img = Image.new("RGBA", (W, H), BG + (255,))
    d = ImageDraw.Draw(img)
    header(d, W, "A rollout is a new ReplicaSet. Undo goes back.", "Deployment keeps the previous ReplicaSet for a while. That is why undo works.")

    boxes = [
        (80, TEAL, "1. Working", ":l8  ·  2 Running Pods\nheading from ConfigMap"),
        (760, ORANGE, "2. You change it", "wrong tag, or CRASH=1,\nor 8Gi request"),
        (1440, RED, "3. Unhappy", "ImagePull / CrashLoop / Pending\ndescribe + logs"),
        (2120, TEAL, "4. Undo", "kubectl rollout undo\nback to the last good ReplicaSet"),
    ]
    for x, color, title, body in boxes:
        round_rect(d, (x, 220, x + 600, 720), 22, WHITE, color, 4)
        center_text(d, title, x + 300, 280, font(26, True), color)
        yy = 400
        for line in body.split("\n"):
            center_text(d, line, x + 300, yy, font(22), MUTED)
            yy += 50
        if x < 2000:
            arrow(d, x + 610, 470, x + 750, 470)
    save(img, "rollout.png")


def clouds():
    W, H = 2800, 900
    img = Image.new("RGBA", (W, H), BG + (255,))
    d = ImageDraw.Draw(img)
    header(d, W, "Same YAML on three clouds", "replicas, ConfigMap, Secret, kubectl rollout. Only the cluster product name changes.")
    cols = [
        (120, AWS, "AWS (you click)", "eks.png", "EKS", "You already created this.\nSame kubectl today."),
        (980, AZURE, "Azure (name only)", "aks.png", "AKS", "Same YAML.\nYou do not open Azure."),
        (1840, GCP, "GCP (name only)", "gke.png", "GKE", "Same YAML.\nYou do not open GCP."),
    ]
    for x, color, title, ic, name, body in cols:
        round_rect(d, (x, 160, x + 840, 820), 24, WHITE, color, 4)
        d.rectangle((x, 160, x + 840, 250), fill=color)
        center_text(d, title, x + 420, 185, font(26, True), WHITE)
        paste(img, load_icon(ic, 100), x + 370, 290)
        center_text(d, name, x + 420, 420, font(32, True), INK)
        yy = 530
        for line in body.split("\n"):
            center_text(d, line, x + 420, yy, font(22), MUTED)
            yy += 50
    save(img, "three-clouds.png")


def helm_vs_apply():
    W, H = 2800, 980
    img = Image.new("RGBA", (W, H), BG + (255,))
    d = ImageDraw.Draw(img)
    header(d, W, "You already apply YAML. Helm is that folder in one command.", "Same Pods. Same Service. Same ConfigMap. Not a second Kubernetes.")
    round_rect(d, (80, 160, 1360, 900), 24, WHITE, (148, 163, 184), 4)
    d.text((140, 200), "What you type today", font=font(28, True), fill=INK)
    for i, t in enumerate([
        "sed  IMAGE  →  $URI:l8",
        "kubectl apply -f configmap.yaml",
        "kubectl apply -f secret.yaml",
        "kubectl apply -f deployment.yaml",
        "kubectl apply -f service.yaml",
        "Four files. Easy for notes-api.",
        "Painful for 20 files or 3 environments.",
    ]):
        d.text((140, 290 + i * 75), "•  " + t, font=font(22), fill=MUTED)
    round_rect(d, (1440, 160, 2720, 900), 24, (236, 253, 245), TEAL, 4)
    d.text((1500, 200), "The Helm version of the same thing", font=font(28, True), fill=INK)
    for i, t in enumerate([
        "templates/  = those YAML files",
        "values.yaml = the IMAGE blank",
        "Chart.yaml  = name + version of the folder",
        "helm install notes ./helm/notes-api \\",
        "         --set image=$URI:l8",
        "helm uninstall notes  = delete that install",
        "Release = this install, named notes.",
    ]):
        d.text((1500, 290 + i * 75), "•  " + t, font=font(22), fill=INK)
    save(img, "helm-vs-apply.png")


def probes():
    W, H = 2800, 980
    img = Image.new("RGBA", (W, H), BG + (255,))
    d = ImageDraw.Draw(img)
    header(d, W, "Two questions kubelet asks /health", "Same URL. Two different jobs if the answer is no.")
    round_rect(d, (80, 160, 1360, 900), 24, (254, 226, 226), RED, 4)
    paste(img, load_icon("kubelet.png", 90), 140, 200)
    d.text((260, 220), "Liveness  ·  are you alive?", font=font(28, True), fill=RED)
    for i, t in enumerate([
        "kubelet GET /health every few seconds.",
        "If it fails: restart this container.",
        "The Pod name may stay. Restarts go up.",
        "Real: notes-api hung, not crashing, not answering.",
        "Shop closed. Restart the process.",
        "Today: point liveness at /nope, watch Restarts.",
    ]):
        d.text((140, 360 + i * 75), "•  " + t, font=font(22), fill=INK)
    round_rect(d, (1440, 160, 2720, 900), 24, (239, 246, 255), (37, 99, 235), 4)
    paste(img, load_icon("svc.png", 90), 1500, 200)
    d.text((1620, 220), "Readiness  ·  send traffic?", font=font(28, True), fill=(37, 99, 235))
    for i, t in enumerate([
        "Same GET /health.",
        "If it fails: do NOT restart.",
        "Take this Pod out of the Service.",
        "kubectl get pods shows Running 0/1 Ready.",
        "Real: app still loading. Door stays shut.",
        "Today: point readiness at /nope, browser hangs.",
    ]):
        d.text((1500, 360 + i * 75), "•  " + t, font=font(22), fill=INK)
    save(img, "probes.png")


def rbac_pic():
    W, H = 2800, 900
    img = Image.new("RGBA", (W, H), BG + (255,))
    d = ImageDraw.Draw(img)
    header(d, W, "RBAC  ·  who may do which verb on which object", "You already used this: lecture 7 access entry made CloudShell an admin.")
    cols = [
        (80, TEAL, "You (today)", "Cluster admin via EKS access entry.\nkubectl apply, delete, describe — all allowed.\nThat is why CloudShell worked."),
        (980, (37, 99, 235), "notes-reader (demo)", "A ServiceAccount + Role: get,list pods only.\nauth can-i get pods → yes.\nauth can-i delete pods → no."),
        (1880, ORANGE, "Real job later", "CI pipeline may apply a Deployment.\nAn intern may only get pods.\nNobody’s laptop deletes the cluster."),
    ]
    for x, color, title, body in cols:
        round_rect(d, (x, 180, x + 840, 820), 22, WHITE, color, 4)
        center_text(d, title, x + 420, 220, font(26, True), color)
        yy = 320
        for line in body.split("\n"):
            center_text(d, line, x + 420, yy, font(22), MUTED)
            yy += 70
    save(img, "rbac.png")


def resources_pic():
    W, H = 2800, 900
    img = Image.new("RGBA", (W, H), BG + (255,))
    d = ImageDraw.Draw(img)
    header(d, W, "Request = reservation. Limit = cap.", "The scheduler uses requests. kubelet enforces limits.")
    round_rect(d, (80, 180, 1360, 820), 24, (236, 253, 245), TEAL, 4)
    d.text((140, 220), "requests  (today: 64Mi)", font=font(30, True), fill=TEAL)
    d.text((140, 320), "“I need this much seat on the node.”", font=font(24), fill=INK)
    d.text((140, 400), "If no node has 8Gi free → Pending.", font=font(24), fill=INK)
    d.text((140, 480), "Real: two apps. One asks for 7Gi on a 2Gi node.", font=font(22), fill=MUTED)
    d.text((140, 540), "The second app waits. It did not crash.", font=font(22), fill=MUTED)
    round_rect(d, (1440, 180, 2720, 820), 24, (255, 247, 237), ORANGE, 4)
    d.text((1500, 220), "limits  (today: 128Mi)", font=font(30, True), fill=ORANGE)
    d.text((1500, 320), "“You may not use more than this.”", font=font(24), fill=INK)
    d.text((1500, 400), "Over the memory limit → kubelet kills the container.", font=font(24), fill=INK)
    d.text((1500, 480), "Real: a leak would take the whole node down.", font=font(22), fill=MUTED)
    d.text((1500, 540), "The limit protects the node, not your notes.", font=font(22), fill=MUTED)
    save(img, "resources.png")


if __name__ == "__main__":
    path()
    two_lists()
    config_vs_image()
    secret_vs_config()
    crash_states()
    rollout()
    clouds()
    helm_vs_apply()
    probes()
    rbac_pic()
    resources_pic()

