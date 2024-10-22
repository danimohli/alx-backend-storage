#!/usr/bin/env python3
"""
Script to provide stats about Nginx logs stored in MongoDB.
"""
from pymongo import MongoClient


def nginx_stats():
    """
    Display statistics about Nginx logs stored in MongoDB.
    """
    client = MongoClient()
    db = client.logs
    colln = db.nginx

    total_logs = colln.count_documents({})

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    metd_c = {method: colln.count_documents({"method": method}) for method in methods}

    get_status_count = colln.count_documents({"method": "GET", "path": "/status"})

    print(f"{total_logs} logs")
    print("Methods:")
    for method in methods:
        print(f"\t{method_counts[method]}")
    print(f"{get_status_count} logs where method=GET and path=/status")


if __name__ == "__main__":
    nginx_stats()
