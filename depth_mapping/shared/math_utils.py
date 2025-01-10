from typing import Iterable


def average(collection: Iterable) -> float:
    """Get the average of a collection of numbers.

    Args:
        collection (Iterable): A collection of numbers.

    Returns:
        float: Arithmetic mean of the collection.
    """
    return sum(collection) / len(collection)
