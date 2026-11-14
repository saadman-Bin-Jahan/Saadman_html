


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("IMDB Dataset.csv")

print("Dataset imported successfully!")



print("\nFirst three rows:")
print(df.head(3))

print("\nLast three rows:")
print(df.tail(3))


print("\nDataset Information:")
df.info()


print("\nNull Values:")
print(df.isnull().sum())

print("\nTotal Null Values:")
print(df.isnull().sum().sum())



subset = df.iloc[40:75]

print("\nSubset of rows 41 to 75:")
print(subset)



highest_votes = df.loc[df['No_of_Votes'].idxmax()]

print("\nMovie with the Highest Number of Votes:")
print(highest_votes)



plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
sns.boxplot(y=df['IMDB_Rating'])
plt.title("Boxplot of IMDb Rating")

plt.subplot(1, 2, 2)
sns.boxplot(y=df['Runtime'])
plt.title("Boxplot of Runtime")

plt.tight_layout()
plt.show()



plt.figure(figsize=(8, 5))

plt.scatter(df['Runtime'], df['IMDB_Rating'])

plt.xlabel("Runtime (Minutes)")
plt.ylabel("IMDb Rating")
plt.title("Relationship between IMDb Rating and Runtime")

plt.show()




plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.hist(df['IMDB_Rating'], bins=10, edgecolor='black')
plt.xlabel("IMDb Rating")
plt.ylabel("Frequency")
plt.title("Distribution of IMDb Rating")

plt.subplot(1, 2, 2)
plt.hist(df['Runtime'], bins=10, edgecolor='black')
plt.xlabel("Runtime (Minutes)")
plt.ylabel("Frequency")
plt.title("Distribution of Runtime")

plt.tight_layout()
plt.show()




plt.figure(figsize=(10, 5))

sns.countplot(data=df, x='IMDB_Rating')

plt.xlabel("IMDb Rating")
plt.ylabel("Number of Movies")
plt.title("Number of Movies with Each IMDb Rating")

plt.show()


