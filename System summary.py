# Define functions
def check_status(status):
    if status == "running":
        return "OK"
    elif status == "starting":
        return "STARTING"
    elif status == "maintenance":
        return "-- MAINTENANCE"
    else:
        return "!! CHECK NEEDED"

def system_summary(system):
    sid   = system["sid"]
    stype = system["type"]
    flag  = check_status(system["status"])
    return f"{sid:<6} {stype:<14} {flag}"

# Data
systems = [
    {"sid": "PRD", "type": "Production",  "status": "running"},
    {"sid": "QAS", "type": "Quality",     "status": "stopped"},
    {"sid": "DEV", "type": "Development", "status": "maintenance"},
    {"sid": "DFD", "type": "Fiori Dev",   "status": "stopped"},
    {"sid": "PFP", "type": "Fiori PRD",   "status": "starting"},
]

# Run
print("=" * 50)
for s in systems:
    print(system_summary(s))
print("=" * 50)