# app/nodes/scrape.py
import requests
import trafilatura

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )
}

def scrape_node(state: dict) -> dict:
    urls = state.get("urls", [])
    print("📰 Scraping URLs:", urls)

    documents = []

    for url in urls:
        try:
            resp = requests.get(url, headers=HEADERS, timeout=15)
            if resp.status_code != 200 or not resp.text:
                print(f"⚠️ Failed to fetch: {url}")
                continue

            text = trafilatura.extract(
                resp.text,
                include_comments=False,
                include_tables=False
            )

            if text:
                documents.append(text.strip())

        except Exception as e:
            print(f"❌ Error scraping {url}: {e}")
            continue

    print(f"📰 Scraped {len(documents)} documents")
    state["documents"] = documents
    return state
