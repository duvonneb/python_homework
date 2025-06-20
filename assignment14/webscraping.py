from time import sleep
import csv
import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--disable-features=NetworkService")
chrome_options.add_argument("--remote-debugging-port=9222")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.set_page_load_timeout(30)

# Prepare output folder
os.makedirs("assignment14/season_data", exist_ok=True)

# Go to the main page
driver.get("https://www.baseball-almanac.com/yearmenu.shtml")
sleep(1)

# Get links for each year
year_links = driver.find_elements(By.XPATH, '//a[contains(@href, "yearly/yr")]')

seasons = []
for link in year_links:
    year = link.text.strip()
    url = link.get_attribute("href")
    if year.isdigit():
        if url.startswith("/"):
            url = "https://www.baseball-almanac.com" + url
        seasons.append((year, url))

# Data containers
season_years = []
season_events = []
season_statistics = []

year_id = 1
event_id = 1
stat_id = 1

# Loop through seasons
for year, url in seasons[:25]:
    try:
        driver.get(url)
        sleep(1)
        print(f"Scraping data for year {year}...")

        # Wait up to 10s for the correct table
        table = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//div[@class="ba-table"]/table[.//p[contains(text(), "Hitting Statistics")]]')
            )
        )

        raw_rows = table.find_elements(By.XPATH, './/tr[td[@class="datacolBlue"]]')
        rows = []
        teams_set = set()
        events_set = set()

        for tr in raw_rows:
            tds = tr.find_elements(By.TAG_NAME, "td")
            if len(tds) == 3:
                stat = tds[0].text.strip()
                team = tds[1].text.strip()
                value = tds[2].text.strip().replace(",", "")
                rows.append((stat, team, value))
                teams_set.add(team)
                events_set.add(stat)

        season_years.append({
            "YearID": year_id,
            "Year": year,
            "Teams": ", ".join(sorted(teams_set)),
            "URL": url
        })

        for stat_name in sorted(events_set):
            season_events.append({
                "EventID": event_id,
                "YearID": year_id,
                "Event": stat_name
            })
            event_id += 1

        for stat_name, team_name, value in rows:
            season_statistics.append({
                "StatID": stat_id,
                "YearID": year_id,
                "Team": team_name,
                "Event": stat_name,
                "Value": value
            })
            stat_id += 1

        year_id += 1

    except WebDriverException as e:
        print(f"Skipping year {year} due to WebDriver error: {e}")
    except Exception as e:
        print(f"Skipping year {year} due to unexpected error: {e}")

driver.quit()

# Save to CSV files
with open("assignment14/season_data/season_years.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["YearID", "Year", "Teams", "URL"])
    writer.writeheader()
    writer.writerows(season_years)

with open("assignment14/season_data/season_events.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["EventID", "YearID", "Event"])
    writer.writeheader()
    writer.writerows(season_events)

with open("assignment14/season_data/season_statistics.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["StatID", "YearID", "Team", "Event", "Value"])
    writer.writeheader()
    writer.writerows(season_statistics)

print("\nDone! Data saved to CSV files in 'season_data' folder.")