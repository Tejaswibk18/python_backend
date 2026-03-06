# 8.	Data Deduplication Service
# Given API response data:
# records = [
#     {"id": 1, "name": "test"},
#     {"id": 2, "name": "demo"},
#     {"id": 1, "name": "test"}
# ]

# Write a function to remove duplicates based on id.
# Expected:
# [
#  {"id":1,"name":"test"},
#  {"id":2,"name":"demo"}
# ]



def remove_duplicates(records):

    seen_ids = set()
    unique_records = []

    for record in records:

        record_id = record["id"]

        if record_id not in seen_ids:
            seen_ids.add(record_id)
            unique_records.append(record)

    return {
        "status": "success",
        "data": unique_records
    }

n = int(input("Enter number of records: "))

records = []

for i in range(n):
    record_id = int(input(f"Enter id for record {i+1}: "))
    name = input(f"Enter name for record {i+1}: ")

    records.append({
        "id": record_id,
        "name": name
    })

response = remove_duplicates(records)

print("\nDeduplicated Data:")
print(response)