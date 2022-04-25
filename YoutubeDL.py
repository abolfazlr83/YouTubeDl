from pytube import YouTube, Playlist, Search
from tqdm import tqdm

print('''\t\t\tHello ! im Abolfazl ♥
    \t\twelcome to youtube video downloader !''')
print("\t\t   Connect to \"vpn\" and continue↓")

n = 3
while(n > 0):
    try:
        print('''
        1.Download video
        2.Download playlist
        3.Extract the audio from video
        4.Search in youtube\n''')
        p = int(input("select ↑: "))
        if(p == 1):
            link = input("\n\nplease Enter the link → : ")  # get the link
            link.strip(" ")
            video = YouTube(link, on_progress_callback=True)
            stream = video.streams.get_highest_resolution()
            if(stream):
                print("Progressing...")
                try:
                    print("downloading started.../")
                    tqdm(stream.download(), desc="processing")
                    print("download successful")
                    break

                except(Exception) as error:
                    print(f"Error‼ --> {error}")
            else:
                print("error!")

        elif(p == 2):
            link = input("\n\nplease Enter the link → : ")  # get the link
            link.strip(" ")
            playlist = Playlist(link)
            print("Progressing...")
            try:
                for video in playlist.videos:
                    stream = video.streams.get_highest_resolution()
                    if(stream):
                        tqdm(stream.first().download(), desc="processing")
                    else:
                        print('Error!')
                        continue

            except(Exception) as error:
                print(f"Error‼ --> {error}")

        elif(p == 3):
            link = input("\n\nplease Enter the link → : ")  # get the link
            link.strip(" ")
            video = YouTube(link)
            stream = video.streams.filter(only_audio=True)
            print("Progressing...")
            if(stream):
                try:
                    print("downloading started.../")
                    tqdm(
                        stream.first().download(),
                        desc="processing",
                        unit="KB"
                    )
                    print("download successful!")

                except(Exception) as error:
                    print(f"Error‼ --> {error}")
            else:
                print("somthing went wrong try again!!")

        elif(p == 4):
            search = Search(
                input("\n\nplease Enter your subject → : ")
            )
            print("Progressing...")
            try:
                r = input(f"""there are '{len(search.results)}' results")
                        show them ? y/n --> """)
                if(r == "y" or r == "Y"):
                    print(f"results = \n {search.results}")
                    r = input("you wanna download one of them? y/n -> ")
                    if(r == "y" or r == "Y"):
                        video_id = input("Enter the video id: ")
                        video = YouTube(
                            "https://youtu.be/" + str(video_id).strip(" ")
                        )
                        stream = video.streams.get_highest_resolution()
                        print("Downloading started...")
                        if(stream):
                            try:
                                tqdm(
                                    stream.download(),
                                    desc="processing",
                                    unit="KB"
                                )
                                print("Download successfully ended !")

                            except(Exception) as error:
                                print(f"Error! -> {error}")
                        else:
                            print("somthing went wrong")

                    else:
                        print("ok")
                        continue

                else:
                    print("ok")
                    continue

            except(Exception) as e:
                print(f"Error‼ --> {e}")

        else:
            print('''please enter the video link again
                and select the option correctly''')
            continue
    except Exception as e:
        n -= 1
        if(n > 0):
            print(f"\nError‼ Enter again -> {e}")

    if(n == 0):
        print('''\nit's been three times..
            Close the program ،
            check the link ،
            then come back♥''')
