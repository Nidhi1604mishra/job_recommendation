from db_config import jobs_collection
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from text_cleaner import clean_text

model = SentenceTransformer('all-MiniLM-L6-v2')

def recommend_jobs(resume_text, top_k=3):
    # Fetch jobs from MongoDB
    jobs = list(jobs_collection.find({}))
    
    # Clean descriptions
    for job in jobs:
        job["clean_description"] = clean_text(job.get("description", ""))

    job_texts = [job["clean_description"] for job in jobs]

    # # Vectorize
    # vectorizer = TfidfVectorizer()
    # job_vectors = vectorizer.fit_transform(job_texts)
    
    # # Clean and vectorize resume
    # cleaned_resume = clean_text(resume_text)
    # resume_vector = vectorizer.transform([cleaned_resume])
    
    
    # Get BERT embeddings 
    job_embeddings = model.encode(job_texts)
    resume_embedding = model.encode([clean_text(resume_text)])


    # Similarity
    similarity = cosine_similarity(resume_embedding, job_embeddings).flatten()
    top_indices = similarity.argsort()[::-1][:top_k]

    results = []
    for idx in top_indices:
        job = jobs[idx]
        score = round(similarity[idx]*100, 2)
        results.append(f"{job['title']} ({score}% match): {job['description']}")
    
    return "\n\n".join(results)
