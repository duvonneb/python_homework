import pandas as pd

# Task 1
# 1
data_1a = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
# Convert dict to a DataFrame
task1_data_frame = pd.DataFrame(data_1a)

# 2
task1_with_salary = task1_data_frame.copy()

# Add new column with values
task1_with_salary['Salary'] = [70000, 80000, 90000]

# 3
task1_older = task1_with_salary.copy()

# Increment Age column by 1
task1_older['Age'] = task1_older['Age'] + 1

# 4
task1_older.to_csv("employees.csv", index=False)

# Task 2
# 1
task2_employees = pd.read_csv('employees.csv')

# 2
json_employees = pd.read_json('additional_employees.json')

# 3
# Combine two DataFrames
more_employees = pd.concat([task2_employees, json_employees], ignore_index=True)

# Task 3
# 1
# Show first 3 rows of DataFrame
first_three = more_employees.head(3)

# 2
# Show last 2 rows of DataFrame
last_two = more_employees.tail(2)

# 3
employee_shape = more_employees.shape

# 4
print(more_employees.info())

# Task 4
# 1
dirty_data = pd.read_csv('dirty_data.csv')
clean_data = dirty_data.copy()

# 2
# Remove duplicates from DataFrame
clean_data = clean_data.drop_duplicates()

# 3
# Replace unknown str to N/A
clean_data['Age'] = clean_data['Age'].replace("unknown", pd.NA)
# Convert str to numeric
clean_data['Age'] = pd.to_numeric(clean_data['Age'], errors="coerce")

# 4
# Replace unknown str to N/A
clean_data['Salary'] = clean_data['Salary'].replace("unknown", pd.NA)
# Convert str to numeric
clean_data['Salary'] = pd.to_numeric(clean_data['Salary'], errors="coerce")

# 5
# Calculate mean of age column
mean_age = clean_data['Age'].mean()
# Fill missing age values with mean of age
clean_data['Age'] = clean_data['Age'].fillna(mean_age)

# Calculate median of salary column
median_salary = clean_data['Salary'].median()
# Fill missing salary values with median of salary
clean_data['Salary'] = clean_data['Salary'].fillna(median_salary)

# 6
# Convert str date to datetime
clean_data['Hire Date'] = pd.to_datetime(clean_data['Hire Date'], errors="coerce")

# 7
# Remove whitespace
clean_data['Name'] = clean_data['Name'].str.strip()
clean_data['Department'] = clean_data['Department'].str.strip()
# Convert all letters to uppercase
clean_data['Name'] = clean_data['Name'].str.upper()
clean_data['Department'] = clean_data['Department'].str.upper()
