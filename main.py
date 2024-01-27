# importing packages
from pytube import YouTube
import os


def downloader(url):
    # url input from user
    yt = YouTube(url)

    # extract only audio
    video = yt.streams.filter(only_audio=True).first()

    # download the file
    out_file = video.download()

    # save the file
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)

    # result of success
    print(yt.title + " has been successfully downloaded.")


songlist = ["Levitating",
            "12 days of christmas",
            "let it go",
            "my little pony",
            "baby shark",
            "little einsteins"
            ]

urls = ["https://www.youtube.com/watch?v=hldMjKHGpag",
        "https://www.youtube.com/watch?v=oyEyMjdD2uk",
        "https://www.youtube.com/watch?v=ImKzSpGXqOE",
        "https://www.youtube.com/watch?v=QTNyyiKiZeU",
        "https://www.youtube.com/watch?v=pOznx1KLN7U",
        "https://www.youtube.com/watch?v=ImnTb9lH7WI"
        ]

# Variables we will change
youtube_name = []
url = ""

# ------------------YOU CODE HERE----------

# Step 1 ask the user to look up a song from song list
p = input("pick a song from the list: ")

# Step 2 to check if song in the list, if it is print out song has been found, if not print out the song is not found

# Step 3 If the song is found, check if the input is equal to one of the songs, then set the URL variable to be equal to the index of the song

if (p in songlist):
    print("found.")
    if (p == songlist[0]):
        url = urls[0]
        downloader(url)
    elif (p == songlist[1]):
        url = urls[1]
        downloader(url)
    elif (p == songlist[2]):
        url = urls[2]
        downloader(url)
    elif (p == songlist[3]):
        url = urls[3]
    elif (p == songlist[4]):
        url = urls[4]
        downloader(url)
    else:
        url = urls[5]
        downloader(url)

else:
    print("Get out!")
    print("The only available songs are: ")
    print(songlist)
    print("Your song has been added!")
    # HERE
    songlist.append(p)
    # HERE
    url = input("please type url here: ")
    downloader(url)
    print(songlist)










