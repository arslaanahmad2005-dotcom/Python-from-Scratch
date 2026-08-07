# ==========================================================
# DAY 03 - PANDAS DATA CLEANING
# Mini Challenge Solution
# ==========================================================

# Step 1: Import Pandas
import pandas as pd

# ----------------------------------------------------------
# Step 2: Create the messy dataset
# ----------------------------------------------------------
data = {
    "Employee": [" Ram", "Shyam ", None, "Mohan", "Ram"],
    "Age": [25, None, 30, 28, 25],
    "Department": ["HR", "IT", "HR", None, "HR"],
    "Salary": ["40000", "50000", None, "45000", "40000"]
}

# Convert dictionary into DataFrame
df = pd.DataFrame(data)

# Display original dataset
print("========== Original Dataset ==========")
print(df)

# ----------------------------------------------------------
# Step 3: Check for missing values
# ----------------------------------------------------------

print("\n========== Missing Values ==========")
print(df.isnull())

# Count missing values in each column
print("\n========== Missing Value Count ==========")
print(df.isnull().sum())

# ----------------------------------------------------------
# Step 4: Fill missing values
# ----------------------------------------------------------

# Replace missing Employee names with 'Unknown'
df["Employee"] = df["Employee"].fillna("Unknown")

# Replace missing Age with the average age
average_age = df["Age"].mean()
df["Age"] = df["Age"].fillna(average_age)

# Replace missing Department with 'General'
df["Department"] = df["Department"].fillna("General")

# Replace missing Salary with '0'
df["Salary"] = df["Salary"].fillna("0")

# Display dataset after filling missing values
print("\n========== After Filling Missing Values ==========")
print(df)

# ----------------------------------------------------------
# Step 5: Remove duplicate rows
# ----------------------------------------------------------

# Remove duplicate records
df = df.drop_duplicates()

print("\n========== After Removing Duplicates ==========")
print(df)

# ----------------------------------------------------------
# Step 6: Change Data Types
# ----------------------------------------------------------

# Convert Salary column from string to integer
df["Salary"] = df["Salary"].astype(int)

# Convert Age column from float to integer
df["Age"] = df["Age"].astype(int)

# Display data types
print("\n========== Data Types ==========")
print(df.dtypes)

# ----------------------------------------------------------
# Step 7: String Operations
# ----------------------------------------------------------

# Remove extra spaces from Employee names
df["Employee"] = df["Employee"].str.strip()

# Convert Employee names into Title Case
df["Employee"] = df["Employee"].str.title()

# ----------------------------------------------------------
# Step 8: Create Tax Column
# ----------------------------------------------------------

# Calculate 10% tax of salary
df["Tax"] = df["Salary"] * 0.10

# ----------------------------------------------------------
# Step 9: Display Final Cleaned Dataset
# ----------------------------------------------------------

print("\n========== Final Cleaned Dataset ==========")
print(df)

# ----------------------------------------------------------
# Step 10: Display Additional Information
# ----------------------------------------------------------

print("\n========== Dataset Information ==========")
print(df.info())

print("\n========== Statistical Summary ==========")
print(df.describe())

print("\n========== Final Missing Values ==========")
print(df.isnull().sum())

print("\n========== Final Dataset Shape ==========")
print(df.shape)