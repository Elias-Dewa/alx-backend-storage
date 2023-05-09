#!/usr/bin/env python3
"""function that lists all documents in a collection"""


def list_all(mongo_collection):
    """list all documents in a collection

    Args:
        mongo_collection (_type_): pymongo collection object

    Returns:
        List: list of collections
    """
    return [mongo_collection.find()]
