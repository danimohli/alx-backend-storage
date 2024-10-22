#!/usr/bin/env python3
"""
Function to insert a new document in a MongoDB collection.
"""

def insert_school(mongo_collection, **kwargs):
    """
    Insert a new document into the specified MongoDB collection.

    Args:
        mongo_collection: The pymongo collection object.
        **kwargs: Arbitrary keyword arguments representing
        the document fields.

    Returns:
        ObjectId: The _id of the newly inserted document.
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
