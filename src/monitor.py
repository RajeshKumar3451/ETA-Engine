import json

log_file = "logs/app.log"

predictions = []
traffic_levels = []

with open(log_file, "r") as f:
    for line in f:
        entry = json.loads(line)
        predictions.append(entry["prediction"])
        traffic_levels.append(entry["input"][2])  # traffic

print("Total Predictions:", len(predictions))

if predictions:
    print("Average ETA:", round(sum(predictions)/len(predictions), 2))

if traffic_levels:
    print("Avg Traffic Level:", round(sum(traffic_levels)/len(traffic_levels), 2))