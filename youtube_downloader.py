import subprocess
import sys

# url = "https://www.youtube.com/shorts/Nq7op3LdAk0"

# subprocess.run([
#     sys.executable, "-m", "yt_dlp",
#     "-f", "bestvideo+bestaudio",
#     "--merge-output-format", "mp4",
#     "-o", "%(title)s.%(ext)s",
#     url
# ])

url = "https://www.youtube.com/watch?v=69v-9S8ho5Q"

subprocess.run([
    sys.executable, "-m", "yt_dlp",
    "-x",
    "--audio-format", "mp3",
    "-o", "%(title)s.%(ext)s",
    url
])

# yt-dlp -f bestvideo+bestaudio --merge-output-format mp4 "https://www.youtube.com/watch?v=o8DqOfzFjls"