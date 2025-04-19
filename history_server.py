from db_config import users_collection
from datetime import datetime

def save_user_history(resume_text, recommendations):
    record = {
        "resume_text": resume_text,
        "recommendations": recommendations,
        "timestamp": datetime.now()
    }
    users_collection.insert_one(record)
    

def get_user_history(limit=5):
    # Get the last 'limit' uploads (most recent first) 
    records = users_collection.find().sort("timestamp", -1).limit(limit)
    
    history_texts = []
    for i, record in enumerate(records, 1):
        text = f"📄 **Resume {i}**\n🕒 {record['timestamp']}\n\n**Top Recommendations:**\n{record['recommendations']}"  
        history_texts.append(text)
        
    return "\n\n---\n\n".join(history_texts) if history_texts else "No past uploads found."      