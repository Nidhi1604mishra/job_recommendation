import requests
from db_config import jobs_collection

RAPIDAPI_KEY = "84b4693372mshf08a3030deb760ep12de71jsn285204b668c9"
RAPIDAPI_HOST = "active-jobs-db.p.rapidapi.com"

def fetch_and_store_jobs(title="Data Engineer", location="United States", limit=10):
    url = "https://active-jobs-db.p.rapidapi.com/active-ats-24h"

    headers = {
        "X-RapidAPI-Key": RAPIDAPI_KEY,
        "X-RapidAPI-Host": RAPIDAPI_HOST
    }

    params = {
        "limit": str(limit),
        "offset": "0",
        "title_filter": f'"{title}"',
        "location_filter": f'"{location}"',
        "description_type": "text"
    }

    response = requests.get(url, headers=headers, params=params)

    try:
        data = response.json()
        print(f"🔍 Raw API Response:\n{data}")
    except Exception as e:
        print("❌ Error parsing JSON:", e)
        print("📄 Raw response text:", response.text)
        return

    if not isinstance(data, list):
        print("⚠️ Unexpected response format. Expected a list.")
        return

    print(f"📦 Jobs fetched: {len(data)}")
    jobs_added = 0

    for job in data:
        print("📦 Raw job object:", job)
    
        title = job.get("title")
        if not title:
            print("⚠️ Title missing! Check structure:", job)
            title = "Unknown Title"
        
        company = job.get("organization", "Unknown Company")
        location_list = job.get("locations_derived", ["Remote"])
        location = location_list[0] if location_list else "Remote"
        description = job.get("description_text", "")

        job_entry = {
            "title": title,
            "company": company,
            "location": location,
            "description": description
        }

        try:
            jobs_collection.insert_one(job_entry)
            print(f"✅ Inserted: {title}")
            print("📊 Inserting into DB:", jobs_collection.full_name)

            jobs_added += 1
        except Exception as e:
            print(f"❌ Error inserting job: {e}")


if __name__ == "__main__":
    fetch_and_store_jobs(title="Data Scientist", location="United States", limit=10)
