# 9.	Search API Logic
# Simulate a search endpoint.
# Data:
# benchmarks = [
#     {"name": "nginx", "category": "web"},
#     {"name": "redis", "category": "cache"},
#     {"name": "mysql", "category": "database"}
# ]
# Requirements:
# •	Search by name or category
# •	Case insensitive




benchmarks = [
    {"name": "nginx", "category": "web"},
    {"name": "redis", "category": "cache"},
    {"name": "mysql", "category": "database"}
]


def search_benchmarks(data, query):

    query = query.lower()
    results = []

    for item in data:

        if query in item["name"].lower() or query in item["category"].lower():
            results.append(item)

    if not results:
        return {
            "status": "error",
            "message": "No matching records found",
            "count": 0
        }

    return {
        "status": "success",
        "results": results,
        "count": len(results)
    }

query = input("Enter search term: ")

response = search_benchmarks(benchmarks, query)

print("\nSearch Results:")
print(response)