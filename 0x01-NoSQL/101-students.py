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

    pipeline = [
        {
            "$project": {
                "name": 1,
                "averageScore": { "$avg": "$scores.score" }
            }
        },
        {
            "$sort": { "averageScore": -1 }
        }
    ]

    return list(mongo_collection.aggregate(pipeline))


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.my_database
    students_collection = db.students
    top_students_list = top_students(students_collection)

    for student in top_students_list:
        print(student)
