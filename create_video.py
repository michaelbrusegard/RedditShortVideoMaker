import os
import moviepy.editor as mp
import random

def edit_video(background_video, screenshots, speech_files):
    print('Editing video...')
    assets_dir = 'assets'  # directory where the files are located

    # Set the size and frame rate of the output video
    size = (1440, 2560)
    fps = 60

    print('Cropping background video...')
    # Load the background video
    bg_clip = mp.VideoFileClip(os.path.join(assets_dir, background_video))

    # Set the frame rate of the input video to 60fps
    bg_clip = bg_clip.set_fps(fps)

    # Get a random 60 second segment from the middle of the background video
    start_time = random.uniform(30, bg_clip.duration - 60 - 30)
    end_time = start_time + 60
    bg_clip = bg_clip.subclip(start_time, end_time)

    # Crop the middle part of the clip to make it vertical
    bg_center_x = bg_clip.w // 2
    bg_center_y = bg_clip.h // 2
    crop_width = bg_clip.h * size[0] // size[1]
    crop_height = bg_clip.h
    bg_clip = bg_clip.crop(bg_center_x - crop_width//2, bg_center_y - crop_height//2,
                           bg_center_x + crop_width//2, bg_center_y + crop_height//2)
    bg_clip = bg_clip.resize(size)

    print('Adding screenshots and speech...')

    print('Writing output video...')
    # Set the frame rate of the output video to 60fps
    final_clip = bg_clip.set_fps(fps)

    # Set the video codec and bitrate for the output video
    codec = 'libx264'
    bitrate = '50M'

    # Write output video with H.264 codec and high bitrate of 50Mbps
    final_clip.write_videofile("output.mp4", codec=codec, bitrate=bitrate)
