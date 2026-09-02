# ==========================================
# DAY 06 - PANDAS REVISION & MINI PROJECT
# SALES DATA ANALYSIS
# ==========================================

import pandas as pd


# ==========================================
# 1. LOAD DATASET
# ==========================================

df = pd.read_csv("sales.csv")

print("Dataset Loaded Successfully!")


# ==========================================
# 2. DATA EXPLORATION
# ==========================================

print("\n----- FIRST 5 ROWS -----")
print(df.head())

print("\n----- LAST 5 ROWS -----")
print(df.tail())

print("\n----- DATASET SHAPE -----")
print(df.shape)

print("\n----- COLUMN NAMES -----")
print(df.columns)

print("\n----- DATASET INFORMATION -----")
df.info()

print("\n----- STATISTICAL SUMMARY -----")
print(df.describe())


# ==========================================
# 3. CHECK MISSING VALUES
# ==========================================

print("\n----- MISSING VALUES -----")
print(df.isnull().sum())


# Remove rows containing missing values
df = df.dropna()

print("\nMissing values removed.")


# ==========================================
# 4. CHECK DUPLICATE VALUES
# ==========================================

print("\n----- DUPLICATE ROWS -----")
print(df.duplicated().sum())

# Remove duplicates
df = df.drop_duplicates()


# ==========================================
# 5. CREATE NEW COLUMN
# ==========================================

df["Revenue_Per_Unit"] = df["Sales"] / df["Quantity"]

print("\n----- DATA WITH NEW COLUMN -----")
print(df.head())


# ==========================================
# 6. DATA ANALYSIS & INSIGHTS
# ==========================================


# INSIGHT 1: TOTAL SALES

total_sales = df["Sales"].sum()

print("\n========== INSIGHT 1 ==========")
print("Total Sales:", total_sales)


# INSIGHT 2: AVERAGE SALES

average_sales = df["Sales"].mean()

print("\n========== INSIGHT 2 ==========")
print("Average Sales:", average_sales)


# INSIGHT 3: TOTAL PROFIT

total_profit = df["Profit"].sum()

print("\n========== INSIGHT 3 ==========")
print("Total Profit:", total_profit)


# INSIGHT 4: MOST SOLD PRODUCT

most_sold_product = (
    df.groupby("Product")["Quantity"]
    .sum()
    .sort_values(ascending=False)
)

print("\n========== INSIGHT 4 ==========")
print("Most Sold Product:")
print(most_sold_product.head(1))


# INSIGHT 5: PRODUCT WITH HIGHEST SALES

highest_sales_product = (
    df.groupby("Product")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\n========== INSIGHT 5 ==========")
print("Product With Highest Sales:")
print(highest_sales_product.head(1))


# INSIGHT 6: MOST PROFITABLE CATEGORY

profitable_category = (
    df.groupby("Category")["Profit"]
    .sum()
    .sort_values(ascending=False)
)

print("\n========== INSIGHT 6 ==========")
print("Profit By Category:")
print(profitable_category)


# INSIGHT 7: REGION WITH HIGHEST SALES

region_sales = (
    df.groupby("Region")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\n========== INSIGHT 7 ==========")
print("Sales By Region:")
print(region_sales)


# INSIGHT 8: AVERAGE PROFIT BY CATEGORY

average_profit_category = (
    df.groupby("Category")["Profit"]
    .mean()
    .sort_values(ascending=False)
)

print("\n========== INSIGHT 8 ==========")
print("Average Profit By Category:")
print(average_profit_category)


# INSIGHT 9: TOP 5 ORDERS BY SALES

top_5_orders = df.sort_values(
    "Sales",
    ascending=False
).head(5)

print("\n========== INSIGHT 9 ==========")
print("Top 5 Orders By Sales:")
print(top_5_orders)


# INSIGHT 10: TOTAL QUANTITY SOLD BY CATEGORY

quantity_by_category = (
    df.groupby("Category")["Quantity"]
    .sum()
    .sort_values(ascending=False)
)

print("\n========== INSIGHT 10 ==========")
print("Total Quantity Sold By Category:")
print(quantity_by_category)


# ==========================================
# 7. BONUS INSIGHTS
# ==========================================


# INSIGHT 11: MOST FREQUENT CATEGORY

print("\n========== INSIGHT 11 ==========")
print("Category Frequency:")
print(df["Category"].value_counts())


# INSIGHT 12: MAXIMUM AND MINIMUM SALE

print("\n========== INSIGHT 12 ==========")
print("Maximum Sale:", df["Sales"].max())
print("Minimum Sale:", df["Sales"].min())


# INSIGHT 13: SALES BY REGION AND CATEGORY

sales_region_category = (
    df.groupby(["Region", "Category"])["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\n========== INSIGHT 13 ==========")
print("Sales By Region And Category:")
print(sales_region_category)


# INSIGHT 14: HIGHEST PROFIT ORDER

highest_profit_order = df.loc[df["Profit"].idxmax()]

print("\n========== INSIGHT 14 ==========")
print("Highest Profit Order:")
print(highest_profit_order)


# ==========================================
# 8. FINAL OBSERVATIONS
# ==========================================

print("\n")
print("========================================")
print("       FINAL PROJECT OBSERVATIONS")
print("========================================")

print("1. Total Rows:", df.shape[0])
print("2. Total Columns:", df.shape[1])
print("3. Total Sales:", total_sales)
print("4. Average Sales:", average_sales)
print("5. Total Profit:", total_profit)

print(
    "6. Most Sold Product:",
    most_sold_product.idxmax()
)

print(
    "7. Product With Highest Sales:",
    highest_sales_product.idxmax()
)

print(
    "8. Most Profitable Category:",
    profitable_category.idxmax()
)

print(
    "9. Region With Highest Sales:",
    region_sales.idxmax()
)

print(
    "10. Highest Individual Sale:",
    df["Sales"].max()
)

print(
    "11. Total Quantity Sold:",
    df["Quantity"].sum()
)


# ==========================================
# PROJECT COMPLETED
# ==========================================

print("\nPandas Mini Project Completed Successfully!")