import string
from pytube import YouTube
import os
def main():
    
    while(True):
        try:
            URL= input("Enter the YT URL that you want to download: ")
            yt = YouTube(URL)
            # Created the save folder if not yet created 
            if not os.path.exists('/Users/zackaugustine/Documents/Youtube Downloads'):
                os.mkdir('/Users/zackaugustine/Documents/Youtube Downloads')

            print(yt.thumbnail_url)

            yd = yt.streams.get_highest_resolution()
            yd.download('/Users/zackaugustine/Documents/Youtube Downloads')
            break
        except Exception:
            print("Not a valid URL, try again.")
main()