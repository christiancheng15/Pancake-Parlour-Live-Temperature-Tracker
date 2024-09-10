import requests
from fake_useragent import UserAgent
import time
import configparser

def get_weather_data():
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'en-SG,en-US;q=0.9,en;q=0.8',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Referer': 'http://www.bom.gov.au/products/IDV60801/IDV60801.94866.shtml',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': ua.random,
    }

    try:
        response = requests.get('http://www.bom.gov.au/fwo/IDV60801/IDV60801.94866.json', headers=headers)

        response.raise_for_status()

        data = response.json()
        latest_weather_data = data["observations"]["data"][0]

        return latest_weather_data

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
    except Exception as e:
        print(f"An error has occurred: {e}")

    return None

if __name__ == "__main__":

    config = configparser.ConfigParser()
    config.read("config.ini")

    ua = UserAgent()
    delay = int(config["Monitor"]["Delay"])
    last_temperature = None

    print(f"Bureau of Meteorology Monitor | Delay: {delay}")

    while True:
        latest_weather_data = get_weather_data()

        if not latest_weather_data:
            print("Failed to retrieve or process weather data.")
            continue

        if latest_weather_data["air_temp"] == last_temperature:
            print("No changes in temperature found.")
            continue

        print(latest_weather_data)

        # Add social media integration

        last_temperature = latest_weather_data["air_temp"]

        time.sleep(delay)