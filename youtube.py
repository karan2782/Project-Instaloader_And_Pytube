from pytube import YouTube


link = "https://www.youtube.com/watch?v=VLXcWXyrUMM"
youtube_c = YouTube(link)
videos = youtube_c.streams.all()  # for video
audios = youtube_c.streams.filter(only_audio=True)  # for audio

vid = list(enumerate(videos))
aud = list(enumerate(audios))

while True:
    print("If you want to download video enter |v| \n If you want to download audio enter |a| \n And If you dont't want to download anything so enter |not|: ")
    choice = input()
    if choice=="v":
        for i in vid:
            print(i)
        print()

        strm_video = int(input("enter stream of video: "))
        videos[strm_video].download()
        print("Video download Successful!")

    elif choice == "a":
        for i in aud:
            print(i)
        print()

        strm_audio = int(input("enter stream of audio: "))
        audios[strm_audio].download()
        print("Audio Download Successful!")
    elif choice == "not":
        break
    else:
        print("Enter valid entries")

print("--Welcome--")
