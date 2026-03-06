# 3.	Pagination Logic
# Write a function that returns paginated results.
# Input:
# data = list(range(1,101))

# Example output:
# page=2, limit=10
# [11,12,13,14,15,16,17,18,19,20]




data = list(range(1, 101))

def paginate_data(data, page, limit):

    total_items = len(data)
    total_pages = (total_items + limit - 1) // limit

    if page < 1 or page > total_pages:
        return {
            "status": "error",
            "message": "Invalid page number"
        }

    start = (page - 1) * limit
    end = start + limit

    result = data[start:end]

    return {
        "status": "success",
        "page": page,
        "limit": limit,
        "total_items": total_items,
        "total_pages": total_pages,
        "data": result
    }

page = int(input("Enter page number: "))
limit = int(input("Enter limit per page: "))     #GET /users?page=2&limit=10

response = paginate_data(data, page, limit)

print("\nAPI Response:")
print(response)