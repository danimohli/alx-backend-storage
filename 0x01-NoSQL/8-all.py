#!/usr/bin/env python3
"""
Function to list all documents in a MongoDB collection.
"""


def list_all(mongo_collection):
    """
    List all documents in the specified MongoDB collection.

    Args:
        mongo_collection: The pymongo collection object.

    Returns:
        list: A list of documents in the collection.
        Returns an empty list if no documents are found.
    """
    return (list(mongo_collection.find())
            if mongo_collection.count_documents({}) > 0 else [])
