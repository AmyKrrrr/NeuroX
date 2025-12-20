from duckduckgo_search import DDGS

def search_web(query: str, max_results: int = 3) -> list[str]:
    urls = []
    with DDGS() as ddgs:
        for r in ddgs.text(query, max_results=max_results):
            urls.append(r["href"])
    return urls
