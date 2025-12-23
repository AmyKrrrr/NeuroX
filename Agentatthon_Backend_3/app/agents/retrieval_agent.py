import time
import requests
import trafilatura
from ddgs import DDGS
from app.agents.base import BaseAgent
from app.agents.result import AgentResult

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

# Block forums/dictionaries to ensure we get articles
BLACKLIST = [
    "reddit.com", "quora.com", "stackexchange.com", "stackoverflow.com",
    "dictionary.com", "thesaurus.com", "merriam-webster.com", "wiktionary.org"
]

class RetrievalAgent(BaseAgent):
    name = "retrieval_agent"

    async def run(self, query: str) -> AgentResult:
        print(f"🌍 Searching for: {query}")
        urls = []

        # 1. SEARCH (Fetch 10 results to have a buffer)
        try:
            with DDGS() as ddgs:
                # Append "news" to query to avoid dictionary definitions
                search_query = query
                results = list(ddgs.text(search_query, max_results=10))
                
                if results:
                    for r in results:
                        link = r['href']
                        # Skip junk sites immediately
                        if any(bad in link for bad in BLACKLIST):
                            continue
                        urls.append(link)
        except Exception as e:
            print(f"⚠️ Search failed: {e}")
            return AgentResult(output=[], confidence=0.0, should_continue=False)

        # 2. PERSISTENT SCRAPING
        # We need 2 good docs. We will try ALL urls until we get them.
        print(f"🕷️ Processing {len(urls)} URLs to find 2 good ones...")
        docs = []
        
        for url in urls:
            if len(docs) >= 2: 
                break # Stop once we have 2 good articles
            
            try:
                # Add a tiny delay to be polite and avoid blocks
                time.sleep(0.5) 
                
                resp = requests.get(url, headers=HEADERS, timeout=5)
                if resp.status_code != 200: 
                    print(f"   ⚠️ Failed ({resp.status_code}): {url}")
                    continue
                
                text = trafilatura.extract(resp.text)
                
                # Check if we actually got text (and not just a cookie banner)
                if text and len(text) > 600:
                    print(f"   ✅ Scraped ({len(text)} chars): {url}")
                    # Truncate to save tokens
                    docs.append({"source": url, "content": text[:4000]})
                else:
                    print(f"   ⚠️ Content too short/empty: {url}")
                    
            except Exception as e:
                print(f"   ⚠️ Scrape error: {url}")
                continue

        # 3. RESULT
        # If we found at least 1 doc, we are successful
        confidence = 0.7 if len(docs) > 0 else 0.3
        
        if len(docs) == 0:
            print("❌ Critical: Could not scrape ANY documents.")
            
        return AgentResult(
            output=docs, 
            confidence=confidence, 
            should_continue=True,
            notes=f"Retrieved {len(docs)} docs"
        )