#!/usr/bin/env python3
"""function that returns all students sorted by average score"""


def top_students(mongo_collection):
    """all students sorted by average score

    Args:
        mongo_collection (_type_): pymongo collection object

    Returns:
        _type_: all students values with type
    """
    return mongo_collection.aggregate(
        [
            {
                "$project":
                {
                    "name": "$name",
                    "averageScore": {"$avg": "$topics.score"}
                }
            },
            {
                "$sort":
                {
                    "averageScore": -1
                }
            },
        ])
