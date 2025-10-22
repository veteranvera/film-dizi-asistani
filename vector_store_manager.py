# vector_store_manager.py
# InMemoryDocumentStore kullanarak belgeleri yazan ve retriever oluşturan basit yönetici

from haystack.document_stores import InMemoryDocumentStore
from haystack.nodes import EmbeddingRetriever

def create_vector_store(docs, embedding_model):
    """Belge listesini alır, InMemoryDocumentStore'a yazar ve
    EmbeddingRetriever oluşturup döner."""
    # Document store (küçük projeler için uygun)
    document_store = InMemoryDocumentStore(use_bm25=True)
    # write_documents() çağrısı doc'ları kaydeder
    document_store.write_documents(docs)

    # Haystack EmbeddingRetriever - sentence-transformers formatı
    retriever = EmbeddingRetriever(
        document_store=document_store,
        embedding_model=embedding_model,
        model_format='sentence_transformers'
    )

    # Embedding'leri oluşturup doküman depolarına yazıyoruz
    document_store.update_embeddings(retriever)

    return document_store, retriever
