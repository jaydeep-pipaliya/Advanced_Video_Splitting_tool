import os
os.environ["IMAGEMAGICK_BINARY"] = "/usr/bin/convert"
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip, ColorClip

def convert_and_split_video(input_path, output_folder, clip_duration=55, aspect_ratio=(9, 16)):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    with VideoFileClip(input_path) as video:
        total_duration = video.duration

        # Target dimensions
        target_width = 1080
        target_height = int(target_width * aspect_ratio[1] / aspect_ratio[0])

        # Apply a zoom factor to make the video larger
        zoom_factor = 1  # Adjust this to control how much bigger the video appears
        video_width = int(video.w * zoom_factor)
        video_height = int(video.h * zoom_factor)

        part = 1
        start = 0

        while start < total_duration:
            end = min(start + clip_duration, total_duration)
            current_duration = end - start

            # Create base white background
            background = ColorClip(
                size=(target_width, target_height),
                color=(255, 255, 255)
            ).set_duration(current_duration)

            # Process video clip
            clip = video.subclip(start, end)
            clip_resized = clip.resize(width=video_width, height=video_height)

            # Center video vertically and horizontally
            video_x = (target_width - video_width) // 2
            video_y = (target_height - video_height) // 2

            # Create title text
            title_clip = TextClip(
                "New South Movie 🎬 🍿",
                fontsize=80,
                color='black',
                font="Liberation-Sans-Bold",
                method='label'
            ).set_duration(current_duration)

            # Position title above the video, shifted slightly to the right
            title_x = (target_width - title_clip.w) // 2 + 50  # Shift right by 50 pixels
            title_y = video_y - title_clip.h - 20

            # Create part number
            part_clip = TextClip(
                f"Part {part}",
                fontsize=70,
                color='black',
                font="Liberation-Sans-Bold",
                method='label'
            ).set_duration(current_duration)

            # Position part number below the video
            part_x = (target_width - part_clip.w) // 2
            part_y = video_y + video_height + 20

            # Combine elements
            final_clip = CompositeVideoClip(
                [
                    background,
                    clip_resized.set_position((video_x, video_y)),
                    title_clip.set_position((title_x, title_y)),
                    part_clip.set_position((part_x, part_y))
                ],
                size=(target_width, target_height)
            )

            output_path = f"{output_folder}/part_{part}.mp4"
            final_clip.write_videofile(
                output_path,
                codec="libx264",
                audio_codec="aac"
            )
            print(f"Saved {output_path}")

            start += clip_duration
            part += 1

    print("Processing complete.")

# Usage
input_video_path = "/home/jaydippipaliya/Downloads/Exp_parts/devera.mkv"
output_folder = "output_clips_folder"
convert_and_split_video(input_video_path, output_folder)
