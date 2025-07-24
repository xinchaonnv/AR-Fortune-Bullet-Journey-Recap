import qrcode
import os

# ✅ Customize this with your GitHub Pages URL
BASE_URL = "https://xinchaonnv.github.io/AR-Fortune-Bullet-Journey-Recap/?player="

# ✅ Add your player IDs here
PLAYER_IDS = ["player001",]

# Create output folder
output_dir = "qr-codes"
os.makedirs(output_dir, exist_ok=True)

# Generate QR PNGs
for player_id in PLAYER_IDS:
    full_url = f"{BASE_URL}{player_id}"
    img = qrcode.make(full_url)
    img_path = os.path.join(output_dir, f"{player_id}.png")
    img.save(img_path)
    print(f"[✓] Saved QR for {player_id} → {full_url}")