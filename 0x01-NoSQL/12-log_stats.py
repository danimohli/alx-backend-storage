#!/usr/bin/env python3
"""
This script provides statistics about Nginx logs stored in MongoDB.
It fetches data from the 'logs' database and 'nginx' collection.

It prints:
1. Total number of logs (documents) in the collection.
2. Method statistics for each HTTP method in ['GET', 'POST', 'PUT', 'PATCH', 'DELETE'].
3. Number of logs where the method is 'GET' and the path is '/status'.
"""
from pymongo import MongoClient


METHODS = ["GET", "POST", "PUT", "PATCH", "DELETE"]


def log_stats(mongo_collection, option=None):
    """
    Function that fetches and displays statistics about the logs
    in the given MongoDB collection.
    If an HTTP method is provided, it counts and prints the number of
    logs for that method.
    Otherwise, it counts all logs, prints method-based stats,
    and checks for '/status' path logs.

    :param mongo_collection: pymongo collection object
    :param method: Optional HTTP method to filter by
    """
    items = {}
    if option:
        value = mongo_collection.count_documents(
            {"method": {"$regex": option}})
        print(f"\tmethod {option}: {value}")
        return

    result = mongo_collection.count_documents(items)
    print(f"{result} logs")
    print("Methods:")
    for method in METHODS:
        log_stats(nginx_collection, method)
    status_check = mongo_collection.count_documents({"path": "/status"})
    print(f"{status_check} status check")


if __name__ == "__main__":
    nginx_collection = MongoClient('mongodb://127.0.0.1:27017').logs.nginx
    log_stats(nginx_collection)
