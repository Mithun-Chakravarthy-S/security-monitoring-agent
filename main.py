from agents.log_analyzer import analyze_logs
from agents.threat_detector import detect_threats
from agents.response_coordinator import respond
from scaledown.log_compressor import compress_logs
from dashboard.dashboard import show_dashboard

LOG_FILE = "logs/sample_logs.txt"

def main():
    suspicious_logs = analyze_logs(LOG_FILE)
    compressed_logs = compress_logs(suspicious_logs)
    threats = detect_threats(compressed_logs)
    responses = respond(threats)
    show_dashboard(threats, responses)

if __name__ == "__main__":
    main()
