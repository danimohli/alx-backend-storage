#!/usr/bin/env python3
"""
Function to return a list of schools with a specific topic in a
MongoDB collection.
"""


def schools_by_topic(mongo_collection, topic):
    """
    Retrieve a list of schools that have a specific topic.

    Args:
        mongo_collection: The pymongo collection object.
        topic (str): The topic to search for in the schools.

    Returns:
        list: A list of schools that have the specified topic.
    """
    return list(mongo_collection.find({"topics": topic}))
