from app.core.rag import RAGPipeline

rag = RAGPipeline()

question = input("Ask a question: ")

result = rag.ask(question)

print("\n")
print("=" * 60)
print("ANSWER")
print("=" * 60)
print(result["answer"])

print("\n")
print("=" * 60)
print("SOURCES")
print("=" * 60)

for source in result["sources"]:
    print(source)