import os
import requests

TOKEN = os.environ.get("TNMGRMU_BOT_TOKEN")
CHAT_ID = os.environ.get("TNMGRMU_CHAT_ID")

response = requests.post(
    f"https://api.telegram.org/bot{TOKEN}/sendMessage",
    data={
        "chat_id": CHAT_ID,
        "text": "✅ FINAL CONFIRMATION TEST PASSED\n\nTelegram bot is working perfectly 🎉"
    }
)

print("STATUS CODE:", response.status_code)
print("RESPONSE:", response.text)

