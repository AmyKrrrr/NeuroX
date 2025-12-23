import os

# --- 1. LITE RETRIEVAL AGENT (Scrapes LESS) ---
retrieval_agent_code = """import time
import requests
import trafilatura
from duckduckgo_search import DDGS
from app.agents.base import BaseAgent
from app.agents.result import AgentResult

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

class RetrievalAgent(BaseAgent):
    name = "retrieval_agent"

    async def run(self, query: str) -> AgentResult:
        print(f"🌍 Searching for: {query}")
        urls = []

        # 1. SEARCH (Limit to 5 results to save time)
        try:
            with DDGS() as ddgs:
                results = list(ddgs.text(query, max_results=5))
                if results:
                    urls = [r['href'] for r in results]
        except Exception as e:
            print(f"⚠️ Search failed: {e}")
            return AgentResult(output=[], confidence=0.0, should_continue=False)

        # 2. SCRAPE (ONLY 2 SITES) <--- THE FIX
        # Reducing this prevents Rate Limits
        print(f"🕷️ Scraping top 2 URLs...")
        docs = []
        
        count = 0
        for url in urls:
            if count >= 2: break # STOP after 2 good sites
            
            try:
                resp = requests.get(url, headers=HEADERS, timeout=5)
                if resp.status_code != 200: continue
                
                text = trafilatura.extract(resp.text)
                
                # Verify text length
                if text and len(text) > 500:
                    # TRUNCATE to 3000 chars (Save Tokens!)
                    docs.append({"source": url, "content": text[:3000]})
                    print(f"   ✅ Scraped (Lite): {url}")
                    count += 1
            except Exception:
                continue

        return AgentResult(output=docs, confidence=1.0 if docs else 0.0, should_continue=True)
"""

# --- 2. ROBUST LLM SERVICE (Groq) ---
llm_service_code = """import time
import os
from groq import Groq

# --- PASTE GROQ KEY HERE ---
API_KEY = "PASTE_YOUR_GROQ_API_KEY_HERE" 

client = None
try:
    if API_KEY and "PASTE" not in API_KEY:
        client = Groq(api_key=API_KEY)
except Exception:
    pass

def generate_text(prompt: str, model: str = 'llama3-70b-8192') -> str:
    if not client: return "Error: API Key missing in app/services/llm.py"

    # Retry 3 times
    for attempt in range(3):
        try:
            chat = client.chat.completions.create(
                messages=[{"role": "user", "content": prompt}],
                model=model,
            )
            return chat.choices[0].message.content

        except Exception as e:
            error_msg = str(e)
            if "429" in error_msg: # Rate Limit
                print(f"⚠️ Limit hit. Waiting 10s...")
                time.sleep(10)
            else:
                return f"Error: {e}"

    return "Server busy."
"""

# --- 3. SYNTHESIS AGENT (Safe Mode) ---
synthesis_agent_code = """from app.agents.base import BaseAgent
from app.agents.result import AgentResult
from app.services.llm import generate_text 

class SynthesisAgent(BaseAgent):
    name = "synthesis_agent"

    async def run(self, query: str, docs: list) -> AgentResult:
        if not docs:
            return AgentResult(output="No info found.", confidence=0.0, should_continue=False)

        print("🤖 Synthesizing (Lite Mode)...")

        # Combine docs (Limit total size to 6000 chars) <--- SAFETY LIMIT
        context = ""
        for d in docs:
            context += f"Source: {d['source']}\\n{d['content']}\\n"
        
        prompt = f"Question: {query}\\n\\nInfo:\\n{context[:6000]}\\n\\nAnswer briefly:"

        final_answer = generate_text(prompt)

        return AgentResult(output=final_answer, confidence=1.0, should_continue=False)
"""

def create_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✅ Updated: {path}")

if __name__ == "__main__":
    create_file("app/agents/retrieval_agent.py", retrieval_agent_code)
    create_file("app/services/llm.py", llm_service_code)
    create_file("app/agents/synthesis_agent.py", synthesis_agent_code)
    print("\\n🎉 DONE! Backend is now in 'Lite Mode'. Paste Groq Key & Restart.")
"""

### Step 2: Apply the Fix
1.  Run `python fix_lite.py`.
2.  Open **`app/services/llm.py`** and paste your Groq API Key.
3.  Restart your backend (`Ctrl+C` -> `uvicorn...`).

### Why this works:
* **Previous Payload:** ~20,000 characters (Hits limit instantly).
* **New Payload:** Max 6,000 characters (Fits easily in Free Tier).
* **Speed:** Scrapes only 2 sites, so it will be much faster.
"""