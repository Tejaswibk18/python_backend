# 2.	Execution Status Updater
# Simulate an API that updates execution status.
# Input:
# executions = [
#     {"id": 1, "status": "PENDING"},
#     {"id": 2, "status": "RUNNING"},
#     {"id": 3, "status": "COMPLETED"}
# ]
# Write a function to update status

# Rules:
# •	Status flow must follow:
# o	PENDING → RUNNING → COMPLETED
# •	Invalid transitions should raise an error.




STATUS_FLOW = {
    "PENDING": "RUNNING",
    "RUNNING": "COMPLETED"
}

executions = [
    {"id": 1, "status": "PENDING"},
    {"id": 2, "status": "RUNNING"},
    {"id": 3, "status": "COMPLETED"}
]

def update_execution_status(exec_list, exec_id, new_status):
    for execution in exec_list:
        if execution["id"] == exec_id:
            current_status = execution["status"]
            if current_status == "COMPLETED":
                return {
                    "status": "error",
                    "message": "Execution already completed. Cannot update."
                }
            allowed_next = STATUS_FLOW.get(current_status)

            if new_status != allowed_next:
                return {
                    "status": "error",
                    "message": f"Invalid transition: {current_status} -> {new_status}"
                }

            execution["status"] = new_status

            return {
                "status": "success",
                "message": "Execution status updated",
                "data": execution
            }

    return {
        "status": "error",
        "message": "Execution ID not found"
    }


exec_id = int(input("Enter execution ID: "))
new_status = input("Enter new status: ").upper()

response = update_execution_status(executions, exec_id, new_status)

print("\nAPI Response:")
print(response)