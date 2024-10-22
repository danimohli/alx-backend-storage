#!/usr/bin/env python3
"""
Script to provide stats about Nginx logs stored in MongoDB.
"""

from pymongo import MongoClient

def nginx_stats():
    """
    Display statistics about Nginx logs stored in MongoDB.
    """
    # Connect to MongoDB
    client = MongoClient()
    db = client.logs  # Access the logs database
    collection = db.nginx  # Access the nginx collection

    # Count total logs
    total_logs = collection.count_documents({})

    # Count methods
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_counts = {method: collection.count_documents({"method": method}) for method in methods}

    # Count logs with method GET and path /status
    get_status_count = collection.count_documents({"method": "GET", "path": "/status"})

    # Display the statistics
    print(f"{total_logs} logs")
    print("Methods:")
    for method in methods:
        print(f"\t{method_counts[method]}")
    print(f"{get_status_count} logs where method=GET and path=/status")

if __name__ == "__main__":
    nginx_stats()
