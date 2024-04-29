import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Load the dataset
df = pd.read_csv("C:\\Users\\hp\\Downloads\\Movie Ratings.csv")
# Display basic information about the dataset
print(df.info())

# Display the first few rows of the dataset
print(df.head())
# Check for missing values
print(df.isnull().sum())

# Handle missing values (replace with the mean, median, or specific value)
df['Rating'].fillna(df['Rating'].mean(), inplace=True)

# Check for duplicates and drop them
df.drop_duplicates(inplace=True)
# Calculate basic statistics
rating_stats = df['Rating'].describe()

# Plot a histogram
plt.hist(df['Rating'], bins=10, edgecolor='black')
plt.title('Distribution of Movie Ratings')
plt.xlabel('Rating')
plt.ylabel('Number of Movies')
plt.show()
# Save the cleaned dataset to a new CSV file
df.to_csv("cleaned_movie_ratings.csv", index=False)
