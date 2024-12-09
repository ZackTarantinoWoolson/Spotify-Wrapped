import json
import sys
import os
from collections import Counter, defaultdict
from datetime import datetime
from prettytable import PrettyTable

# Define the file path
file_path = "StreamingHistory_music_0.json"

# Read JSON data from the file
with open(os.path.join(os.path.dirname(sys.argv[0]), "StreamingHistory_music_0.json"), "r") as file:
    data = json.load(file)

# Parse the endTime field into datetime objects
for item in data:
    item["month"] = datetime.strptime(item["endTime"], "%Y-%m-%d %H:%M").strftime("%Y-%m")

# Count total number of tracks played per artist
artist_track_counts = Counter(item["artistName"] for item in data)

# Count occurrences of each track (artist and track combined)
track_artist_counts = Counter(
    f"{item['artistName']} - {item['trackName']}" for item in data
)

# Count artists per month
monthly_artist_counts = defaultdict(Counter)
for item in data:
    monthly_artist_counts[item["month"]][item["artistName"]] += 1

# Generate tables
artist_table = PrettyTable()
artist_table.field_names = ["Artist", "Total Tracks Played"]
for artist, count in artist_track_counts.most_common(10):
    artist_table.add_row([artist, count])

track_table = PrettyTable()
track_table.field_names = ["Artist - Track", "Play Count"]
for track_artist, count in track_artist_counts.most_common(10):
    track_table.add_row([track_artist, count])

monthly_table = PrettyTable()
monthly_table.field_names = ["Month", "Top 3 Artists"]
for month, counts in monthly_artist_counts.items():
    top_artists = counts.most_common(3)
    monthly_table.add_row(
        [month, ", ".join(f"{artist} ({count})" for artist, count in top_artists)]
    )

# Display the results
print("Top 10 Artists by Total Tracks Played:")
print(artist_table)
print("\nTop 10 Tracks by Play Count:")
print(track_table)
print("\nTop 3 Artists Per Month:")
print(monthly_table)