# ============================================================
# DAY 04 - PANDAS DATA MANIPULATION
# ============================================================
# Topics Covered:
# 1. Add columns
# 2. Update columns
# 3. Delete columns
# 4. Merge DataFrames
# 5. Join DataFrames
# 6. Concatenate DataFrames
# 7. GroupBy
# 8. Unique values
# 9. Value counts
# 10. Real-world sales dataset
# ============================================================


# ------------------------------------------------------------
# 1. IMPORT PANDAS
# ------------------------------------------------------------

import pandas as pd


# ============================================================
# PART A - ADD, UPDATE & DELETE COLUMNS
# ============================================================

# Create an employee DataFrame
employees = pd.DataFrame({
    "Employee_ID": [101, 102, 103, 104, 105],
    "Name": ["Arslaan", "Aman", "Sara", "Ali", "Riya"],
    "Department": ["IT", "HR", "IT", "Finance", "HR"],
    "Age": [20, 22, 21, 25, 23],
    "Salary": [50000, 45000, 60000, 55000, 48000]
})

print("\n========== ORIGINAL EMPLOYEE DATA ==========")
print(employees)


# ------------------------------------------------------------
# TASK 1: ADD A NEW COLUMN
# ------------------------------------------------------------

# Calculate 10% bonus based on salary
employees["Bonus"] = employees["Salary"] * 0.10

print("\n========== AFTER ADDING BONUS ==========")
print(employees)


# ------------------------------------------------------------
# TASK 2: ADD ANOTHER COLUMN
# ------------------------------------------------------------

# Add a Status column
employees["Status"] = "Active"

print("\n========== AFTER ADDING STATUS ==========")
print(employees)


# ------------------------------------------------------------
# TASK 3: UPDATE A COLUMN
# ------------------------------------------------------------

# Increase everyone's salary by 5%
employees["Salary"] = employees["Salary"] * 1.05

print("\n========== AFTER 5% SALARY INCREASE ==========")
print(employees)


# ------------------------------------------------------------
# TASK 4: UPDATE SPECIFIC ROWS
# ------------------------------------------------------------

# Increase salary of employees working in IT by another 10%
employees.loc[
    employees["Department"] == "IT",
    "Salary"
] *= 1.10

print("\n========== AFTER IT SALARY UPDATE ==========")
print(employees)


# ------------------------------------------------------------
# TASK 5: DELETE A COLUMN
# ------------------------------------------------------------

# Remove the Status column
employees = employees.drop("Status", axis=1)

print("\n========== AFTER DELETING STATUS ==========")
print(employees)


# ============================================================
# PART B - UNIQUE VALUES & VALUE COUNTS
# ============================================================

# ------------------------------------------------------------
# TASK 6: FIND UNIQUE DEPARTMENTS
# ------------------------------------------------------------

print("\n========== UNIQUE DEPARTMENTS ==========")
print(employees["Department"].unique())


# ------------------------------------------------------------
# TASK 7: COUNT UNIQUE DEPARTMENTS
# ------------------------------------------------------------

print("\n========== NUMBER OF UNIQUE DEPARTMENTS ==========")
print(employees["Department"].nunique())


# ------------------------------------------------------------
# TASK 8: COUNT EMPLOYEES IN EACH DEPARTMENT
# ------------------------------------------------------------

print("\n========== EMPLOYEES PER DEPARTMENT ==========")
print(employees["Department"].value_counts())


# ============================================================
# PART C - GROUPBY
# ============================================================

# ------------------------------------------------------------
# TASK 9: AVERAGE SALARY BY DEPARTMENT
# ------------------------------------------------------------

average_salary = employees.groupby("Department")["Salary"].mean()

print("\n========== AVERAGE SALARY BY DEPARTMENT ==========")
print(average_salary)


# ------------------------------------------------------------
# TASK 10: TOTAL SALARY BY DEPARTMENT
# ------------------------------------------------------------

total_salary = employees.groupby("Department")["Salary"].sum()

print("\n========== TOTAL SALARY BY DEPARTMENT ==========")
print(total_salary)


# ------------------------------------------------------------
# TASK 11: MULTIPLE GROUPBY OPERATIONS
# ------------------------------------------------------------

