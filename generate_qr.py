import qrcode
import os

# GitHub Pages base URL for your AR summary project
BASE_URL = "https://xinchaonnv.github.io/AR-Fortune-Bullet-Journey-Recap/?player="

# List of player JSON IDs
PLAYER_IDS = ["player001", "player002", "player003"]  # Extend this as needed

# Output folder for QR codes
OUTPUT_DIR = "qr-codes"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Generate QR PNGs for each player
for player_id in PLAYER_IDS:
    full_url = f"{BASE_URL}{player_id}"
    qr_img = qrcode.make(full_url)
    qr_img.save(os.path.join(OUTPUT_DIR, f"{player_id}.png"))
    print(f"[✓] QR saved for {player_id}: {full_url}")