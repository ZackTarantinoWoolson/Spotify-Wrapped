## Install Python
Download Python here: https://www.python.org/downloads/
And make sure to install the prettytables package. https://pypi.org/project/prettytable/
```
pip install prettytable
```

## Clone this repo
Instructions for clonning the repo are here: https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository
Or you can download the Zip data manually. 

## Downloading Spotify data
Access your Spotify account via a Desktop (non-mobile device) and go to your Account Privacy settings ()

On that page, there will be an option to send an email to "Download your Data". It may take a few days to get that data. 

Once you receive your data, unzip the "my_spotify_data" folder and open the "Spotify Account Data" folder. Copy the "StreamingHistory_music_0.json" file into the "PutDataHere" folder. 

From there, run the script and see the table output in your terminal. 

## Usage
Currently, this script will show the Top 10 Tracks and Artists by number of plays and the Top 3 Artists per month.