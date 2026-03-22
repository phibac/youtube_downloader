import subprocess

url = "https://www.youtube.com/watch?v=bunCcqOUkG4"

subprocess.run([
    "yt-dlp",
    "-f", "bv*+ba/b",            # best video + best audio
    "--merge-output-format", "mp4",
    "-o", "%(title)s.%(ext)s",
    url
])

url = "https://www.youtube.com/shorts/FTg_FLt0F9A"

subprocess.run([
    "yt-dlp",
    "-x",
    "--audio-format", "mp3",
    "-o", "%(title)s.%(ext)s",
    url
])