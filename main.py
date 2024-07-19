import os
from moviepy.editor import *

# Load the video file
video_path = "video.mp4"
video = VideoFileClip(video_path)

# Extract the audio
audio = video.audio

# Get the base name and directory of the video file
base_name = os.path.splitext(os.path.basename(video_path))[0]
directory = os.path.dirname(video_path)

# Construct the audio file path
audio_path = os.path.join(directory, f"{base_name}.mp3")

# Write the audio to an MP3 file with a bitrate of 128k
audio.write_audiofile(audio_path, bitrate="128k")

# Close the video and audio objects
video.close()
audio.close()
