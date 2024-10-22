#!/usr/bin/env python3
"""
Script to provide stats about Nginx logs stored in MongoDB.
"""

from pymongo import MongoClient


def log_stats():
    """
    Provide statistics about Nginx logs.
    """
    # Connect to MongoDB
    client = MongoClient()
    db = client.logs  # Access the 'logs' database
    collection = db.nginx  # Access the 'nginx' collection

    # Count total logs
    total_logs = collection.count_documents({})

    # Count logs by methods
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print(f"{total_logs} logs")
    print("Methods:")
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # Count logs with method GET and path /status
    status_check = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check} status check")


if __name__ == "__main__":
    log_stats()
