from src.data_loader_file import load_all_documents
from src.embedding import EmbeddingPipeline

if __name__ == "__main__":
    docs = load_all_documents("data")
    # print(f"Loaded {len(docs)} documents.")
    # print(docs)
    chunks = EmbeddingPipeline().chunk_documents(docs)
    chunkvectors= EmbeddingPipeline().embed_chunks(chunks)
    print(chunkvectors)