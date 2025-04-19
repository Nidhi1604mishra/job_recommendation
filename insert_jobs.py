from db_config import jobs_collection

# Clear old jobs
jobs_collection.delete_many({})

# Sample job documents
jobs = [
    {"title": "Data Scientist", "description": "Looking for Python, SQL, ML skills."},
    {"title": "Backend Developer", "description": "Experience with APIs, Python, and Databases."},
    {"title": "AI Engineer", "description": "Deep learning, NLP, and PyTorch experience required."}
]

# Insert into MongoDB
jobs_collection.insert_many(jobs)
print("Jobs inserted successfully!")
