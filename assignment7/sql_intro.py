import sqlite3

def add_publisher(cursor, name):
    try:
        cursor.execute("SELECT publisher_id FROM publisher WHERE name = ?", (name,))
        if cursor.fetchone():
            print(f"Publisher '{name}' already exists.")
            return
        cursor.execute("INSERT INTO publisher (name) VALUES (?)", (name,))
    except sqlite3.IntegrityError:
        print(f"{name} is already in the database.")

def add_magazine(cursor, title, issue_date, publisher_name):
    try:
        # Get the publisher_id for the given publisher name
        cursor.execute("SELECT publisher_id FROM publisher WHERE name = ?", (publisher_name,))
        result = cursor.fetchone()

        if result is None:
            print(f"There was no publisher named {publisher_name}.")
            return

        publisher_id = result[0]

        cursor.execute("SELECT * FROM magazine WHERE title = ? AND issue_date = ? AND publisher_id = ?", (title, issue_date, publisher_id))
        if cursor.fetchone():
            print(f"Magazine '{title}' (issue: {issue_date}) by '{publisher_name}' already exists.")
            return

        # Insert the new magazine with all required fields
        cursor.execute("INSERT INTO magazine (title, issue_date, publisher_id) VALUES (?, ?, ?)", (title, issue_date, publisher_id))

    except sqlite3.IntegrityError:
        print(f"{title} is already in the database.")

def add_subscriber(cursor, name, address, magazine_title):
    try:
        cursor.execute("SELECT magazine_id FROM magazine WHERE title = ?", (magazine_title,))
        result = cursor.fetchone()
        if not result:
            print(f"No magazine found with title '{magazine_title}'.")
            return
        magazine_id = result[0]

        cursor.execute("SELECT * FROM subscriber WHERE name = ? AND address = ?", (name, address))
        if cursor.fetchone():
            print(f"Subscriber '{name}' at '{address}' already exists.")
            return

        cursor.execute("INSERT INTO subscriber (name, address, magazine_id) VALUES (?, ?, ?)", (name, address, magazine_id))

    except sqlite3.IntegrityError as e:
        print(f"Error adding subscriber '{name}': {e}")

def add_subscription(cursor, name, subscriber_name, subscriber_address, magazine_title):
    try:
        cursor.execute("SELECT subscriber_id FROM subscriber WHERE name = ? AND address = ?", (subscriber_name, subscriber_address))
        sub_result = cursor.fetchone()
        if not sub_result:
            print(f"No subscriber found with name '{subscriber_name}' at '{subscriber_address}'.")
            return
        subscriber_id = sub_result[0]

        cursor.execute("SELECT magazine_id FROM magazine WHERE title = ?", (magazine_title,))
        mag_result = cursor.fetchone()
        if not mag_result:
            print(f"No magazine found with title '{magazine_title}'.")
            return
        magazine_id = mag_result[0]

        cursor.execute("SELECT * FROM subscription WHERE subscriber_id = ? AND magazine_id = ?", (subscriber_id, magazine_id))
        if cursor.fetchone():
            print(f"Subscription for '{subscriber_name}' to '{magazine_title}' already exists.")
            return

        cursor.execute("INSERT INTO subscription (name, subscriber_id, magazine_id) VALUES (?, ?, ?)", (name, subscriber_id, magazine_id))

    except sqlite3.IntegrityError as e:
        print(f"Error adding subscription: {e}")

try:
    with sqlite3.connect("../db/magazines.db") as conn:
        #print("Database created and connected successfully.")
        conn.execute("PRAGMA foreign_keys = 1")
        cursor = conn.cursor()

        # Create tables
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS publisher (
            publisher_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS magazine (
            magazine_id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            issue_date TEXT,
            publisher_id INTEGER NOT NULL,
            FOREIGN KEY (publisher_id) REFERENCES publisher(publisher_id)
        )              
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS subscriber (
            subscriber_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            address TEXT NOT NULL,
            magazine_id INTEGER NOT NULL,
            FOREIGN KEY (magazine_id) REFERENCES magazine(magazine_id)
        )              
        """)

        # join table for subscribers and magazines
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS subscription (
            subscription_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            subscriber_id INTEGER NOT NULL,           
            magazine_id INTEGER NOT NULL,
            FOREIGN KEY (subscriber_id) REFERENCES subscriber(subscriber_id),
            FOREIGN KEY (magazine_id) REFERENCES magazine(magazine_id)
        )              
        """)

        # === Populate Tables with Sample Data ===

        # Publishers
        add_publisher(cursor, "New York Media")
        add_publisher(cursor, "Forbes Media")
        add_publisher(cursor, "Time USA, LLC")

        # Magazines
        add_magazine(cursor, "New York Magazine", "2024-01", "New York Media")
        add_magazine(cursor, "Forbes", "2024-02", "Forbes Media")
        add_magazine(cursor, "TIME", "2024-03", "Time USA, LLC")

        # Subscribers
        add_subscriber(cursor, "John Johnson", "123 Maple St", "New York Magazine")
        add_subscriber(cursor, "Sam Smith", "456 Oak Ave", "Forbes")
        add_subscriber(cursor, "John Johnson", "789 Pine Rd", "TIME")  # Same name, different address

        # Subscriptions
        add_subscription(cursor, "Monthly Time", "John Johnson", "123 Maple St", "TIME")
        add_subscription(cursor, "Geo Plan", "Sam Smith", "456 Oak Ave", "Forbes")
        add_subscription(cursor, "Fashion Forward", "John Johnson", "789 Pine Rd", "TIME")

        conn.commit()
        print("\nTables successfully populated with sample data.")

except sqlite3.Error as e:
    print("An error occurred:", e)

cursor.execute("SELECT * FROM subscriber")
rows = cursor.fetchall()
print('All information from the subscriber table:')
for row in rows:
    print(row)

cursor.execute("SELECT * FROM magazine ORDER BY title ASC;")
rows = cursor.fetchall()
print('All magazine sorted by name:')
for row in rows:
    print(row)

cursor.execute("""
            SELECT magazine.title
            FROM magazine
            JOIN publisher ON magazine.publisher_id = publisher.publisher_id
            WHERE publisher.name = 'Forbes Media';
            """)
rows = cursor.fetchall()
print('All magazines from Forbes:')
for row in rows:
    print(row)