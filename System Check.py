systems = [
    {"sid": "PRD", "type": "Production",  "status": "running", "db": "ASE",  "os": "Linux"},
    {"sid": "QAS", "type": "Quality",     "status": "stopped", "db": "ASE",  "os": "Linux"},
    {"sid": "DEV", "type": "Development", "status": "running", "db": "HANA", "os": "Linux"},
    {"sid": "DFD", "type": "Fiori Dev",   "status": "stopped", "db": "ASE",  "os": "AIX"},
]

print("=" * 45)
print(f"{'SID':<6} {'Type':<14} {'DB':<6} {'OS':<8} Status")
print("=" * 45)

for s in systems:
    if s["status"] == "running":
        flag = "OK"
    else:
        flag = "!! CHECK"

    print(f"{s['sid']:<6} {s['type']:<14} {s['db']:<6} {s['os']:<8} {flag}")

print("=" * 45)