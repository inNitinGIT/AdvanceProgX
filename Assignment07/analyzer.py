from typing import List, Dict, Set
from collections import defaultdict
from functools import reduce
from operator import add


def total_time_per_user(logs: List[Dict[str, float]]) -> Dict[str, float]:
    """
    Returns total screen time per user.
    Uses defaultdict for efficient aggregation.
    """
    totals: Dict[str, float] = defaultdict(float)

    for record in logs:
        totals[record["user"]] += record.get("duration", 0.0)

    return dict(totals)


def most_active_users(logs: List[Dict[str, float]], k: int) -> List[str]:
    """
    Returns top k most active users sorted by total time (descending).
    Uses sorted() with key.
    """
    totals = total_time_per_user(logs)

    return [
        user
        for user, _ in sorted(
            totals.items(),
            key=lambda item: item[1],
            reverse=True
        )[:k]
    ]


def unique_actions(logs: List[Dict[str, float]]) -> Set[str]:
    """
    Returns a set of unique actions.
    Uses set comprehension.
    """
    return {record["action"] for record in logs}


def total_activity_time(logs: List[Dict[str, float]]) -> float:
    """
    Returns total activity time across all users.
    Uses reduce().
    """
    return reduce(
        add,
        (record.get("duration", 0.0) for record in logs),
        0.0
    )
