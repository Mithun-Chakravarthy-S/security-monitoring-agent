def show_dashboard(threats, responses):
    print("\n==============================")
    print("   SECURITY MONITORING DASHBOARD")
    print("==============================")

    print(f"\nThreats Detected: {len(threats)}\n")

    for idx, threat in enumerate(threats, start=1):
        print(f"{idx}. {threat['type']} | Severity: {threat['severity']}")

    print("\n--- Automated Responses ---")
    for response in responses:
        print(response)
