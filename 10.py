# 10.	Audit Log System
# Write a simple audit logging system.
# When an action happens:
# Example log:
# 2026-03-05 12:10:20 | admin | CREATED_BENCHMARK

# Requirements:
# •	Store logs in a list
# •	Allow retrieving logs by user.





from datetime import datetime

logs = []
def add_log(user, action):

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    log_entry = {
        "timestamp": timestamp,
        "user": user,
        "action": action
    }

    logs.append(log_entry)

    return {
        "status": "success",
        "message": "Log added"
    }

def get_logs_by_user(user):

    user_logs = []

    for log in logs:
        if log["user"] == user:
            user_logs.append(log)

    if not user_logs:
        return {
            "status": "error",
            "message": "No logs found for this user"
        }

    return {
        "status": "success",
        "logs": user_logs
    }


while True:

    print("\n1. Add Log")
    print("2. View Logs by User")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":

        user = input("Enter user: ")
        action = input("Enter action: ")

        response = add_log(user, action)

        print(response)

    elif choice == "2":

        user = input("Enter user to search logs: ")

        response = get_logs_by_user(user)

        print(response)

    elif choice == "3":
        break

    else:
        print("Invalid choice")