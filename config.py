from dotenv import load_dotenv
import os

load_dotenv()

SERP_API_KEY = os.getenv("SERP_API_KEY")
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

DOMAINS = [
    "bekasikota.go.id",
    "rsud.bekasikota.go.id"
]

QUERY_GROUPS = [
    "(slot OR gacor OR maxwin OR pragmatic OR sbobet OR togel OR casino OR slot88 OR judi online)",
    "(エロアニメ OR シャツ OR ジーンズ OR サンダル OR 東京)",
]
