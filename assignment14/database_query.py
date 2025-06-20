import sqlite3

# Connect to the SQLite database
connection = sqlite3.connect("assignment14/baseball_data.db")
cursor = connection.cursor()

# Loop to allow multiple queries
while True:
    print("\nChoose an option:")
    print("1 - Filter by Year")
    print("2 - Filter by Event")
    print("3 - Show Joined Data (Year + Event + Team + Stat)")
    print("Type 'exit' to quit.")
    choice = input("Enter your choice (1/2/3): ").strip().lower()

    if choice == 'exit':
        print("Closing")
        break

    try:
        if choice == "1":
            year = input("Enter the year to filter by (ex. 1904): ").strip()
            cursor.execute("SELECT * FROM season_years WHERE Year = ?", (year,))
            results = cursor.fetchall()
            for row in results:
                print(row)

        elif choice == "2":
            keyword = input("Enter a keyword in the event name (ex. Home Runs): ").strip()
            cursor.execute("SELECT * FROM season_events WHERE Event LIKE ?", (f"%{keyword}%",))
            results = cursor.fetchall()
            for row in results:
                print(row)

        elif choice == "3":
            print("\nJoining data from all 3 tables...\n")
            cursor.execute("""
                SELECT sy.Year, ss.Team, ss.Event, ss.Value
                FROM season_statistics ss
                JOIN season_years sy ON ss.YearID = sy.YearID
            """)
            results = cursor.fetchall()
            for row in results:
                print(f"Year: {row[0]} | Team: {row[1]} | Event: {row[2]} | Value: {row[3]}")

        else:
            print("Invalid choice. Please select 1, 2, 3, or type 'exit'.")

    except Exception as e:
        print(f"Error during query: {e}")

# Close connection
connection.close()