from pymongo.mongo_client import MongoClient
from credentials import user, mongodb_password

# We will use MongoDB Atlas to host out database online.
URI = f"mongodb+srv://{user}:{mongodb_password}@onlinestore.1nli3cp.mongodb.net/?retryWrites=true&w=majority"


def connect_mongodb(uri=URI) -> MongoClient:
    """Connect to the mongoDB server."""
    # Create a new client and connect to the server
    client = MongoClient(uri)
    # Send a ping to confirm a successful connection
    while True:
        try:
            client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
            break
        except Exception as e:
            print(e)
    return client
