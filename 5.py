# 5.	Unique Request ID Generator
# Write a function to generate request IDs like:
# REQ-20260305-0001
# REQ-20260305-0002

# Requirements:
# •	Date-based prefix
# •	Increment counter
# •	Thread-safe logic (optional challenge)





from datetime import datetime
from threading import Lock


class RequestIDGenerator:

    def __init__(self):
        self.counter = 0
        self.lock = Lock()

    def generate_id(self):

        with self.lock:   # thread-safe block

            self.counter += 1

            today = datetime.now().strftime("%Y%m%d")

            request_id = f"REQ-{today}-{self.counter:04d}"   #format no to 4 digits

            return {
                "status": "success",
                "request_id": request_id
            }


generator = RequestIDGenerator()

n = int(input("Enter number of request IDs to generate: "))

for i in range(n):
    response = generator.generate_id()
    print(response)