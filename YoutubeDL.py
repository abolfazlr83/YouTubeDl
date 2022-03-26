from pytube import YouTube

print('''\t\t\tHello ! im Abolfazl ♥
    \t\twelcom to youtube video downloder !''')
print("\t\t   Connect to \"vpn\" and continue↓")
n = 3
while(n > 0):
    link = input("\n\nplease Enter the link → : ")  # get the link
    link.strip(" ")
    try:
        video = YouTube(link)
        print('''
        1.Download the video
        2.Extract the audio from video\n''')
        p = int(input("select ↑: "))
        if(p == 1):
            print("Progressing...")
            stream = video.streams.get_highest_resolution()
            if(stream):
                try:
                    print("downloading started.../")
                    stream.download()
                    print("download seccessful")
                    break

                except(Exception):
                    print("eror‼ something went wrong!")

        elif(p == 2):
            print("Progressing...")
            stream = video.streams.filter(only_audio=True)
            if(stream):
                try:
                    print("downloading started.../")
                    stream.first().download()
                    print("download seccessful!")

                except(Exception):
                    print("eror‼ something isn't right")

        else:
            print('''please enter the video link again
                and select the option correctly''')
            continue
    except Exception:
        n -= 1
        if(n > 0):
            print("\nEror‼ Enter again")

    if(n == 0):
        print('''\nit's been three times..
            Close the program ،
            check the link ،
            then come back♥''')
