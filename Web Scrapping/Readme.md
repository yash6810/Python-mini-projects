# Web Scraping Projects

This folder contains **Python-based web scraping scripts** built to extract, monitor, and log real-world data from live websites.

The focus here is on **practical scraping**, automation, scheduling, and data persistence — not demo or toy examples.

---

## 📌 Current Scripts

### 1️⃣ Amazon Price Tracker

A script that tracks product prices on Amazon India and notifies the user when prices fall below a predefined threshold.

**Core capabilities:**
- Scrapes product title and price
- Handles cookies and headers to reduce blocking
- Logs price history with timestamps
- Sends email alerts on price drops
- Runs automatically at fixed intervals

---

## 🛠️ Tech Stack Used

- **Python**
- `requests` – HTTP requests
- `BeautifulSoup (bs4)` – HTML parsing
- `schedule` – task automation
- `smtplib` & `email` – notifications
- `csv`, `datetime`, `os` – logging & utilities

---

## 📂 Folder Structure

web-scraping/

│

├── amazon_price_tracker.py

└── README.md


---

## ⚙️ Configuration Overview

Sensitive information (emails, passwords, product IDs) is **intentionally separated** into `config.py`.

This improves:
- Security
- Reusability
- Maintainability

---

## ▶️ Execution

Run any script directly:

```bash
python amazon_price_tracker.py
```

Scripts are designed to:

Run continuously

Handle network failures

Log every execution safely

⚠️ Important Notes

Website structures can change — selectors may need updates

Aggressive scraping may trigger blocking

Scripts are intended for learning and personal automation

🚧 Planned Additions

Multi-website scrapers (Flipkart, news sites, job portals)

Proxy rotation & user-agent randomization

Data storage using SQLite / PostgreSQL

Centralized logging system

🎯 Purpose of This Folder

This folder represents:

Hands-on scraping experience

Automation mindset

Real-world data collection workflows

It is meant to grow over time, not stay static.

