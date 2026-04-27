import csv

def check_status(status):
    if status == "running":
        return "OK"
    elif status == "maintenance":
        return "-- MAINTENANCE"
    elif status == "starting":
        return "-- STARTING"
    else:
        return "!! CHECK NEEDED"

print("=" * 48)
print(f"{'SID':<6} {'Type':<14} {'DB':<6} {'OS':<8} Status")
print("=" * 48)

with open("functions/systems.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        flag = check_status(row["status"])
        print(f"{row['sid']:<6} {row['type']:<14} {row['db']:<6} {row['os']:<8} {flag}")

print("=" * 48)