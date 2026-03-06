1.	 API Request Payload ValidatorProblem Idea:
Write a function that validates an incoming API payload.
Example payload:
	payload = {
    		"name": "Nginx-Test",
    		"environment": "dev",
    		"sut": ["vm1", "vm2"],
    		"run_parameters": {"users": 100, "duration": 60}
}
Requirements:
•	Ensure all required keys exist.
•	"sut" must be a non-empty list.
•	"run_parameters" must contain only numeric values.
•	Return "VALID" or raise an exception.



2.	Execution Status Updater
Simulate an API that updates execution status.
Input:
executions = [
    {"id": 1, "status": "PENDING"},
    {"id": 2, "status": "RUNNING"},
    {"id": 3, "status": "COMPLETED"}
]
Write a function to update status

Rules:
•	Status flow must follow:
o	PENDING → RUNNING → COMPLETED
•	Invalid transitions should raise an error.

3.	Pagination Logic
Write a function that returns paginated results.
Input:
data = list(range(1,101))

Example output:
page=2, limit=10
[11,12,13,14,15,16,17,18,19,20]


4.	Benchmark Result Aggregator
Given benchmark results:
results = [
    {"sut": "vm1", "latency": 120},
    {"sut": "vm2", "latency": 150},
    {"sut": "vm1", "latency": 110},
]
Write a function to calculate average latency per SUT.
{
 "vm1": 115,
 "vm2": 150
}

5.	Unique Request ID Generator
Write a function to generate request IDs like:
REQ-20260305-0001
REQ-20260305-0002

Requirements:
•	Date-based prefix
•	Increment counter
•	Thread-safe logic (optional challenge)

6.	API Rate Limiter
Simulate API rate limiting.
Rules:
A user can make max 5 requests per minute.
If exceeded → return "Rate limit exceeded".
Input example:
request_log = {
    "user1": [timestamps]
}

7.	Workflow Stage Executor
Simulate a workflow execution system.
Example workflow:
workflow = [
    {"stage": "build", "status": "PENDING"},
    {"stage": "test", "status": "PENDING"},
    {"stage": "deploy", "status": "PENDING"}
]

Rules:
•	Stages must run sequentially.
•	Next stage runs only if previous completed.


8.	Data Deduplication Service
Given API response data:
records = [
    {"id": 1, "name": "test"},
    {"id": 2, "name": "demo"},
    {"id": 1, "name": "test"}
]

Write a function to remove duplicates based on id.
Expected:
[
 {"id":1,"name":"test"},
 {"id":2,"name":"demo"}
]

9.	Search API Logic
Simulate a search endpoint.
Data:
benchmarks = [
    {"name": "nginx", "category": "web"},
    {"name": "redis", "category": "cache"},
    {"name": "mysql", "category": "database"}
]
Requirements:
•	Search by name or category
•	Case insensitive

10.	Audit Log System
Write a simple audit logging system.
When an action happens:
Example log:
2026-03-05 12:10:20 | admin | CREATED_BENCHMARK

Requirements:
•	Store logs in a list
•	Allow retrieving logs by user.
