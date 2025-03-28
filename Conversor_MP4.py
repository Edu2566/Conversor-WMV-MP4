# Use togheter witch Free Cam player to convert videos quickly
from moviepy import VideoFileClip

def convert_wmv_to_mp4(input_path: str, output_path: str) -> None:
    clip = VideoFileClip(input_path)
    clip.write_videofile(output_path, codec="libx264", audio_codec="aac")

convert_wmv_to_mp4(r"C:\path\to\your\video.wvm", r"./outputs/output.mp4")
