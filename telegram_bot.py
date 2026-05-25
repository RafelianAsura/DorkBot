import requests
from config import BOT_TOKEN, CHAT_ID


def send_telegram(message):

    try:

        response = requests.post(
            f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
            data={
                "chat_id": CHAT_ID,
                "text": message
            },
            timeout=10
        )

        print("[TELEGRAM SENT]")

    except Exception as e:

        print(f"[TELEGRAM ERROR] {e}")
