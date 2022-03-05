#import pytube library 
from pytube import YouTube
import re

#import the link 
link = input("enter the link of youtube video")

#add link to liabrary 
video = YouTube(link)

#print title of video 
print(video.title)

#function to display text if download in progress 
def progrees():
    print("download in progress")

#function to display text if download is finished 
def finsh():
    print("download done")

#dowload high resolution video 
video.streams.get_highest_resolution().download(output_path="E:\data science")
#call progress function 
video.register_on_progress_callback(progrees())
#call finsh function 
video.register_on_complete_callback(finsh())
