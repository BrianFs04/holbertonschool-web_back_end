#!/usr/bin/env python3
""" log_stats module """
from pymongo import MongoClient
client = MongoClient()
collection = client.logs.nginx
logs = collection.count_documents({})
status = collection.count_documents({"method": "GET", "path": "/status"})

if __name__ == "__main__":

    print(f"{logs} logs")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    print(f"{status} status check")
