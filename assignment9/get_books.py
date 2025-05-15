import pandas as pd
import json

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Task 3

# Open the page
driver.get('https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart')

# Wait for content to load
sleep(2)

# Find all <li> elements with class 'cp-search-result-item'
items = driver.find_elements(By.CSS_SELECTOR, "li.cp-search-result-item")

# Empty list
results = []

# Loop through each result item
for item in items:
    try:
        # Title
        title_element = item.find_element(By.CLASS_NAME, "title-content")
        title = title_element.text

        # Authors (can be multiple)
        author_elements = item.find_elements(By.CLASS_NAME, "author-link")
        authors = "; ".join([author.text for author in author_elements])

        # Format-Year
        format_container = item.find_element(By.CLASS_NAME, "cp-format-info")
        format_year_element = format_container.find_element(By.TAG_NAME, "span")
        format_year = format_year_element.text

        # Build result dictionary
        result = {
            "Title": title,
            "Author": authors,
            "Format-Year": format_year
        }

        # Add to results list
        results.append(result)

    except Exception as e:
        print("Skipping because:", e)
        continue

# Close browser
driver.quit()

# Convert to DataFrame
df = pd.DataFrame(results)

# Print the DataFrame
print(df)

# Task 4

# Write to DataFrame
df.to_csv("assignment9/get_books.csv", index=False)

# Write to JSON
with open("assignment9/get_books.json", "w") as f:
    json.dump(results, f, indent=4)