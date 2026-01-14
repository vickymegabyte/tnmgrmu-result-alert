import os
import requests

print("✅ Script started")

TOKEN = os.environ.get("TNMGRMU_BOT_TOKEN")
CHAT_ID = os.environ.get("TNMGRMU_CHAT_ID")

print("TOKEN:", "FOUND" if TOKEN else "MISSING")
print("CHAT_ID:", CHAT_ID if CHAT_ID else "MISSING")

def send_telegram(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    r = requests.post(url, json={
        "chat_id": CHAT_ID,
        "text": msg
    })
    print("Telegram response:", r.text)

def main():
    send_telegram("🧪 TEST ALERT — DEBUG MODE")

main()
