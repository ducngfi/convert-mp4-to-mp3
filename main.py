import os
from moviepy.editor import *

def extract_audio(video_path, bitrate="128k"):
    # Load the video file
    video = VideoFileClip(video_path)

    # Extract the audio
    audio = video.audio

    # Get the base name and directory of the video file
    base_name = os.path.splitext(os.path.basename(video_path))[0]
    directory = os.path.dirname(video_path)

    # Construct the audio file path
    audio_path = os.path.join(directory, f"{base_name}.mp3")

    # Write the audio to an MP3 file with the specified bitrate
    audio.write_audiofile(audio_path, bitrate=bitrate)

    # Close the video and audio objects
    video.close()
    audio.close()

def main():
    video_path = "video.mp4"  # Change this to your video file path
    bitrate = "128k"  # Default bitrate
    extract_audio(video_path, bitrate)

if __name__ == "__main__":
    main()
