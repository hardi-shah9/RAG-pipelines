from src.data_loader_file import load_all_documents
from src.vectorstore import FaissVectorStore
# from src.embedding import EmbeddingPipeline

if __name__ == "__main__":
    # docs = load_all_documents("data")
    # print(f"Loaded {len(docs)} documents.")
    # print(docs)
    # chunks = EmbeddingPipeline().chunk_documents(docs)
    # chunkvectors= EmbeddingPipeline().embed_chunks(chunks)
    store= FaissVectorStore("faiss_store")
    # store.build_from_documents(docs)
    # store.build_from_documents(docs)
    store.load()
    print(store.query("What is attention mechanism?", top_k=3))
    # print(chunkvectors)