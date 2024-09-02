# Import necessary libraries
import requests  # To handle HTTP requests for downloading the JSON files if they are from URLs
import json      # To handle JSON data parsing and saving

# Step 1: Define the URLs or local file paths for the JSON files
# Replace these with the actual URLs or local file paths for each JSON file.
files = [
    "./movies-2000s.json",  # JSON file for movies in the 2000s
    "./movies-2010s.json",  # JSON file for movies in the 2010s
    "./movies-2020s.json"   # JSON file for movies in the 2020s
]

# Initialize an empty list to store all movie data from all files
all_movies = []

# Step 2: Load and combine JSON data from all files
for file in files:
    try:
        # If using URLs, uncomment the line below to fetch the data
        # response = requests.get(file)
        # If using local files, comment out the line above and use the open method below

        # Open the file or handle the HTTP response
        with open(file, 'r') as f:
            data = json.load(f)  # Load the JSON data from the file or response

            # Combine the data into one list
            # Assuming the data from each file is a list of movie dictionaries
            all_movies.extend(data)  # Add the data to the all_movies list

    except Exception as e:
        # Print an error message if any file fails to load
        print(f"Failed to load data from {file}: {e}")

# Step 3: Inspect the combined data structure
print(all_movies[:2])  # Display the first two items to understand the structure

# Step 4: Filter, organize, or sort the combined data
# Example: Sorting all movies by their title or release year (replace 'key_name' with an actual key)
# Adjust the key_name based on your JSON structure, e.g., 'title' or 'release_year'
sorted_movies = sorted(all_movies, key=lambda x: x['key_name'])  # Change 'key_name' to the correct field

# Step 5: Display or save the processed data
# Print the sorted list of movies to verify the output
print(sorted_movies)

# Optional: Save the sorted or filtered data back to a JSON file
# This saves the combined and sorted movie data into a new file called 'sorted_movies.json'.
with open('sorted_movies.json', 'w') as file:
    json.dump(sorted_movies, file, indent=4)  # 'indent=4' makes the JSON output readable
