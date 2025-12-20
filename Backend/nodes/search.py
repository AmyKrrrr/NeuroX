# app/nodes/search.py
from app.services.search_client import search_web
from duckduckgo_search.exceptions import DuckDuckGoSearchException

# 🔥 TEMPORARY fallback URLs (remove later)
FALLBACK_URLS = [
    "https://www.bbc.com/news/world-asia-india-68823827",
    "https://ecfr.eu/special/what_does_india_think/analysis/can_modi_deliver_good_governance",
]

def search_node(state: dict) -> dict:
    query = state.get("query")
    if not query:
        state["urls"] = []
        return state

    try:
        urls = search_web(query)

        # If DDG returns nothing (rare but possible)
        if not urls:
            print("⚠️ No search results. Using fallback URLs.")
            urls = FALLBACK_URLS

    except DuckDuckGoSearchException:
        print("⚠️ DuckDuckGo rate-limited. Using fallback URLs.")
        urls = FALLBACK_URLS

    state["urls"] = urls
    return state
