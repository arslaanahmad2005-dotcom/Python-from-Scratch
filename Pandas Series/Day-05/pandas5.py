# ============================================================
# DAY 05 - ADVANCED PANDAS
# ============================================================
# Topics Covered:
# 1. Pivot Table
# 2. Crosstab
# 3. Multi-Index
# 4. Date & Time Operations
# 5. Rolling Window
# 6. Expanding Window
# 7. 5 Analysis-Based Questions
# ============================================================


# ------------------------------------------------------------
# 1. IMPORT LIBRARIES
# ------------------------------------------------------------

import pandas as pd


# ============================================================
# PART A - CREATE REAL-WORLD SALES DATASET
# ============================================================

data = {
    "Date": [
        "2026-01-05",
        "2026-01-10",
        "2026-01-15",
        "2026-02-03",
        "2026-02-10",
        "2026-02-18",
        "2026-03-02",
        "2026-03-12",
        "2026-03-20",
        "2026-04-05",
        "2026-04-15",
        "2026-04-25"
    ],

    "City": [
        "Lucknow",
        "Delhi",
        "Mumbai",
        "Lucknow",
        "Delhi",
        "Mumbai",
        "Lucknow",
        "Delhi",
        "Mumbai",
        "Lucknow",
        "Delhi",
        "Mumbai"
    ],

    "Category": [
        "Electronics",
        "Accessories",
        "Electronics",
        "Accessories",
        "Electronics",
        "Accessories",
        "Electronics",
        "Accessories",
        "Electronics",
        "Accessories",
        "Electronics",
        "Accessories"
    ],

    "Product": [
        "Laptop",
        "Mouse",
        "Mobile",
        "Keyboard",
        "Laptop",
        "Mouse",
        "Mobile",
        "Keyboard",
        "Laptop",
        "Mouse",
        "Mobile",
        "Keyboard"
    ],

    "Quantity": [
        2, 10, 3, 8,
        2, 12, 4, 7,
        3, 15, 5, 10
    ],

    "Sales": [
        120000, 8000, 60000, 12000,
        120000, 9600, 80000, 10500,
        180000, 12000, 100000, 15000
    ]
}

# Convert dictionary into DataFrame
df = pd.DataFrame(data)


# Display original dataset
print("\n================================================")
print("              ORIGINAL DATASET")
print("================================================")

print(df)


# ============================================================
# PART B - DATE & TIME OPERATIONS
# ============================================================

# ------------------------------------------------------------
# TASK 1: Convert Date column into datetime format
# ------------------------------------------------------------

df["Date"] = pd.to_datetime(df["Date"])

print("\n========== DATA TYPES ==========")
print(df.dtypes)


# ------------------------------------------------------------
# TASK 2: Extract Year
# ------------------------------------------------------------

df["Year"] = df["Date"].dt.year


# ------------------------------------------------------------
# TASK 3: Extract Month
# ------------------------------------------------------------

df["Month"] = df["Date"].dt.month


# ------------------------------------------------------------
# TASK 4: Extract Month Name
# ------------------------------------------------------------

df["Month_Name"] = df["Date"].dt.month_name()


# ------------------------------------------------------------
# TASK 5: Extract Day
# ------------------------------------------------------------

df["Day"] = df["Date"].dt.day


# ------------------------------------------------------------
# TASK 6: Extract Day Name
# ------------------------------------------------------------

df["Day_Name"] = df["Date"].dt.day_name()


print("\n========== DATE & TIME INFORMATION ==========")
print(df)


# ------------------------------------------------------------
# TASK 7: Filter data after a specific date
# ------------------------------------------------------------

filtered_data = df[df["Date"] >= "2026-03-01"]

print("\n========== SALES AFTER MARCH 1 ==========")
print(filtered_data)


# ============================================================
# PART C - PIVOT TABLE
# ============================================================

# ------------------------------------------------------------
# TASK 8: Basic Pivot Table
# ------------------------------------------------------------

# Find total sales for each city and category
pivot_table = pd.pivot_table(
    df,
    values="Sales",
    index="City",
    columns="Category",
    aggfunc="sum"
)

