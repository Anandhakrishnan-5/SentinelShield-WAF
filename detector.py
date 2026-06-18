import re


def detect_attack(data):

    rules = {
        "SQL Injection": {
            "pattern": r"(union.*select|or\s+1=1|drop\s+table)",
            "severity": "High"
        },

        "XSS": {
            "pattern": r"(<script|javascript:|onerror=)",
            "severity": "Medium"
        },

        "Directory Traversal": {
            "pattern": r"(\.\./|\.\.\\)",
            "severity": "Medium"
        },

        "Command Injection": {
            "pattern": r"(;|\||&&)\s*(ls|cat|whoami)",
            "severity": "High"
        },

        "Local File Inclusion": {
            "pattern": r"(/etc/passwd|boot.ini)",
            "severity": "High"
        }
    }

    for attack, details in rules.items():

        if re.search(
            details["pattern"],
            data,
            re.IGNORECASE
        ):
            return attack, details["severity"]

    return None, None
