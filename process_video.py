# convert videos to mp3
import os
import subprocess

files = os.listdir("videos")
for file in files:
    name, ext = os.path.splitext(file)      # drops ".webm"
    parts = name.split(" - ")
    tutorial_number = parts[0]              # "001"
    file_name = parts[-1]                   # "Intro & Setup"
    print(tutorial_number, file_name)
    subprocess.run(["ffmpeg", "-i", f"videos/{file}", f"audios/{tutorial_number} - {file_name}.mp3"])

