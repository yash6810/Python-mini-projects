import requests as r
import bs4
from datetime import datetime
import schedule
import time
import random
import smtplib
from email.message import EmailMessage
import csv
import os
import config

def log_to_csv(pid, title, price):
    file_exists = os.path.isfile('price_history.csv')
    with open('price_history.csv', 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(['Timestamp', 'ProductID', 'Title', 'Price']) # Header
        
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        writer.writerow([timestamp, pid, title, price])

def send_notification(pid, product_title, new_price, product_url):
    sender_email = config.SENDER_EMAIL
    app_password = config.APP_PASSWORD
    reciver_email = config.RECEIVER_EMAIL

    subject = f"Price Drop Alert for {product_title}"
    body = f"The Price has dropped to {new_price}!\n\nBuy it here: {product_url}"

    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = reciver_email

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender_email, app_password)
            server.send_message(msg)
            print(f"--> Email Notification sent for {pid}!")
    except Exception as e:
        print(f"Error: Unable to send email. {e}")


base_url = "https://www.amazon.in/dp/"
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'TE': 'Trailers',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
}

def price_track():
    base_resopnse = r.get("https://www.amazon.in/", headers=headers)
    cookies = base_resopnse.cookies

    print(f"\n[{datetime.now()}] Checking Prices...")
    for pid, target_price in config.PRODUCTS.items():
        try:
            url = base_url+pid

            product_response = r.get(url, headers=headers, cookies=cookies)
            product_response.raise_for_status() # Raise an exception for HTTP errors (4xx or 5xx)

            soup = bs4.BeautifulSoup(product_response.text, features="lxml")

            product_title_element = soup.find(id="productTitle")
            product_title = product_title_element.get_text(strip=True) if product_title_element else "Title not found"

            price_lines = soup.find_all(class_="a-price-whole")
            if not price_lines:
                print(f"Could not find price for {pid} - {product_title}")
                log_to_csv(pid, product_title, "N/A - Price Not Found") 
                continue

            raw_price = price_lines[0].get_text(strip=True) 
            final_price = raw_price.replace(",", "").replace(".", "")
            price_value = int(final_price)
            
            log_to_csv(pid, product_title, price_value)

            print(f"Product '{product_title}' ({pid}): Current Price: {price_value}")

            if price_value < target_price:
                print(f"  -> PRICE DROP! It is below your target of {target_price}!")
                send_notification(pid, product_title, price_value, url)
        except r.exceptions.RequestException as req_err:
            print(f"Error fetching product {pid} ({url}): {req_err}")
            log_to_csv(pid, "Error - Network/HTTP", "N/A") # Log network error to CSV
        except Exception as e:
            print(f"An unexpected error occurred for product {pid} ({url}): {e}")
            log_to_csv(pid, "Error - Parsing/Other", "N/A") # Log other errors to CSV

schedule.every(5).minutes.do(price_track)

price_track()

while True:
    schedule.run_pending()
    time.sleep(random.randint(30, 60))
