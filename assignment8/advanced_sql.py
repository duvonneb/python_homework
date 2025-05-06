import sqlite3

db_file = "../db/lesson.db"

def run_sql_statement(task):
    try:
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()
        #print("Connected to database.")

        cursor.execute(task)

        rows = cursor.fetchall()
        for row in rows:
            print(row)

    except sqlite3.Error as e:
        print("An error occurred:", e)

    finally:
        if conn:
            conn.close()
            #print("Database connection closed.")

# Task 1
print("Running Task 1.")
task_1 = """
        SELECT line_items.order_id, products.price * line_items.quantity AS total_cost
        FROM line_items
        JOIN orders ON line_items.order_id = orders.order_id
        JOIN products ON line_items.product_id = products.product_id
        ORDER BY line_items.order_id
        LIMIT 5;
        """
run_sql_statement(task_1)

# Task 2
print("Running Task 2.")
task_2 = """
        SELECT
            customers.customer_name,
            AVG(order_totals.total_price) AS average_total_price
        FROM
            customers
        LEFT JOIN (
            SELECT
                orders.customer_id AS customer_id_b,
                SUM(products.price * line_items.quantity) AS total_price
            FROM
                orders
            JOIN
                line_items ON orders.order_id = line_items.order_id
            JOIN 
                products ON line_items.product_id = products.product_id
            GROUP BY
                orders.order_id
        ) AS order_totals
        ON customers.customer_id = order_totals.customer_id_b
        GROUP BY
            customers.customer_id;
        """
run_sql_statement(task_2)

# Task 3
print("Running Task 3.")
try:
    conn = sqlite3.connect(db_file)
    conn.execute("PRAGMA foreign_keys = 1")
    cursor = conn.cursor()

    conn.execute("BEGIN")

    # Get customer ID
    cursor.execute("SELECT customer_id FROM customers WHERE customer_name = 'Perez and Sons'")
    customer_id = cursor.fetchone()[0]

    # Get employee ID of the employee creating order
    cursor.execute("SELECT employee_id FROM employees WHERE first_name = 'Miranda' AND last_name = 'Harris'")
    employee_id = cursor.fetchone()[0]

    # Get 5 least expensive products
    cursor.execute("SELECT product_id FROM products ORDER BY price ASC LIMIT 5")
    product_ids = [row[0] for row in cursor.fetchall()]

    # Insert new row
    cursor.execute("""
    INSERT INTO orders (customer_id, employee_id)
    VALUES (?, ?)
    RETURNING order_id
    """, (customer_id, employee_id))
    order_id = cursor.fetchone()[0]

    # Insert a new line for each product with order_id
    for product_id in product_ids:
        cursor.execute("""
            INSERT INTO line_items (order_id, product_id, quantity)
            VALUES (?, ?, ?)
        """, (order_id, product_id, 10))

    conn.commit()

    cursor.execute("""
    SELECT 
        line_items.line_item_id,
        line_items.quantity,
        products.product_name
    FROM 
        line_items
    JOIN 
        products ON line_items.product_id = products.product_id
    WHERE 
        line_items.order_id = ?
    """, (order_id,))

    for line_item_id, quantity, product_name in cursor.fetchall():
        print(line_item_id, quantity, product_name)

except sqlite3.Error as e:
    conn.rollback()
    print("Transaction failed:", e)
finally:
    conn.close()

# Task 4
print("Running Task 4.")
task_4 = """
        SELECT 
            employees.first_name, 
            employees.last_name, 
            COUNT(orders.order_id) AS count_of_orders
        FROM 
            employees
        JOIN orders ON employees.employee_id = orders.employee_id
        GROUP BY
            employees.employee_id
        HAVING
            COUNT(orders.order_id) > 5
        """
run_sql_statement(task_4)