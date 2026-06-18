from flask import Flask, request, render_template
from detector import detect_attack
from logger_module import log_attack
from database import save_alert, get_alerts
from rate_limiter import is_rate_limited

app = Flask(__name__)


@app.route("/")
def inspect_request():

    payload = str(request.args)
    ip = request.remote_addr

    if is_rate_limited(ip):
        return "🚫 Rate Limit Exceeded"

    attack, severity = detect_attack(payload)

    if attack:

        print(
            f"[ALERT] {attack} | Severity: {severity}"
        )

        log_attack(ip, attack)

        save_alert(ip, attack, severity)

        return f"🚫 Blocked: {attack} ({severity})"

    return "✅ Request Allowed"


@app.route("/dashboard")
def dashboard():

    alerts = get_alerts()

    high_count = 0
    medium_count = 0

    attack_stats = {}

    for alert in alerts:

        attack_type = alert[2]

        if attack_type not in attack_stats:
            attack_stats[attack_type] = 0

        attack_stats[attack_type] += 1

        if alert[3] == "High":
            high_count += 1

        elif alert[3] == "Medium":
            medium_count += 1

    return render_template(
        "dashboard.html",
        alerts=alerts,
        total_attacks=len(alerts),
        high_count=high_count,
        medium_count=medium_count,
        attack_stats=attack_stats
    )


if __name__ == "__main__":
    app.run(debug=True)
