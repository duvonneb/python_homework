Lesson 14 - Web Scraping and Dashboard Project

This project has five parts:

1. Web Scraping
2. Data Cleaning & Transformation
3. Data Visualization
4. Dashboard / App Functionality
5. Code Quality & Documentation

---

## Summary

We scraped the "American League Team Review Hitting Statistics" leaderboard from 1901–1926. From each table, we extracted:

season_years: The year, teams, and page URL
season_events: The year and event name
season_statistics: The year, team, event and statistic values

---

## Setup Instructions

### 1. Clone and create a virtual environment

```bash
git clone <your-repo-url>
cd python_homework
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r assignment14/requirements.txt
```

### 3. Run the scraper

```bash
python assignment14/webscraping.py
```

- This will create 3 CSV files in `assignment14/season_data/`
  season_years.csv
  season_events.csv
  season_statistics.csv

### 4. Import CSVs into SQLite

```bash
python assignment14/database_import.py
```

- This creates `baseball_data.db` in the same folder.

### 5. Query via Command Line

```bash
python assignment14/database_query.py
```

- Choose between filtering by year, event, or joined data preview.

### 6. Launch Streamlit dashboard

```bash
streamlit run assignment14/dashboard.py
```

- Use sidebar filters to explore data and visualizations interactively.

---

## Screenshot

assignment14/Streamlit.pdf

---

## Final Deliverables

- `webscraping.py`
- `database_import.py`
- `baseball_data.db`
- `database_query.py`
- `dashboard.py`
- `season_data/*.csv`
- `README.md`
