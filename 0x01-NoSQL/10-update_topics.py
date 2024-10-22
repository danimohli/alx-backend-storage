#!/usr/bin/env python3
"""
Function to update the topics of a school document in a MongoDB collection.
"""


def update_topics(mongo_collection, name, topics):
    """
    Update the topics of a school document based on the school name.

    Args:
        mongo_collection: The pymongo collection object.
        name (str): The name of the school to update.
        topics (list): A list of topics to set for the school.

    Returns:
        UpdateResult: The result of the update operation.
    """
    result = mongo_collection.update_many(
        {"name": name},  # Filter by school name
        {"$set": {"topics": topics}}  # Update the topics field
    )
    return result
