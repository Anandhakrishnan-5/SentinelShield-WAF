# SentinelShield-WAF

## Advanced Intrusion Detection & Web Protection System

SentinelShield-WAF is a Python and Flask-based Web Application Firewall (WAF) simulation project designed to detect, log, and monitor common web application attacks. The system inspects incoming HTTP requests, identifies malicious payloads, generates alerts, stores attack information, and displays security events through a dashboard.

---

## Project Overview

This project was developed to demonstrate the core functionality of a Web Application Firewall and Intrusion Detection System.

The system performs:

- HTTP Request Inspection
- Attack Signature Detection
- Security Event Logging
- Alert Generation
- Dashboard Monitoring
- Rate Limiting and Abuse Detection

---

## Features

### Attack Detection
- SQL Injection Detection
- Cross-Site Scripting (XSS) Detection
- Directory Traversal Detection
- Command Injection Detection

### Security Monitoring
- Request Logging
- Severity Classification
- Attack Tracking
- Alert Management

### Protection Mechanisms
- Request Blocking
- Rate Limiting
- Suspicious Activity Monitoring

### Dashboard
- Total Attack Count
- Alert Records
- Severity Information
- Security Event Monitoring

---

## Technologies Used

- Python 3.11
- Flask
- SQLite
- HTML
- CSS
- Git
- GitHub

---

## Project Architecture

HTTP Request
↓
Request Inspection
↓
Attack Detection Engine
↓
Severity Classification
↓
Logging System
↓
SQLite Database
↓
Dashboard Visualization

---

## Project Structure

SentinelShield-WAF/

├── app.py

├── detector.py

├── logger_module.py

├── database.py

├── rate_limiter.py

├── templates/

│   └── dashboard.html

├── logs/

│   └── security.log

└── README.md

---

## Sample Attack Payloads

### SQL Injection

```
?id=or 1=1
```

### Cross-Site Scripting (XSS)

```
?q=<script>alert(1)</script>
```

### Directory Traversal

```
?page=../../etc/passwd
```

### Command Injection

```
?cmd=whoami
```

---

## Security Workflow

1. User sends an HTTP request.
2. The request is inspected by the detection engine.
3. Attack signatures are matched against predefined rules.
4. Malicious requests are classified by severity.
5. Security events are logged.
6. Alerts are stored in the SQLite database.
7. Dashboard displays attack information.

---

## Learning Outcomes

- Web Application Firewall Concepts
- Intrusion Detection Techniques
- HTTP Request Analysis
- Security Logging
- Rate Limiting
- Flask Application Development
- SQLite Database Integration
- Cybersecurity Monitoring

---

## Future Enhancements

- IP Blocking
- PDF Report Generation
- Graphical Attack Statistics
- User Authentication
- Email Alert Notifications
- Docker Deployment
- Cloud Hosting

---

## Author

**Anandhakrishnan T Pillai**

MSc Cyber Forensics & Cybersecurity

GitHub: https://github.com/Anandhakrishnan-5

---

## License

This project is developed for educational and cybersecurity learning purposes.
