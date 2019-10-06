import datetime
from celery import shared_task
from django.conf import settings
from moviepy.editor import *
from os import listdir, makedirs, path
from os.path import basename, join, isfile
from pathlib import Path


def create_destination_folder():
    """Creates folder with name based on datetime"""
    videos_folder = settings.VIDEOS_DIR
    task_name = datetime.datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    destination_folder = path.join(videos_folder, task_name)
    makedirs(destination_folder, exist_ok=True)
    return destination_folder


def upload_original_videos(v, video_number, destination_folder):
    """Uploads original videos and places them in the destination folder"""
    with open(f"{destination_folder}\\{video_number}_{v}", "wb+") as destination:
        for chunk in v.chunks():
            destination.write(chunk)


@shared_task
def merge_videos(destination_folder):
    """Merge videos on alphabetical order"""
    print("Inside merge_videos")
    video_name = f"{os.path.basename(os.path.normpath(destination_folder))}.mp4"
    destination_filepath = os.path.join(destination_folder, video_name)
    result = {'destination_filepath': destination_filepath}
    video_files = sorted(Path(destination_folder).glob('*.mp4'))
    clips_list = [VideoFileClip(destination_folder + '\\' + video.name) for video in video_files]
    merged_video = concatenate_videoclips(clips_list)
    merged_video.write_videofile(destination_filepath, codec='libx264', audio_codec='aac')
    return result
