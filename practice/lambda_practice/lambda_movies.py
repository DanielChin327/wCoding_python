import requests  # Import requests for downloading JSON data if needed
import json      # Import json for parsing and saving JSON data

# Step 1: Define the URLs or local paths for the JSON files
# Replace these with actual URLs or local file paths for each decade's movies
files = [
    "./movies-2000s.json",  # Path or URL to the JSON file for movies from the 2000s
    "./movies-2010s.json",  # Path or URL to the JSON file for movies from the 2010s
    "./movies-2020s.json"   # Path or URL to the JSON file for movies from the 2020s
]

# Initialize an empty list to store all movies from the combined files
all_movies = []

# Step 2: Load and combine JSON data from all files
for file in files:
    try:
        # If the JSON file is available via URL, use requests to get the data
        # response = requests.get(file)  # Uncomment if using URLs
        # data = response.json()         # Parse JSON from the response if using URLs

        # If the JSON file is stored locally, open and read it
        with open(file, 'r') as f:
            data = json.load(f)  # Load the JSON data from the file

            # Combine data into the all_movies list
            # Assuming each JSON file contains a list of movie dictionaries
            all_movies.extend(data)  # Append data from each file to the all_movies list

    except Exception as e:
        # Print an error message if any file fails to load
        print(f"Failed to load data from {file}: {e}")

# Step 3: Inspect the combined data structure
print(all_movies[:2])  # Display the first two movie entries to check the data structure

# Step 4: Filter, organize, or sort the combined movie data
# Example: Sorting movies by title
sorted_movies = sorted(all_movies, key=lambda x: x['title'])  # Sort movies alphabetically by title

# Another example: Sorting movies by year in descending order
sorted_movies_by_year = sorted(all_movies, key=lambda x: x['year'], reverse=True)

# # Step 5: Display the sorted list of movies
# print("Sorted by title:", sorted_movies[:5])  # Display first 5 sorted movies by title
# print("Sorted by year:", sorted_movies_by_year[:5])  # Display first 5 sorted movies by year

# Optional: Save the sorted or filtered data back to a new JSON file
# Save sorted movies by title into 'sorted_movies.json'
with open('sorted_movies.json', 'w') as file:
    json.dump(sorted_movies, file, indent=4)  # 'indent=4' makes the JSON output readable

# Save sorted movies by year into 'sorted_movies_by_year.json'
with open('sorted_movies_by_year.json', 'w') as file:
    json.dump(sorted_movies_by_year, file, indent=4)  # 'indent=4' for readable formatting
