import sqlite3

conn = sqlite3.connect(
    "alerts.db",
    check_same_thread=False
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS alerts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ip TEXT,
    attack TEXT,
    severity TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
""")

conn.commit()


def save_alert(ip, attack, severity):

    cursor.execute(
        """
        INSERT INTO alerts(ip, attack, severity)
        VALUES (?, ?, ?)
        """,
        (ip, attack, severity)
    )

    conn.commit()


def get_alerts():

    cursor.execute(
        "SELECT * FROM alerts ORDER BY id DESC"
    )

    return cursor.fetchall()
