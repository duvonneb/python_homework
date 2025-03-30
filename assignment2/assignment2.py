import traceback
import csv

# Task 2
def read_employees():
    dict = {}
    rows = []
    # Read csv file to a dict
    try:
        with open(f'../csv/employees.csv', 'r') as file:
            reader = csv.reader(file)
            for i, row in enumerate(reader):
                # First row with fields tag
                if i == 0:
                    dict['fields'] = row
                else:
                    rows.append(row)
        # All other rows with rows tag
        dict['rows'] = rows
    # Catch exception if something fails
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")
    return dict
employees = read_employees()
print(employees)

# Task 3
# Find the index of the column header requested
def column_index(str):
    return employees["fields"].index(str)
employee_id_column = column_index("employee_id")

# Task 4
# Retrieve the value of first_name from a row 
def first_name(row_num):
    first_name_column = column_index("first_name")
    row = employees["rows"][row_num]
    return row[first_name_column]

# Task 5
def employee_find(employee_id):
    def employee_match(row):
        # Return the rows with the matching employee_id.
        return int(row[employee_id_column]) == employee_id
    # Filter out matching rows
    matches = list(filter(employee_match, employees["rows"]))
    return matches

# Task 6
def employee_find_2(employee_id):
    # Use lambda to do task 5
    matches = list(filter(lambda row : int(row[employee_id_column]) == employee_id , employees["rows"]))
    return matches

# Task 7
def sort_by_last_name():
     # Sort list by last name
     employees["rows"].sort(key=lambda row : row[column_index("last_name")])
     return employees["rows"]
sorted_list = sort_by_last_name()
print(sorted_list)

# Task 8
def employee_dict(row):
    new_dict = {}
    # Find corresponding row and assign to a new dict
    for i in range(len(employees["fields"])):
        new_dict[employees["fields"][i]] = row[i]
    # Remove employee id column
    del new_dict["employee_id"]
    return new_dict

# Task 9
def all_employees_dict():
    employees2 = read_employees()
    new_dict = {}
    # Create a dict of multiple dicts per employee row
    for i in range(len(employees2["rows"])):
        new_dict[i+1] = employee_dict(employees2["rows"][i])
    return new_dict
all_employees_list = all_employees_dict
print(all_employees_list)

# Task 10
import os
def get_this_value():
    return os.getenv(f"THISVALUE", "ABC") # Add default value

# Task 11
import custom_module
def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)
    print(custom_module.secret)

# Task 12
def read_minutes():
    # Function to read csv files into a dict
    def read_csv(fil):
        minutes = {}
        rows = []
        with open(f"../csv/{fil}.csv", 'r') as file:
            reader = csv.reader(file)
            for i, row in enumerate(reader):
                if i == 0:
                    minutes['fields'] = tuple(row)
                else:
                    rows.append(tuple(row))
        minutes['rows'] = rows
        return minutes
    # Set two new dict for each file
    minutes1 = read_csv("minutes1")
    minutes2 = read_csv("minutes2")
    return minutes1, minutes2
minutes1, minutes2 = read_minutes()
print(minutes1, minutes2)

# Task 13
def create_minutes_set():
    # Create sets from both minutes rows
    set1 = set(minutes1['rows'])
    set2 = set(minutes2['rows'])
    # Return the union
    return set1.union(set2)
minutes_set = create_minutes_set()
print(minutes_set)

# Task 14
from datetime import datetime
# Convert date and time strings into dates
def create_minutes_list():
    minutes_list = map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), minutes_set)
    return list(minutes_list)
minutes_list = create_minutes_list()
print(minutes_list)

# Task 15
def write_sorted_list():
    # Sort list by date and time
    minutes_list.sort(key=lambda x: x[1])
    # Convert dates back to strings
    new_minutes_list = list(map(lambda x: (x[0], datetime.strftime(x[1], "%B %d, %Y")), minutes_list))
    # Write list to a csv file
    with open('./minutes.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(minutes1['fields'])
        writer.writerows(new_minutes_list)
    return new_minutes_list
write_sorted_list()