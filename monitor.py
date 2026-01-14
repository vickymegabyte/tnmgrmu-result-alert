import requests
import hashlib
import os

URL = "https://cms2results.tnmgrmuexam.ac.in/#/ExamResult"

BOT_TOKEN = os.environ["TNMGRMU_BOT_TOKEN"]
CHAT_ID = os.environ["TNMGRMU_CHAT_ID"]

# Keywords to detect B.Pharm results
KEYWORDS = ["B.PHARM", "BPHARM", "B PHARM", "PHARMACY","MPHARM","M PHARM", "M.PHARM", "PHARM"]

def get_page_content():
    response = requests.get(URL, timeout=20)
    response.raise_for_status()
    return response.text.upper()

def get_hash(content):
    return hashlib.md5(content.encode()).hexdigest()

def send_telegram(message):
    telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }
    requests.post(telegram_url, json=payload)

def contains_bpharm(content):
    return any(keyword in content for keyword in KEYWORDS)

def main():
    send_telegram("🧪 TEST ALERT\n\nYour TNMGRMU Result Alert Bot is working correctly ✅")

    # Read old hash
    try:
        with open("hash.txt", "r") as f:
            old_hash = f.read()
    except FileNotFoundError:
        old_hash = ""

    # Update hash file
    with open("hash.txt", "w") as f:
        f.write(current_hash)

    # Alert only if page changed AND B.Pharm mentioned
    if current_hash != old_hash and contains_bpharm(content):
        send_telegram(
            "🎓 **B.PHARM RESULT PUBLISHED (TNMGRMU)**\n\n"
            "Check now:\n"
            "https://cms2results.tnmgrmuexam.ac.in/#/ExamResult"
        )

if __name__ == "__main__":
    main()
