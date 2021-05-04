#!/usr/bin/env python3
""" log_stats module """
from pymongo import MongoClient

client = MongoClient()
collection = client.logs.nginx

if __name__ == "__main__":
    logs = collection.estimated_document_count()
    print(f"{logs} logs")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    status = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status} status check")

    print("IPs:")
    ips = collection.aggregate(
        [
            {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
            {"$project": {"ip": "$_id", "count": 1}},
            {"$sort": {"count": -1}},
            {"$limit": 10}
        ]
    )
    for ip in ips:
        print(f"\t{ip.get('ip')}: {ip.get('count')}")
