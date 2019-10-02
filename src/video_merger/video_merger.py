from moviepy.editor import *
from os import listdir, makedirs, path
from os.path import basename, join, isfile
from pathlib import Path

# Path where the videos to merge are placed
folder = r"G:\path\with\videos\to\merge"


def create_destination_path(folder):
    merged_filename = basename(folder).replace(' ', '_') + '.mp4'
    project_name = Path(folder).parents[0].name
    destination_folder = f'videos\\{project_name}'
    os.makedirs(destination_folder, exist_ok=True)
    destination_filepath = f'{destination_folder}\\{merged_filename}'
    return destination_filepath


def create_clips_list(folder):
    # Videos on the folder will be merged on alphabetical order
    video_files = sorted(Path(folder).glob('*.mp4'))
    clips_list = [VideoFileClip(folder + '\\' + video.name) for video in video_files]
    return clips_list


def merge_videos(clips_list, destination_filepath):
    merged_video = concatenate_videoclips(clips_list)
    merged_video.write_videofile(destination_filepath, codec='libx264', audio_codec='aac')


def main():
    destination_filepath = create_destination_path(folder)
    clips_list = create_clips_list(folder)
    merge_videos(clips_list, destination_filepath)


if __name__ == "__main__":
    main()
