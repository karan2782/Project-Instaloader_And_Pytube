# from pytube import YouTube
# import os
#
# # where to save
# SAVE_PATH = "D:"  # to_do
#
# # link of the video to be downloaded
# link = "https://www.youtube.com/watch?v=xWOoBJUqlbI"
#
# try:
#     # object creation using YouTube
#     # which was imported in the beginning
#     yt = YouTube(link)
#
#     # Get all available video streams for the video
#     video_streams = yt.streams.filter(file_extension='mp4')
#
#     # Choose the first stream (you can modify this logic based on your preferences)
#     if video_streams:
#         d_video = video_streams[0]
#
#         # Download the video and set the filename
#         d_video.download(output_path=SAVE_PATH, filename= "gVideo")
#         print("Download complete!")
#     else:
#         print("No mp4 video streams found.")
#
# except Exception as e:
#     print("An error occurred:", e)
#
# print('Task Completed!')
from pytube import YouTube
def audio_from_youtube(url):
    yt=YouTube(url)
    so=yt.streams.filter(only_audio=True).first()

    so.download()

video_url=input("Enter youtube url")
audio_from_youtube(video_url)