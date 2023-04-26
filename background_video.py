import os
import yt_dlp
import ffmpeg

def get_background_video(url):
    print('Downloading background video...')
    assets_dir = 'assets'
    video_id = url.split('?v=')[-1]
    webm_file = f"{video_id}.webm"
    mp4_file = f"{video_id}.mp4"
    if os.path.isfile(os.path.join(assets_dir, mp4_file)):
        print("Background video already exist. Skipping download...")
        return mp4_file
    ydl_opts = {
        'format': 'bestvideo[height=2160][fps=60]',
        'outtmpl': webm_file,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    input_stream = ffmpeg.input(os.path.join(assets_dir, webm_file))
    video_stream = input_stream['v']
    output_stream = ffmpeg.output(video_stream, os.path.join(assets_dir, mp4_file), vcodec='copy')
    ffmpeg.run(output_stream)
    os.remove(webm_file)
    return mp4_file