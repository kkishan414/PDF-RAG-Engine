# from src.data_loader import load_all_documents
# from src.embedding import EmbeddingPipeline
# from src.vectorstore import FaissVectorStore
from src.search import RAGSearch

## Example usage 

if __name__ == "__main__":
    #embedding_manager = EmbeddingPipeline()
    #docs = load_all_documents("data")
    #store = FaissVectorStore()
    #store.build_from_documents(docs)
    #store.load()
    ragsearch = RAGSearch()
    print(ragsearch.search_and_summarize("Kishan has how much hands on experience",top_k=3))
    #print(store.query("Kishan has how much hands on experience",top_k=3))

