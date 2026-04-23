from analyzer import (
    total_time_per_user,
    most_active_users,
    unique_actions,
    total_activity_time
)


def main():
    logs = [
        {"user": "101", "action": "YouTube", "duration": 1.5},
        {"user": "102", "action": "Instagram", "duration": 2.0},
        {"user": "101", "action": "WhatsApp", "duration": 0.5},
        {"user": "103", "action": "YouTube", "duration": 3.0},
        {"user": "102", "action": "Netflix", "duration": 1.0},
    ]

    print("Total time per user:")
    print(total_time_per_user(logs))

    print("\nTop 2 most active users:")
    print(most_active_users(logs, 2))

    print("\nUnique actions:")
    print(unique_actions(logs))

    print("\nTotal activity time:")
    print(total_activity_time(logs))


if __name__ == "__main__":
    main()