print("\n================================================")
print("              PIVOT TABLE")
print("================================================")

print(pivot_table)


# ------------------------------------------------------------
# TASK 9: Pivot Table with multiple calculations
# ------------------------------------------------------------

pivot_summary = pd.pivot_table(
    df,
    values="Sales",
    index="City",
    columns="Category",
    aggfunc=["sum", "mean"]
)

print("\n========== PIVOT TABLE - SUM & MEAN ==========")
print(pivot_summary)


# ------------------------------------------------------------
# TASK 10: Pivot Table by Product
# ------------------------------------------------------------

product_pivot = pd.pivot_table(
    df,
    values="Sales",
    index="Product",
    columns="City",
    aggfunc="sum",
    fill_value=0
)

print("\n========== PRODUCT-CITY PIVOT TABLE ==========")
print(product_pivot)


# ============================================================
# PART D - CROSSTAB
# ============================================================

# ------------------------------------------------------------
# TASK 11: Basic Crosstab
# ------------------------------------------------------------

# Count how many orders belong to each
# City and Category combination.

cross_table = pd.crosstab(
    df["City"],
    df["Category"]
)

print("\n================================================")
print("                 CROSSTAB")
print("================================================")

print(cross_table)


# ------------------------------------------------------------
# TASK 12: Crosstab with margins
# ------------------------------------------------------------

cross_table_margin = pd.crosstab(
    df["City"],
    df["Category"],
    margins=True
)

print("\n========== CROSSTAB WITH TOTAL ==========")
print(cross_table_margin)


# ------------------------------------------------------------
# TASK 13: Crosstab with values
# ------------------------------------------------------------

cross_sales = pd.crosstab(
    df["City"],
    df["Category"],
    values=df["Sales"],
    aggfunc="sum",
    margins=True
)

print("\n========== CROSSTAB - TOTAL SALES ==========")
print(cross_sales)


# ============================================================
# PART E - MULTI-INDEX
# ============================================================

# ------------------------------------------------------------
# TASK 14: Create Multi-Index DataFrame
# ------------------------------------------------------------

multi_index_df = df.set_index(
    ["City", "Category"]
)

print("\n================================================")
print("              MULTI-INDEX DATAFRAME")
print("================================================")

print(multi_index_df)


# ------------------------------------------------------------
# TASK 15: Access data using MultiIndex
# ------------------------------------------------------------

print("\n========== LUCKNOW DATA ==========")

print(
    multi_index_df.loc["Lucknow"]
)


# ------------------------------------------------------------
# TASK 16: Access specific City + Category
# ------------------------------------------------------------

print("\n========== LUCKNOW - ELECTRONICS ==========")

print(
    multi_index_df.loc[
        ("Lucknow", "Electronics")
    ]
)


# ------------------------------------------------------------
# TASK 17: Reset MultiIndex
# ------------------------------------------------------------

reset_df = multi_index_df.reset_index()

print("\n========== RESET INDEX ==========")
print(reset_df)


# ============================================================
# PART F - SORTING DATE DATA
# ============================================================

# ------------------------------------------------------------
# TASK 18: Sort by Date
# ------------------------------------------------------------

df = df.sort_values("Date")

print("\n========== DATA SORTED BY DATE ==========")
print(
    df[
        ["Date", "City", "Product", "Sales"]
    ]
)


# ============================================================
# PART G - ROLLING WINDOW
# ============================================================

# ------------------------------------------------------------
# TASK 19: Calculate 3-day rolling average
# ------------------------------------------------------------

df["Rolling_Average"] = (
    df["Sales"]
    .rolling(window=3)
    .mean()
)

print("\n================================================")
print("              ROLLING AVERAGE")
print("================================================")

print(
    df[
        ["Date", "Sales", "Rolling_Average"]
    ]
)


# ------------------------------------------------------------
# TASK 20: 3-period rolling sum
# ------------------------------------------------------------

df["Rolling_Sum"] = (
    df["Sales"]
    .rolling(window=3)
    .sum()
)

print("\n========== ROLLING SUM ==========")

print(
    df[
        ["Date", "Sales", "Rolling_Sum"]
    ]
)


