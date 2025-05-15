# Task 5
import pandas as pd

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get('https://owasp.org/www-project-top-ten/')

sleep(2)

# Get <a> tags for the top 10 vulnerabilities
all_links = driver.find_elements(By.XPATH, "/html/body/main/div/div[1]/section[1]/ul[2]/li/a")

top_10 = []

for link in all_links:
    href = link.get_attribute("href")
    title = link.text
    top_10.append({'title': title, 'link': href})

# Save to CSV
df = pd.DataFrame(top_10)
df.to_csv("assignment9/owasp_top_10.csv", index=False)

driver.quit()