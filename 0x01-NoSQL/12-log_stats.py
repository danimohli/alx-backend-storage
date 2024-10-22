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

HTTP_METHODS = ["GET", "POST", "PUT", "PATCH", "DELETE"]


def retrieve_log_stats(mongo_collection, method=None):
    """
    Function that fetches and displays statistics about
    the logs in the given MongoDB collection.
    If an HTTP method is provided, it counts and prints
    the number of logs for that method.
    Otherwise, it counts all logs, prints method-based stats,
    and checks for '/status' path logs.

    :param mongo_collection: pymongo collection object
    :param method: Optional HTTP method to filter by
    """
    if method:
        method_count = mongo_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {method_count}")
    else:
        total_logs = mongo_collection.count_documents({})
        print(f"{total_logs} logs")
        print("Methods:")
        for method in HTTP_METHODS:
            retrieve_log_stats(mongo_collection, method)

        status_logs = mongo_collection.count_documents({"method": "GET", "path": "/status"})
        print(f"{status_logs} status check")


if __name__ == "__main__":
    db_client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = db_client.logs.nginx
    retrieve_log_stats(nginx_collection)
