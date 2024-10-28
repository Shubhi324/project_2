import subprocess

# Replace 'rtsp://your_stream_url' with your RTSP or RTMP stream link
input_stream = 'rtsp://your_stream_url'
output_stream = 'rtmp://localhost/live/stream'

# Command to convert RTSP stream to RTMP
command = [
    'ffmpeg',
    '-i', input_stream,
    '-c:v', 'libx264',
    '-preset', 'ultrafast',
    '-f', 'flv',
    output_stream
]

# Run the ffmpeg command
process = subprocess.Popen(command)
