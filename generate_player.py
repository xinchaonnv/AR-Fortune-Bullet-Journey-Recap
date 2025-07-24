import os
import sys
import json
import qrcode
import shutil
import subprocess

BASE_URL = "https://xinchaonnv.github.io/AR-Fortune-Bullet-Journey-Recap/"
TEMPLATE_FILE = "template.index.html"
OUTPUT_DIR = "qr-codes"

if len(sys.argv) != 3:
    print("Usage: python generate_player.py player042 '{\"class\": \"Mage\", ...}'")
    sys.exit(1)

player_id = sys.argv[1]
json_str = sys.argv[2]

player_dir = os.path.join(".", player_id)
stats_path = os.path.join(player_dir, "stats.json")
index_target = os.path.join(player_dir, "index.html")
qr_path = os.path.join(OUTPUT_DIR, f"{player_id}.png")

os.makedirs(player_dir, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

shutil.copyfile(TEMPLATE_FILE, index_target)
print(f"[✓] Copied index.html → {index_target}")

with open(stats_path, "w") as f:
    json.dump(json.loads(json_str), f, indent=2)
print(f"[✓] Created stats.json → {stats_path}")

url = f"{BASE_URL}{player_id}/"
img = qrcode.make(url)
img.save(qr_path)
print(f"[✓] QR code saved → {qr_path} → {url}")

try:
    subprocess.run(["git", "add", player_id], check=True)
    subprocess.run(["git", "commit", "-m", f"Add {player_id} summary"], check=True)
    subprocess.run(["git", "push"], check=True)
    print(f"[✓] Committed and pushed {player_id} to GitHub 🚀")
except subprocess.CalledProcessError as e:
    print(f"[✗] Git push failed: {e}")