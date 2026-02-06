def respond(threats):
    responses = []

    for threat in threats:
        if threat["severity"] == "High":
            responses.append(
                f"ACTION: Block IP | Reason: {threat['type']}"
            )
        else:
            responses.append(
                f"ACTION: Alert SOC | Reason: {threat['type']}"
            )

    return responses
