import requests
from bs4 import BeautifulSoup
from datetime import datetime
import sys
from ytmusicapi import YTMusic

def get_or_create_playlist(name, description=""):
    playlists = ytmusic.get_library_playlists()

    for pl in playlists:
        if pl['title'].lower() == name.lower():
            print(f"Playlist already exists: {pl['title']} (ID: {pl['playlistId']})")
            return pl['playlistId']
        
    playlist_id = ytmusic.create_playlist(name, description)
    print(f"New playlist created: {name} (ID: {playlist_id})")
    return playlist_id

now = datetime.now()

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36"
}

request = requests.get(url="https://en.wikipedia.org/wiki/Category:Lists_of_Billboard_Year-End_Hot_100_singles", headers=headers)
request.raise_for_status()

soup = BeautifulSoup(request.text, "html.parser")

messy_year_list = soup.select(selector=".mw-category-group ul > li > a")
year_list = [elem.get("title") for elem in messy_year_list]
first_year = int(year_list[0].split(" ")[-1])
last_year = int(year_list[-1].split(" ")[-1])

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
splitted_dates = date.split("-")

year = int(splitted_dates[0])
month = int(splitted_dates[1].lstrip("0"))
day = int(splitted_dates[2].lstrip("0"))

try:
    searched_date = datetime(year, month, day)
except:
    sys.exit("You've entered an invalid date to seach.")


if searched_date <= now and first_year <= year <= last_year:
    request = requests.get(url=f"https://en.wikipedia.org/wiki/Billboard_Year-End_Hot_100_singles_of_{year}", headers=headers)
    request.raise_for_status()

    soup = BeautifulSoup(request.text, "html.parser")

    rows = soup.select(selector="div > .wikitable > tbody > tr ")
    song_list = []
    for row in rows:
        cells = row.find_all("td")

        if len(cells) >= 2:
            song_list.append(cells[1].find("a").get_text())
    
    ytmusic = YTMusic("headers_auth.json")
    playlist_id = get_or_create_playlist(f"Top 100 of {year}", f"Created in Python using Wikipedia's 'Top 100 Songs of {year}' data.")
    for song in song_list:
        results = ytmusic.search(song, filter="songs")

        if not results:
            print(f"Song couldn't found: {song}")
            continue
        track_id = None
        for r in results:
            if r.get("resultType") == "song" and "videoId" in r:
                track_id = r["videoId"]
                break
        
        if track_id:
            try:
                ytmusic.add_playlist_items(playlist_id, [track_id])
                print(f"Added: {song}")
            except Exception as e:
                print(f"Error while adding: {song} -> {e}")
        else:
            print(f"No valid song ID found: {song}")

else:
    sys.exit("You've entered an invalid date to seach.")