def detect_threats(suspicious_logs):
    threats = []

    for log in suspicious_logs:
        if "Failed login" in log:
            threats.append({
                "type": "Brute Force Attack",
                "severity": "High",
                "log": log
            })

        elif "Suspicious IP" in log:
            threats.append({
                "type": "Unknown IP Activity",
                "severity": "Medium",
                "log": log
            })

    return threats
