import pandas as pd
import matplotlib.pyplot as plt

# Read in the Netflix CSV as a DataFrame
netflix_df = pd.read_csv("netflix_data.csv")

# Subset the DataFrame for type "Movie"
netflix_subset = netflix_df[netflix_df["type"] == "Movie"]

# Select only the columns of interest
netflix_movies = netflix_subset[["title", "country", "genre", "release_year", "duration"]]

# Filter for durations shorter than 60 minutes
short_movies = netflix_movies[netflix_movies.duration < 60]
colors=[]
import matplotlib.pyplot as plt

# Create an empty list to store colors based on genre
colors = []

# Use a for loop to iterate over each row of the DataFrame
for index, row in netflix_movies.iterrows():
    genre = row['genre']
    
    # Conditions to assign colors based on genre
    if genre == "Children":
        colors.append('green')
    elif genre == "Documentaries":
        colors.append("orange")
    elif genre == "Stand-Up":
        colors.append('brown')
    else:
        colors.append("red")

fig = plt.figure()

# Use plt.scatter to create a scatter plot with colors based on genre
plt.scatter(netflix_movies['release_year'], netflix_movies['duration'], c=colors)

# Add labels and a title to the plot
plt.xlabel('Release year')
plt.ylabel('Duration (min)')
plt.title('Movie Duration by Year of Release')

# Display the plot
plt.show()

#"Are we certain that movies are getting shorter?
answer="maybe"
