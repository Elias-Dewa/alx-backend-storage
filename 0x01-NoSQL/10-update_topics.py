#!/usr/bin/env python3
"""function that changes all topics of a school document based on the name"""


def update_topics(mongo_collection, name, topics):
    """Update all topics of a school document

    Args:
        mongo_collection (_type_): pymongo collection object
        name (str): the school name to update
        topics (list): the list of topics approached in the school

    Returns:
        _type_: values with the type
    """
    return mongo_collection.update_many({name: "name"},
                                        {"$set": {"topics": topics}})
