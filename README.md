**Video Processing with Logo and Text Overlay**

This project processes videos by applying a logo overlay and dynamic text based on the filename. It also includes an introduction clip before the main video. The script can handle films of any length and will display a logo in the top-right corner of each video.

**Features**
- Add a branding overlay to the video that remains visible during its duration.
- Create dynamic text from the filename and overlay it on the intro clip.
- Combine an introductory video with the main video.
- Works with videos of all lengths.

**Directory Structure**
The project expects the following directory structure:
.
```├── AltIntro.mp4       # Intro video to be appended at the start of each video.
├── Nhce_Logo.png      # Logo image to be overlaid on the video.
├── DBMS               # Directory containing lab videos 
│   ├── example_1.mp4
│   ├── example_2.mp4
│   └── ...
├── OS                 # Directory containing lab videos
│   ├── os_1.mp4
│   ├── os_2.mp4
│   └── ...
└── video_processing.py # The script file (your main code).
```

**Prerequisites**
- Python 3.x: Make sure you have Python installed. 
- ImageMagick: This project requires ImageMagick for image processing. 
- Required Libraries: Install the necessary Python libraries by running:
```pip install moviepy pillow
```

**How to Run**
- Clone the repository:
  https://github.com/astha-05/LabXpert.git
```cd video-processing
```
- Add your video files: Place your .mp4 video files in the DBMS or OS directories.
- Make sure you have:
Nhce_Logo.png in the root directory for the logo.
AltIntro.mp4 in the root directory for the intro clip.
- Run the Script: Run the script using the following command:
```python video_processing.py
```

**Output**
The processed video will be saved with the same filename as the original video. Each video will start with the intro, followed by the full video with a logo overlay.
