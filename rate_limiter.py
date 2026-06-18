import time

requests = {}

LIMIT = 20
WINDOW = 60


def is_rate_limited(ip):

    current_time = time.time()

    if ip not in requests:
        requests[ip] = []

    requests[ip].append(current_time)

    requests[ip] = [
        t for t in requests[ip]
        if current_time - t < WINDOW
    ]

    return len(requests[ip]) > LIMIT
