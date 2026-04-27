import csv
from datetime import datetime

def check_status(status):
    if status == "running":
        return "OK"
    elif status == "maintenance":
        return "-- MAINTENANCE"
    elif status == "starting":
        return "-- STARTING"
    else:
        return "!! CHECK NEEDED"

def generate_report(input_file, output_file):
    results = []
    errors  = 0

    try:
        with open(input_file) as f:
            reader = csv.DictReader(f)
            for row in reader:
                flag = check_status(row["status"])
                if "CHECK" in flag:
                    errors += 1
                results.append(f"{row['sid']:<6} {row['type']:<14} {row['db']:<6} {row['os']:<8} {flag}")

    except FileNotFoundError:
        print(f"ERROR: {input_file} not found.")
        return

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

    with open(output_file, "w") as out:
        out.write(f"SAP System Report — {timestamp}\n")
        out.write("=" * 48 + "\n")
        out.write(f"{'SID':<6} {'Type':<14} {'DB':<6} {'OS':<8} Status\n")
        out.write("=" * 48 + "\n")
        for line in results:
            out.write(line + "\n")
        out.write("=" * 48 + "\n")
        out.write(f"Total systems: {len(results)}\n")
        out.write(f"Systems needing attention: {errors}\n")

    print(f"Report saved to {output_file}")
    print(f"Total: {len(results)} systems | Attention needed: {errors}")

# Run
generate_report("functions/systems.csv", "functions/report1.txt")