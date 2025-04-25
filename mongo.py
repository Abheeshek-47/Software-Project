from pymongo import MongoClient

# MongoDB connection URI
MONGO_URI = "mongodb+srv://amitsingh003official:E867cGvwI7iSOg4N@cluster0.1t8ki.mongodb.net/lms"

# Connect to MongoDB
client = MongoClient(MONGO_URI)

# Access the 'lms' database
db = client['lms']

# Access a collection (like a table) — create one if it doesn't exist
collection = db['card']

# Data to insert
data = {
    "sap": "1234",
    "data": {}
}

# Insert the data
result = collection.insert_one(data)

# Print inserted ID
print("Inserted document ID:", result.inserted_id)
