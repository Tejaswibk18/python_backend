# 6.	API Rate Limiter
# Simulate API rate limiting.
# Rules:
# A user can make max 5 requests per minute.
# If exceeded → return "Rate limit exceeded".
# Input example:
# request_log = {
#     "user1": [timestamps]
#}




import time

RATE_LIMIT = 5
WINDOW = 60

request_log = {}


def rate_limiter(user):

    current_time = time.time()

    if user not in request_log:
        request_log[user] = []

    # Remove timestamps older than 60 seconds
    request_log[user] = [
        t for t in request_log[user] if current_time - t < WINDOW
    ]

    if len(request_log[user]) >= RATE_LIMIT:
        return {
            "status": "error",
            "message": "Rate limit exceeded"
        }

    request_log[user].append(current_time)

    return {
        "status": "success",
        "message": "Request allowed",
        "requests_in_current_window": len(request_log[user])
    }


user = input("Enter user id: ")

while True:

    input("\nPress ENTER to send request...")

    response = rate_limiter(user)

    print(response)