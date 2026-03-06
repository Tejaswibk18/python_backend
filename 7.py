# 7.	Workflow Stage Executor
# Simulate a workflow execution system.
# Example workflow:
# workflow = [
#     {"stage": "build", "status": "PENDING"},
#     {"stage": "test", "status": "PENDING"},
#     {"stage": "deploy", "status": "PENDING"}
# ]

# Rules:
# •	Stages must run sequentially.
# •	Next stage runs only if previous completed.




workflow = [
    {"stage": "build", "status": "PENDING"},
    {"stage": "test", "status": "PENDING"},
    {"stage": "deploy", "status": "PENDING"}
]

def execute_stage(workflow, stage_name):

    for i, stage in enumerate(workflow):

        if stage["stage"] == stage_name:

            # check previous stage
            if i > 0 and workflow[i-1]["status"] != "COMPLETED":
                return {
                    "status": "error",
                    "message": f"Previous stage '{workflow[i-1]['stage']}' not completed"
                }

            if stage["status"] == "COMPLETED":
                return {
                    "status": "error",
                    "message": "Stage already completed"
                }

            # run stage
            stage["status"] = "RUNNING"

            print(f"Running stage: {stage_name}")

            # simulate execution
            stage["status"] = "COMPLETED"

            return {
                "status": "success",
                "message": f"Stage '{stage_name}' completed",
                "workflow": workflow
            }

    return {
        "status": "error",
        "message": "Stage not found"
    }


while True:

    stage = input("\nEnter stage to execute (build/test/deploy) or 'exit': ")

    if stage == "exit":
        break

    response = execute_stage(workflow, stage)

    print(response)