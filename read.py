import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from pymongo import MongoClient

# MongoDB Setup
MONGO_URI = "mongodb+srv://amitsingh003official:E867cGvwI7iSOg4N@cluster0.1t8ki.mongodb.net/lms"
client = MongoClient(MONGO_URI)
db = client['lms']
collection = db['id_card_db']

# RFID Reader setup
reader = SimpleMFRC522()

try:
    print("Place your RFID card near the reader...")
    id, text = reader.read()
    print(f"Card read successfully! ID: {id}")

    # MongoDB Insert
    data = {
        "id": str(id),  
        "data": text
    }

    result = collection.insert_one(data)
    print("Data inserted into MongoDB. Document ID:", result.inserted_id)

except Exception as e:
    print("Error:", e)

finally:
    GPIO.cleanup()
