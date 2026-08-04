import pandas as pd
data={
    "Name":["Arslaan","Rahul","Aman"],
    "Age":[20,21,22],
    "City":["Lucknow","Delhi","Kanpur"]

}
df=pd.DataFrame(data)
print(df)
df2=pd.read_csv("netflix_titles.csv")
df2.head()
df2.tail()
df2.shape
df2.columns
df2.info()
df2.describe()
