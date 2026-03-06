# 4.	Benchmark Result Aggregator
# Given benchmark results:
# results = [
#     {"sut": "vm1", "latency": 120},
#     {"sut": "vm2", "latency": 150},
#     {"sut": "vm1", "latency": 110},
# ]
# Write a function to calculate average latency per SUT.
# {
#  "vm1": 115,
#  "vm2": 150
# }




def aggregate_latency(results):

    latency_sum = {}
    count = {}

    for record in results:
        sut = record["sut"]
        latency = record["latency"]

        if sut not in latency_sum:
            latency_sum[sut] = 0
            count[sut] = 0

        latency_sum[sut] += latency
        count[sut] += 1

    averages = {}

    for sut in latency_sum:
        averages[sut] = latency_sum[sut] / count[sut]

    return {
        "status": "success",
        "data": averages
    }

n = int(input("Enter number of benchmark results: "))

results = []

for i in range(n):
    sut = input(f"Enter SUT for record {i+1}: ")
    latency = float(input(f"Enter latency for record {i+1}: "))

    results.append({
        "sut": sut,
        "latency": latency
    })

response = aggregate_latency(results)

print("\nAggregated Result:")
print(response)