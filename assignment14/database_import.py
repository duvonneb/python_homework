import sqlite3
import csv
import os

# Set the folder where your CSV files are stored
csv_folder = "assignment14/season_data"

# Connect to SQLite
connection = sqlite3.connect("assignment14/baseball_data.db")
cursor = connection.cursor()

# Create tables
cursor.execute("""
CREATE TABLE IF NOT EXISTS season_years (
    YearID INTEGER,
    Year INTEGER,
    Teams TEXT,
    URL TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS season_events (
    EventID INTEGER,
    YearID INTEGER,
    Event TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS season_statistics (
    StatID INTEGER,
    YearID INTEGER,
    Team TEXT,
    Event TEXT,
    Value TEXT
)
""")

# Function to import a CSV file into a table
def import_csv(csv_filename, table_name):
    csv_path = os.path.join(csv_folder, csv_filename)

    try:
        with open(csv_path, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            headers = next(reader)  # Read the header row

            # Create a placeholder string like "?, ?, ?"
            placeholders = ", ".join(["?"] * len(headers))

            # Create SQL insert statement
            insert_sql = f"INSERT INTO {table_name} VALUES ({placeholders})"

            # Insert each row
            for row in reader:
                cursor.execute(insert_sql, row)

            connection.commit()

    except Exception as e:
        print(f"Error importing {csv_filename}: {e}")

# Import each CSV
import_csv("season_years.csv", "season_years")
import_csv("season_events.csv", "season_events")
import_csv("season_statistics.csv", "season_statistics")

# Close the connection to the database
connection.close()
print("\nAll CSV files have been imported into the SQLite database.")