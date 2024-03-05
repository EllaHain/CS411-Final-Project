from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
load_dotenv()
import os
password = os.getenv("PASS")
user = os.getenv("USER")




uri = f"mongodb+srv://{user}:{password}@cluster0.eg5wv2x.mongodb.net/test?retryWrites=true&w=majority&appName=Cluster&authSource=admin"


# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))


# Send a ping to confirm a successful connection
try:
   client.admin.command('ping')
   print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
   print(e)

