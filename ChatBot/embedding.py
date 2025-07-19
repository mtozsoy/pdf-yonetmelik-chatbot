from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

embedder = SentenceTransformer('all-MiniLM-L6-v2')

def create_faiss_index(chunks):
    embeddings = embedder.encode(chunks)
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(np.array(embeddings).astype('float32'))
    return index

def search_similar(question, index, chunks, top_k=5):
    q_emb = embedder.encode([question]).astype('float32')
    distances, indices = index.search(q_emb, top_k)
    return [chunks[i] for i in indices[0]]
