# 1.	 API Request Payload ValidatorProblem Idea:
# Write a function that validates an incoming API payload.
# Example payload:
# 	payload = {
#     		"name": "Nginx-Test",
#     		"environment": "dev",
#     		"sut": ["vm1", "vm2"],
#     		"run_parameters": {"users": 100, "duration": 60}
# }
# Requirements:
# •	Ensure all required keys exist.
# •	"sut" must be a non-empty list.
# •	"run_parameters" must contain only numeric values.
# •	Return "VALID" or raise an exception.


from pydantic import BaseModel, field_validator, ValidationError
from typing import List, Dict

class Payload(BaseModel):
    name: str
    environment: str
    sut: List[str]
    run_parameters: Dict[str, float]

    @field_validator("sut")
    def check_sut_not_empty(cls, value):
        if len(value) == 0:
            raise ValueError("sut must be a non-empty list")
        return value

def get_payload_input():
    name = input("Enter name: ")
    environment = input("Enter environment: ")

    sut_input = input("Enter SUT values (comma separated): ")
    sut = [i.strip() for i in sut_input.split(",") if i.strip()]    #convert str to list

    users = float(input("Enter users count: "))
    duration = float(input("Enter duration: "))

    payload = {
        "name": name,
        "environment": environment,
        "sut": sut,
        "run_parameters": {
            "users": users,
            "duration": duration
        }
    }

    return payload

def validate_request(payload):
    try:
        data = Payload(**payload)   #dict unpacking , convert dictionary into keyword arguments so the Pydantic model can read each field.

        return {
            "status": "success",
            "message": "Payload is valid",
            "data": data.model_dump()
        }

    except ValidationError as e:

        error_list = []

        for err in e.errors():
            error_list.append({
                "field": err["loc"][0],
                "error": err["msg"]
            })

        return {
            "status": "error",
            "errors": error_list
        }

payload = get_payload_input()

response = validate_request(payload)

print("\nAPI Response:")
print(response)