import requests
import hashlib

URL = "https://cms2results.tnmgrmuexam.ac.in/#/ExamResult"

def get_hash():
    r = requests.get(URL, timeout=20)
    return hashlib.md5(r.text.encode()).hexdigest()

def send_telegram(msg, token, chat_id):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    requests.post(url, json={"chat_id": chat_id, "text": msg})

def main():
    with open("hash.txt", "r") as f:
        old_hash = f.read()

    new_hash = get_hash()
    if new_hash != old_hash:
        send_telegram(
            "🚨 TNMGRMU Result Update Detected!\n\nhttps://cms2results.tnmgrmuexam.ac.in/#/ExamResult",
            TOKEN, CHAT_ID
        )
        with open("hash.txt", "w") as f:
            f.write(new_hash)

if __name__ == "__main__":
    main()
