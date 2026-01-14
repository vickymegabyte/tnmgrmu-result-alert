import requests
import hashlib
import os

URL = "https://cms2results.tnmgrmuexam.ac.in/#/ExamResult"

TOKEN = os.environ.get("TNMGRMU_BOT_TOKEN")
CHAT_ID = os.environ.get("TNMGRMU_CHAT_ID")

if not TOKEN or not CHAT_ID:
    raise ValueError("Telegram BOT TOKEN or CHAT ID not set")


def get_hash():
    r = requests.get(URL, timeout=20)
    return hashlib.md5(r.text.encode()).hexdigest()

def send_telegram(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, json={
        "chat_id": CHAT_ID,
        "text": msg
    })

def main():
    with open("hash.txt", "r") as f:
        old_hash = f.read().strip()

    new_hash = get_hash()

    if new_hash != old_hash:
        send_telegram(
            "🚨 TNMGRMU Result Update Detected!\n\n"
            "https://cms2results.tnmgrmuexam.ac.in/#/ExamResult"
        )
        with open("hash.txt", "w") as f:
            f.write(new_hash)

if __name__ == "__main__":
    main()
