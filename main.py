import time
from datetime import datetime

from config import DOMAINS, QUERY_GROUPS
from scanner import scan_domain
from telegram_bot import send_telegram

print("\n=== DORKBOT START ===\n")

for domain in DOMAINS:

    print(f"\n===== {domain} =====")

    for query_group in QUERY_GROUPS:

        try:

            findings = scan_domain(domain, query_group)

            if not findings:
                print("[-] No suspicious results")
                continue

            for item in findings:

                title = item["title"]
                link = item["link"]
                score = item["score"]
                bad = ", ".join(item["bad"])
                safe = ", ".join(item["safe"])

                print(f"\n[FOUND] {title}")
                print(f"Score: {score}")

                message = f"""
🚨 HIGH CONFIDENCE RESULT

🌐 Domain:
{domain}

📊 Score:
{score}

⚠️ Suspicious:
{bad}

🛡️ Safe:
{safe}

📄 Title:
{title}

🔗 Link:
{link}
"""

                send_telegram(message)

                with open("logs/results.txt", "a", encoding="utf-8") as log:

                    log.write(f"[{datetime.now()}]\n")
                    log.write(f"DOMAIN: {domain}\n")
                    log.write(f"SCORE : {score}\n")
                    log.write(f"TITLE : {title}\n")
                    log.write(f"LINK  : {link}\n")
                    log.write("=" * 50 + "\n\n")

                time.sleep(2)

        except Exception as e:

            print(f"[ERROR] {e}")

        time.sleep(5)

print("\n=== FINISHED ===")
