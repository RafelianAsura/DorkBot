from serpapi import GoogleSearch
from bs4 import BeautifulSoup
import requests

from config import SERP_API_KEY
from scoring import calculate_score

EXCLUDE_URLS = [
    "/video",
    "/galeri",
    "/tag/",
    "/category/",
    ".pdf"
]

seen_links = set()


def analyze_html(url):

    try:

        response = requests.get(
            url,
            timeout=10,
            headers={
                "User-Agent": "Mozilla/5.0"
            }
        )

        html = response.text.lower()

        soup = BeautifulSoup(html, "html.parser")

        body_text = soup.get_text(" ")[:5000]

        combined = html + " " + body_text

        return calculate_score(combined)

    except:

        return 0, [], []



def scan_domain(domain, query_group):

    dork = f"{query_group} site:{domain}"

    print(f"\n[SEARCH] {dork}")

    params = {
        "engine": "google",
        "q": dork,
        "api_key": SERP_API_KEY,
        "num": 10,
    }

    search = GoogleSearch(params)

    results = search.get_dict()

    organic_results = results.get("organic_results", [])

    findings = []

    for result in organic_results:

        title = result.get("title", "")
        link = result.get("link", "")
        snippet = result.get("snippet", "")

        if not link:
            continue

        lower_link = link.lower()

        if link in seen_links:
            continue

        skip = False

        for bad_url in EXCLUDE_URLS:

            if bad_url in lower_link:
                skip = True
                break

        if skip:
            continue

        seen_links.add(link)

        serp_text = title + " " + snippet

        serp_score, bad1, safe1 = calculate_score(serp_text)

        html_score, bad2, safe2 = analyze_html(link)

        final_score = serp_score + html_score

        if final_score < 8:
            continue

        findings.append({
            "title": title,
            "link": link,
            "score": final_score,
            "bad": list(set(bad1 + bad2)),
            "safe": list(set(safe1 + safe2))
        })

    return findings
