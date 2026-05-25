# Dorkbot

Automated Google dorking for domain security monitoring and threat detection

## Features

✅ Automated Google dorking with SerpAPI  
✅ Intelligent scoring system for threat detection  
✅ Real-time Telegram alerts  
✅ HTML content analysis  
✅ Duplicate detection  
✅ URL filtering & deduplication  
✅ Detailed logging  

## Setup

### 1. Clone & Install

```bash
git clone https://github.com/RafelianAsura/DorkBot.git
cd dorkbot
```

### 2. Install Dependencies

```powershell
pip install -r requirements.txt
```

### 3. Configure Credentials

Copy `.env.example` to `.env` and fill in your credentials:

```bash
cp .env.example .env
```

Edit `.env`:
```env
SERP_API_KEY=your_serpapi_key
BOT_TOKEN=your_telegram_bot_token
CHAT_ID=your_chat_id
```

**Get your credentials:**
- **SERP_API_KEY**: [serpapi.com](https://serpapi.com)
- **BOT_TOKEN**: [@BotFather](https://t.me/botfather) on Telegram
- **CHAT_ID**: Send a message to your bot, then get ID from `@userinfobot`

### 4. Configure Targets

Edit `config.py` to add your target domains and search queries:

```python
DOMAINS = [
    "example.com",
    "subdomain.example.com"
]

QUERY_GROUPS = [
    "(malware OR phishing OR defacement)",
    "(other OR search OR terms)",
]
```

### 5. Run

```powershell
py main.py
```

## Project Structure

```
dorkbot/
├── main.py              # Entry point
├── scanner.py           # SERP scanning engine
├── scoring.py           # Threat scoring system
├── telegram_bot.py      # Telegram notifications
├── config.py            # Configuration & env vars
├── requirements.txt     # Dependencies
├── .env.example         # Environment template
├── README.md            # This file
└── logs/
    └── results.txt      # Scan results log
```

## How It Works

1. **Scanning** → Uses Google dorking + SerpAPI to find results
2. **Scoring** → Analyzes title, snippet, and HTML for threat keywords
3. **Filtering** → Removes duplicates and low-confidence results
4. **Alerting** → Sends high-confidence findings to Telegram
5. **Logging** → Saves all results to `logs/results.txt`

## Scoring System

- **Suspicious keywords** add points (higher = more suspicious)
- **Safe keywords** subtract points (detected defenses)
- **Threshold**: Results with score ≥ 8 are alerted

## Security

⚠️ **IMPORTANT**
- Never commit `.env` with real credentials
- Use `.env.example` as template for others
- Rotate API keys if accidentally exposed
- This tool is for defensive/monitoring use only

## License

MIT
