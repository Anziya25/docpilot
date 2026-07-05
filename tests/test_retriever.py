from app.services.retriever import RetrieverService

retriever = RetrieverService()

results = retriever.search(
    "What is multi-head attention?"
)

print("=" * 60)

print(f"Retrieved {len(results)} Results")

print("=" * 60)

for i, (doc, score) in enumerate(results, start=1):

    print(f"Result {i}")

    print("Score :", score)

    print("Metadata :", doc.metadata)

    print()

    print(doc.page_content[:500])

    print("=" * 60)