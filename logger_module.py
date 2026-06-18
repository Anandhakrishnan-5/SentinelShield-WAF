import logging

logging.basicConfig(
    filename="logs/security.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)


def log_attack(ip, attack):
    logging.info(
        f"IP={ip} ATTACK={attack}"
    )
