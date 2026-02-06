def analyze_logs(log_file):
    with open(log_file, "r") as file:
        logs = file.readlines()

    suspicious_logs = []

    for line in logs:
        if "WARNING" in line or "ERROR" in line:
            suspicious_logs.append(line.strip())

    return suspicious_logs