department_summary = employees.groupby("Department")["Salary"].agg(
    ["mean", "sum", "min", "max"]
)

print("\n========== DEPARTMENT SALARY SUMMARY ==========")
print(department_summary)


# ============================================================
# PART D - MERGE DATAFRAMES
# ============================================================

# Create first DataFrame
employee_info = pd.DataFrame({
    "Employee_ID": [101, 102, 103, 104],
    "Name": ["Arslaan", "Aman", "Sara", "Ali"]
})

# Create second DataFrame
department_info = pd.DataFrame({
    "Employee_ID": [101, 102, 103, 104],
    "Department": ["IT", "HR", "Finance", "IT"]
})

print("\n========== EMPLOYEE INFO ==========")
print(employee_info)

print("\n========== DEPARTMENT INFO ==========")
print(department_info)


# ------------------------------------------------------------
# TASK 12: MERGE TWO DATAFRAMES
# ------------------------------------------------------------

merged_data = pd.merge(
    employee_info,
    department_info,
    on="Employee_ID"
)

print("\n========== MERGED DATA ==========")
print(merged_data)


# ------------------------------------------------------------
# TASK 13: DIFFERENT TYPES OF MERGE
# ------------------------------------------------------------

# Inner Join
inner_merge = pd.merge(
    employee_info,
    department_info,
    on="Employee_ID",
    how="inner"
)

print("\n========== INNER MERGE ==========")
print(inner_merge)


# Left Join
left_merge = pd.merge(
    employee_info,
    department_info,
    on="Employee_ID",
    how="left"
)

print("\n========== LEFT MERGE ==========")
print(left_merge)


# Right Join
right_merge = pd.merge(
    employee_info,
    department_info,
    on="Employee_ID",
    how="right"
)

print("\n========== RIGHT MERGE ==========")
print(right_merge)


# Outer Join
outer_merge = pd.merge(
    employee_info,
    department_info,
    on="Employee_ID",
    how="outer"
)

print("\n========== OUTER MERGE ==========")
print(outer_merge)


# ============================================================
# PART E - JOIN DATAFRAMES
# ============================================================

# Create DataFrame with Employee_ID as index
employee_names = pd.DataFrame({
    "Name": ["Arslaan", "Aman", "Sara"]
}, index=[101, 102, 103])


# Create another DataFrame with same index
employee_salary = pd.DataFrame({
    "Salary": [50000, 45000, 60000]
}, index=[101, 102, 103])


# ------------------------------------------------------------
# TASK 14: JOIN TWO DATAFRAMES
# ------------------------------------------------------------

joined_data = employee_names.join(employee_salary)

print("\n========== JOINED DATA ==========")
print(joined_data)


# ============================================================
# PART F - CONCATENATE DATAFRAMES
# ============================================================

# Create first DataFrame
team_A = pd.DataFrame({
    "Name": ["Arslaan", "Aman"],
    "Age": [20, 22]
})


# Create second DataFrame
team_B = pd.DataFrame({
    "Name": ["Sara", "Ali"],
    "Age": [21, 25]
})


# ------------------------------------------------------------
# TASK 15: VERTICAL CONCATENATION
# ------------------------------------------------------------

combined_vertical = pd.concat(
    [team_A, team_B],
    ignore_index=True
)

print("\n========== VERTICAL CONCATENATION ==========")
print(combined_vertical)


# ------------------------------------------------------------
# TASK 16: HORIZONTAL CONCATENATION
# ------------------------------------------------------------

combined_horizontal = pd.concat(
    [team_A, team_B],
    axis=1
)

print("\n========== HORIZONTAL CONCATENATION ==========")
print(combined_horizontal)


# ============================================================
# PART G - REAL-WORLD SALES DATASET
# ============================================================

sales = pd.DataFrame({

    "Order_ID": [
        1001, 1002, 1003, 1004,
        1005, 1006, 1007, 1008
    ],

    "Product": [
        "Laptop",
        "Mouse",
        "Keyboard",
        "Laptop",
        "Monitor",
        "Mouse",
        "Keyboard",
        "Laptop"
    ],

    "Category": [
        "Electronics",
        "Accessories",
        "Accessories",
        "Electronics",
        "Electronics",
        "Accessories",
        "Accessories",
        "Electronics"
    ],

    "City": [
        "Lucknow",
        "Delhi",
        "Lucknow",
        "Mumbai",
        "Delhi",
        "Mumbai",
        "Lucknow",
        "Delhi"
    ],

    "Quantity": [
        2, 5, 3, 1,
        2, 8, 4, 1
    ],

    "Price": [
        60000,
        800,
        1500,
        60000,
        12000,
        800,
        1500,
        60000
    ]
})


