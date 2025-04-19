from pymongo import MongoClient

# Connect to local MOngoDB
client = MongoClient("mongodb://localhost:27017/")

# Create or access the database
db = client["job_recommender"]

# Collections for jobs and users
jobs_collection = db["jobs"]
users_collection = db["users"]