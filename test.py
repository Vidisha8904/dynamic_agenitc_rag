from db import get_chroma_client

client = get_chroma_client()

# List all collection names
collections = client.list_collections()
for collection in collections:
    print(f"Collection Name: {collection}")


client = get_chroma_client()
collection = client.get_collection(name="pydantic_ai_docs")

# Fetch stored data
results = collection.get()  # Retrieves all stored documents, IDs, metadata, and embeddings

# # Print data
# print("IDs:", results.get("ids", []))  # Document IDs
# print("Documents:", results.get("documents", []))  # Text documents
# print("Metadata:", results.get("metadatas", []))  # Metadata
# print("Embeddings:", results.get("embeddings", []))  # Embeddings (if stored)

# Print retrieved data
print(results) 
