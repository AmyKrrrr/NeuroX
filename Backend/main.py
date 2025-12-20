# app/main.py
from app.graph.workflow import build_workflow

if __name__ == "__main__":
    app = build_workflow()

    query = "is the government of india good or not"
    result = app.invoke({"query": query})

    print("\n===== FINAL OUTPUT =====\n")
    print(result.get("output"))
