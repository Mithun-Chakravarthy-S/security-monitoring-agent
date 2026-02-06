def compress_logs(logs):
    """
    Simulates ScaleDown compression by reducing log volume by 90%
    """
    if not logs:
        return []

    compressed_size = max(1, int(len(logs) * 0.1))
    return logs[:compressed_size]
