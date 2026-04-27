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

# Read + process
results = []

try:
    with open("functions/systems.csv") as f:
        reader = csv.DictReader(f)
        for row in reader:
            flag = check_status(row["status"])
            results.append(f"{row['sid']:<6} {row['type']:<14} {row['db']:<6} {row['os']:<8} {flag}")

except FileNotFoundError:
    print("ERROR: systems.csv not found. Check the file location.")
    exit()

# Write to file
with open("functions/report.txt", "w") as out:
    out.write("=" * 48 + "\n")
    out.write(f"{'SID':<6} {'Type':<14} {'DB':<6} {'OS':<8} Status\n")
    out.write("=" * 48 + "\n")
    for line in results:
        out.write(line + "\n")
    out.write("=" * 48 + "\n")

print("Done. Report saved to report.txt")