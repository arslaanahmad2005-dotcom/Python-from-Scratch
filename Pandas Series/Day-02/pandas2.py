import pandas as pd

# ==========================
# Create DataFrame
# ==========================

data = {
    "Name": [
        "Arslaan", "Rahul", "Aman", "Sara", "Priya",
        "Rohan", "Anjali", "Karan", "Neha", "Vikas"
    ],
    "Age": [20, 19, 21, 22, 20, 23, 19, 21, 20, 22],
    "Marks": [90, 75, 88, 95, 82, 67, 91, 78, 85, 69],
    "City": [
        "Lucknow", "Delhi", "Kanpur", "Lucknow", "Delhi",
        "Kanpur", "Lucknow", "Delhi", "Lucknow", "Kanpur"
    ],
    "Department": [
        "CSE", "IT", "CSE", "ECE", "IT",
        "ME", "CSE", "IT", "ECE", "CSE"
    ]
}

df = pd.DataFrame(data)

print("========== Original Data ==========")
print(df)

# ==========================
# 1. Marks > 80
# ==========================
print("\n1. Students with Marks > 80")
print(df[df["Marks"] > 80])

# ==========================
# 2. Marks < 70
# ==========================
print("\n2. Students with Marks < 70")
print(df[df["Marks"] < 70])

# ==========================
# 3. Age >= 20
# ==========================
print("\n3. Students with Age >= 20")
print(df[df["Age"] >= 20])

# ==========================
# 4. City == Lucknow
# ==========================
print("\n4. Students from Lucknow")
print(df[df["City"] == "Lucknow"])

# ==========================
# 5. Department == CSE
# ==========================
print("\n5. Students from CSE Department")
print(df[df["Department"] == "CSE"])

# ==========================
# 6. Marks between 75 and 90
# ==========================
print("\n6. Marks between 75 and 90")
print(df[df["Marks"].between(75, 90)])

# ==========================
# 7. City is Delhi or Kanpur
# ==========================
print("\n7. Students from Delhi or Kanpur")
print(df[df["City"].isin(["Delhi", "Kanpur"])])

# ==========================
# 8. Age > 20 AND Marks > 85
# ==========================
print("\n8. Age > 20 AND Marks > 85")
print(df[(df["Age"] > 20) & (df["Marks"] > 85)])

# ==========================
# 9. Age == 19 OR Department == IT
# ==========================
print("\n9. Age == 19 OR Department == IT")
print(df[(df["Age"] == 19) | (df["Department"] == "IT")])

# ==========================
# 10. Students not from Delhi
# ==========================
print("\n10. Students not from Delhi")
print(df[df["City"] != "Delhi"])

# ==========================
# Sort by Marks (Ascending)
# ==========================
print("\nSorted by Marks (Ascending)")
print(df.sort_values(by="Marks"))

# ==========================
# Sort by Marks (Descending)
# ==========================
print("\nSorted by Marks (Descending)")
print(df.sort_values(by="Marks", ascending=False))

# ==========================
# Rename Marks to Score
# ==========================
df_renamed = df.rename(columns={"Marks": "Score"})

print("\nRenamed Column (Marks -> Score)")
print(df_renamed)

# ==========================
# First 5 Rows using loc[]
# ==========================
print("\nFirst 5 Rows using loc[]")
print(df.loc[0:4])

# ==========================
# First 5 Rows using iloc[]
# ==========================
print("\nFirst 5 Rows using iloc[]")
print(df.iloc[0:5])