# ============================================================
# PART H - EXPANDING WINDOW
# ============================================================

# ------------------------------------------------------------
# TASK 21: Calculate cumulative average
# ------------------------------------------------------------

df["Expanding_Average"] = (
    df["Sales"]
    .expanding()
    .mean()
)

print("\n================================================")
print("             EXPANDING AVERAGE")
print("================================================")

print(
    df[
        ["Date", "Sales", "Expanding_Average"]
    ]
)


# ------------------------------------------------------------
# TASK 22: Calculate cumulative sales
# ------------------------------------------------------------

df["Cumulative_Sales"] = (
    df["Sales"]
    .expanding()
    .sum()
)

print("\n========== CUMULATIVE SALES ==========")

print(
    df[
        ["Date", "Sales", "Cumulative_Sales"]
    ]
)


# ============================================================
# PART I - ANALYSIS QUESTIONS
# ============================================================

print("\n\n================================================")
print("          5 ANALYSIS QUESTIONS")
print("================================================")


# ------------------------------------------------------------
# QUESTION 1
# Which city generated the highest total sales?
# ------------------------------------------------------------

city_sales = (
    df.groupby("City")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\nQUESTION 1:")
print("Which city generated the highest total sales?")

print(city_sales)

highest_city = city_sales.idxmax()
highest_city_sales = city_sales.max()

print(
    f"\nAnswer: {highest_city} generated "
    f"the highest total sales of ₹{highest_city_sales:,.0f}"
)


# ------------------------------------------------------------
# QUESTION 2
# Which product sold the highest quantity?
# ------------------------------------------------------------

product_quantity = (
    df.groupby("Product")["Quantity"]
    .sum()
    .sort_values(ascending=False)
)

print("\nQUESTION 2:")
print("Which product sold the highest quantity?")

print(product_quantity)

best_product = product_quantity.idxmax()
best_quantity = product_quantity.max()

print(
    f"\nAnswer: {best_product} sold "
    f"the highest quantity: {best_quantity} units"
)


# ------------------------------------------------------------
# QUESTION 3
# Which category generated the highest revenue?
# ------------------------------------------------------------

category_sales = (
    df.groupby("Category")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\nQUESTION 3:")
print("Which category generated the highest revenue?")

print(category_sales)

best_category = category_sales.idxmax()
best_category_sales = category_sales.max()

print(
    f"\nAnswer: {best_category} generated "
    f"the highest revenue of ₹{best_category_sales:,.0f}"
)


# ------------------------------------------------------------
# QUESTION 4
# Which month had the highest sales?
# ------------------------------------------------------------

monthly_sales = (
    df.groupby("Month_Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\nQUESTION 4:")
print("Which month had the highest sales?")

print(monthly_sales)

best_month = monthly_sales.idxmax()
best_month_sales = monthly_sales.max()

print(
    f"\nAnswer: {best_month} had the "
    f"highest sales of ₹{best_month_sales:,.0f}"
)


# ------------------------------------------------------------
# QUESTION 5
# Which city-category combination generated
# the highest sales?
# ------------------------------------------------------------

city_category_sales = (
    df.groupby(
        ["City", "Category"]
    )["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\nQUESTION 5:")
print(
    "Which city-category combination "
    "generated the highest sales?"
)

print(city_category_sales)

best_combination = city_category_sales.idxmax()
best_combination_sales = city_category_sales.max()

print(
    f"\nAnswer: {best_combination[0]} + "
    f"{best_combination[1]} generated "
    f"₹{best_combination_sales:,.0f}"
)


# ============================================================
# FINAL DATASET
# ============================================================

print("\n\n================================================")
print("              FINAL DATASET")
print("================================================")

print(df)


# ============================================================
# FINAL SUMMARY
# ============================================================

print("\n================================================")
print("              DAY 05 COMPLETED")
print("================================================")

print("\nTopics Practiced:")
print("1. Pivot Table")
print("2. Crosstab")
print("3. Multi-Index")
print("4. Date & Time Operations")
print("5. Rolling Window")
print("6. Expanding Window")
print("7. GroupBy Analysis")
print("8. 5 Analysis-Based Questions")