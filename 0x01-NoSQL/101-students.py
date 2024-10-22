#!/usr/bin/env python3
"""
Function to return all students sorted by average score
"""
from pymongo import MongoClient


def top_students(mongo_collection):

    """
    Returns all students sorted by average score.
    Each item in the returned result will have the key 'averageScore'.

    :param mongo_collection: pymongo collection object
    :return: List of students sorted by their average score
    """
    top_student = mongo_collection.aggregate([
        {
            "$project": {
                "name": "$name",
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {"$sort": {"averageScore": -1}}
    ])

    return top_student
