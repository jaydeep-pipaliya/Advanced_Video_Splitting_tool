# Convert and Split Video Script

This Python script processes a video to create multiple clips of specified duration, adjusts their aspect ratio, and overlays custom text (a title and part numbers). The processed clips are saved in a specified output folder.

## Features

- Converts a video into smaller clips of a specified duration.
- Adjusts the video's aspect ratio to match a target dimension (default: 9:16).
- Adds a customizable title above the video and a part number below it.
- Centers the video in a white background with a zoom factor for resizing.
- Outputs clips in MP4 format.

## Requirements

- Python 3.6 or higher
- `moviepy` library
- `ImageMagick` (ensure it's installed and the binary path is set in the script)
- `ffmpeg` (used internally by `moviepy`)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/convert-and-split-video.git
    cd convert-and-split-video
    ```

2. Install dependencies:

    ```bash
    pip install moviepy
    ```

3. Ensure ImageMagick is installed on your system and update the binary path in the script if necessary.

    ```bash
    sudo apt install imagemagick
    ```

4. Install `ffmpeg` if not already installed:

    ```bash
    sudo apt install ffmpeg
    ```

## Usage

1. Update the following parameters in the script or pass them as function arguments:
    - `input_path`: Path to the input video file.
    - `output_folder`: Folder where the processed clips will be saved.
    - `clip_duration`: (Optional) Duration of each clip in seconds (default: 55).
    - `aspect_ratio`: (Optional) Target aspect ratio for the output videos (default: 9:16).

2. Run the script:

    ```bash
    python convert_and_split_video.py
    ```

3. The processed video clips will be saved in the specified output folder as `part_1.mp4`, `part_2.mp4`, and so on.

## Script Explanation

### Parameters

- **`input_path`**: Path to the video you want to process.
- **`output_folder`**: Path where output files will be saved. The folder will be created if it doesn't exist.
- **`clip_duration`**: Length of each clip (default: 55 seconds).
- **`aspect_ratio`**: Target aspect ratio (default: 9:16).

### Steps

1. **Split Video**:
    - The script calculates the total duration of the video and splits it into smaller clips.
2. **Aspect Ratio Adjustment**:
    - Clips are resized to fit the specified aspect ratio with a zoom factor for enhanced framing.
3. **Text Overlay**:
    - Adds a title and a part number to each clip.
4. **Output**:
    - Saves each processed clip in the specified output folder in MP4 format.

## Example

Assuming your video file is `example.mp4` and you want to save the processed clips in the `output_clips` folder:

```python
convert_and_split_video(
    input_path="example.mp4",
    output_folder="output_clips",
    clip_duration=60,
    aspect_ratio=(9, 16)
)
```

## Outputs

The output clips will be named sequentially as:
- `part_1.mp4`
- `part_2.mp4`
- `part_3.mp4`

...and so on, depending on the video's total duration.

## Troubleshooting

- If you encounter issues with `ImageMagick`, ensure the binary path is correct:
    ```python
    os.environ["IMAGEMAGICK_BINARY"] = "/usr/bin/convert"
    ```
- Ensure `ffmpeg` is installed on your system.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue for improvements or bug fixes.

---
