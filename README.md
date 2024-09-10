### Automated real-time temperature monitoring from the Bureau of Meteorology

# Pancake Parlour Live Temperature Tracker

### Monitor real-time weather data from the Australian Bureau of Meteorology (BoM) and retrieve the latest observations at Melbourne Airport. The script periodically checks for updates in temperature and other weather conditions, providing real-time monitoring with user-configurable intervals. This script was originally developed for Pancake Parlour's Winter Parlour, a promotion where pancakes were discounted to $5 if the air temperature dropped to 5°C or lower.

## Features
- Weather Data Retrieval: Fetches real-time weather data from the Bureau of Meteorology's JSON endpoint for Melbourne Airport.
- Dynamic User-Agent: Uses a random User-Agent for requests to avoid detection or rate-limiting from frequent requests.
- Temperature Monitoring: Monitors the air temperature and detects changes. Initially built to notify if the temperature falls to 5°C or below for Pancake Parlour's $5 pancake promotion.
- Customizable Check Interval: The delay between data checks is configurable via a config.ini file, allowing for flexible monitoring intervals.
- Future Social Media Integration: Placeholder for potential integration with social media platforms to post weather updates or promotional offers.

## Prerequisites
Before running the project, ensure you have the following installed:
- Python 3.x
- requests
- fake_useragent

## Installation
1. Clone the repository
```bash
git clone https://github.com/christiancheng15/Pancake-Parlour-Live-Temperature-Tracker.git
cd Pancake-Parlour-Live-Temperature-Tracker
```

2. Install the necessary prerequisites
```bash
pip install -r requirements.txt
```

## Usage

1. Configure delay setting in config.ini
```
[Monitor]
Delay = <DELAY>
```
Replace <DELAY> with number of seconds between checks.

2. Running the script
```bash
python main.py
```

## Output
```
{'sort_order': 0, 'wmo': 94866, 'name': 'Melbourne Airport', 'history_product': 'IDV60801', 'local_date_time': '10/04:30pm', 'local_date_time_full': '20240910163000', 'aifstime_utc': '20240910063000', 'lat': -37.7, 'lon': 144.8, 'apparent_t': 12.6, 'cloud': 'Mostly clear', 'cloud_base_m': 1200, 'cloud_oktas': 1, 'cloud_type': 'Cumulus', 'cloud_type_id': 8, 'delta_t': 5.2, 'gust_kmh': 35, 'gust_kt': 19, 'air_temp': 18.3, 'dewpt': 8.3, 'press': 1021.8, 'press_msl': 1021.8, 'press_qnh': 1021.7, 'press_tend': '-', 'rain_trace': '0.0', 'rel_hum': 52, 'sea_state': '-', 'swell_dir_worded': '-', 'swell_height': None, 'swell_period': None, 'vis_km': '10', 'weather': '-', 'wind_dir': 'NNE', 'wind_spd_kmh': 28, 'wind_spd_kt': 15}
```
The script will return a dict object representing the latest weather-related data at Melbourne Airport. A new dict object is returned only when the temperature has changed.

## Troubleshooting
- Scraping Issues: If the script fails to scrape the latest weather data, ensure that the headers are correct and that the Bureau of Meteorology's website structure has not changed.

## Contributing
Contributions are welcome! If you have ideas for new features or improvements, feel free to submit a pull request or open an issue.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Contact
For any questions or inquires, please contact [christiancheng15](https://github.com/christiancheng15/).