print("\n\n================================================")
print("             REAL-WORLD SALES DATA")
print("================================================")

print(sales)


# ============================================================
# SALES ANALYSIS
# ============================================================

# ------------------------------------------------------------
# TASK 17: ADD TOTAL SALES COLUMN
# ------------------------------------------------------------

sales["Total_Sales"] = sales["Quantity"] * sales["Price"]

print("\n========== TOTAL SALES ==========")
print(sales)


# ------------------------------------------------------------
# TASK 18: FIND UNIQUE CITIES
# ------------------------------------------------------------

print("\n========== UNIQUE CITIES ==========")
print(sales["City"].unique())


# ------------------------------------------------------------
# TASK 19: COUNT ORDERS BY CITY
# ------------------------------------------------------------

print("\n========== ORDERS BY CITY ==========")
print(sales["City"].value_counts())


# ------------------------------------------------------------
# TASK 20: TOTAL SALES BY CITY
# ------------------------------------------------------------

city_sales = sales.groupby("City")["Total_Sales"].sum()

print("\n========== TOTAL SALES BY CITY ==========")
print(city_sales)


# ------------------------------------------------------------
# TASK 21: TOTAL QUANTITY SOLD BY PRODUCT
# ------------------------------------------------------------

product_quantity = sales.groupby("Product")["Quantity"].sum()

print("\n========== QUANTITY SOLD BY PRODUCT ==========")
print(product_quantity)


# ------------------------------------------------------------
# TASK 22: AVERAGE PRICE BY PRODUCT
# ------------------------------------------------------------

average_price = sales.groupby("Product")["Price"].mean()

print("\n========== AVERAGE PRICE BY PRODUCT ==========")
print(average_price)


# ------------------------------------------------------------
# TASK 23: BEST-SELLING PRODUCT
# ------------------------------------------------------------

best_selling = product_quantity.sort_values(
    ascending=False
)

print("\n========== PRODUCTS SORTED BY QUANTITY SOLD ==========")
print(best_selling)


# ------------------------------------------------------------
# TASK 24: TOTAL SALES BY CATEGORY
# ------------------------------------------------------------

category_sales = sales.groupby("Category")["Total_Sales"].sum()

print("\n========== TOTAL SALES BY CATEGORY ==========")
print(category_sales)


# ============================================================
# PART H - APPLY CUSTOM FUNCTION
# ============================================================

# ------------------------------------------------------------
# TASK 25: CREATE SALES LEVEL
# ------------------------------------------------------------

def sales_level(amount):
    """
    Categorize sales amount into
    High, Medium or Low.
    """

    if amount >= 50000:
        return "High"

    elif amount >= 10000:
        return "Medium"

    else:
        return "Low"


# Apply the custom function to Total_Sales
sales["Sales_Level"] = sales["Total_Sales"].apply(sales_level)


print("\n========== SALES LEVEL ==========")
print(sales)


# ============================================================
# PART I - DELETE COLUMN
# ============================================================

# ------------------------------------------------------------
# TASK 26: DELETE PRICE COLUMN
# ------------------------------------------------------------

# We already calculated Total_Sales,
# so Price is no longer required.
sales = sales.drop("Price", axis=1)

print("\n========== AFTER DELETING PRICE ==========")
print(sales)


# ============================================================
# FINAL DATASET
# ============================================================

print("\n\n================================================")
print("             FINAL CLEANED DATASET")
print("================================================")

print(sales)


# ============================================================
# FINAL SUMMARY
# ============================================================

print("\n========== FINAL DATASET SHAPE ==========")
print(sales.shape)

print("\n========== FINAL DATA TYPES ==========")
print(sales.dtypes)

print("\n========== FINAL DATASET INFORMATION ==========")
sales.info()