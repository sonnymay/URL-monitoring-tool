import requests
import time

def check_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return True
    except requests.exceptions.RequestException:
        pass
    return False

def monitor_url(url, interval):
    while True:
        if check_url(url):
            print(f"{url} is accessible.")
        else:
            print(f"{url} is not accessible.")
            # Add your notification logic here (send an email, push notification, etc.)

        time.sleep(interval)

# Example usage
url_to_monitor = "https://example.com"
check_interval = 60  # seconds

monitor_url(url_to_monitor, check_interval)
