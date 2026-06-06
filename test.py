from pymongo import MongoClient
import certifi

uri = "mongodb+srv://yash1423:irGikDBgmKUxTssu@cluster0.4xttowc.mongodb.net/?appName=Cluster0"

client = MongoClient(
    uri,
    tlsCAFile=certifi.where()
)

print(client.admin.command("ping"))