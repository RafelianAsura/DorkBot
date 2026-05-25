import re

SUSPICIOUS_KEYWORDS = {
    "slot": 2,
    "gacor": 3,
    "maxwin": 3,
    "casino": 3,
    "togel": 3,
    "sbobet": 4,
    "pragmatic": 4,
    "slot88": 4,
    "judol": 3,
    "judi": 1,
}

SAFE_KEYWORDS = {
    "tolak": -5,
    "stop": -5,
    "edukasi": -4,
    "sosialisasi": -4,
    "himbauan": -4,
    "berita": -2,
}

REGEX_PATTERNS = [
    r"slot\d+",
    r"gacor",
    r"maxwin",
    r"pragmatic",
]


def calculate_score(text):

    score = 0

    suspicious_found = []
    safe_found = []

    lower = text.lower()

    for word, value in SUSPICIOUS_KEYWORDS.items():

        if word in lower:
            score += value
            suspicious_found.append(word)

    for word, value in SAFE_KEYWORDS.items():

        if word in lower:
            score += value
            safe_found.append(word)

    for pattern in REGEX_PATTERNS:

        if re.search(pattern, lower):
            score += 2

    return score, suspicious_found, safe_found
