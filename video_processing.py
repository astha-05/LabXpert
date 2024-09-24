import os
from moviepy.editor import *

currentDirectory = os.getcwd()
subDirectories = os.listdir(currentDirectory)
subDirectories = [i for i in subDirectories if i == "DBMS" or i == "OS"]

for i in subDirectories[:]:  # AltIntro, DBMS, Nhce_Logo.png, OS, sem3.py
    for j in os.listdir(i):
        if j.endswith('.mp4'):
            mp4Split = j.rsplit('.mp4', 1)
            LabVidSplitList = mp4Split[0].split('_')
            LabVidString = '\n'.join(map(str, LabVidSplitList))

            # Full lab video path
            video_path = os.path.join(currentDirectory, i, j)

            # Load full lab clip 
            labClip = VideoFileClip(video_path)
            lw, lh = labClip.size  # Get lab video size

            # Load and configure the logo
            NhceLogo = ImageClip('Nhce_Logo.png')
            NhceLogo = NhceLogo.resize(0.2)  # Resize logo
            NhceLogo = NhceLogo.set_opacity(0.5)  # Set transparency
            NhceLogo = NhceLogo.set_duration(labClip.duration)  # Make logo duration match the full lab clip
            NhceLogo = NhceLogo.set_position(("right", "center"))  # Position the logo

            # Composite logo on the full lab video
            labClipWithLogo = CompositeVideoClip([labClip, NhceLogo])

            # Create the text clip
            txt_clip = TextClip(LabVidString, fontsize=35, color='white', font='Arial', interline=10)
            txt_clip = txt_clip.set_position('center')

            # Load intro clip
            introClip = VideoFileClip("AltIntro.mp4")

            # Background color for text (larger than text clip)
            w, h = txt_clip.size
            color_clip = ColorClip(size=(w + 300, h + 50), color=(0, 100, 150))
            color_clip = color_clip.set_opacity(0.5)

            # Composite the text on color background
            mask_clip = CompositeVideoClip([color_clip, txt_clip])
            mask_clip = mask_clip.set_position('center').set_duration(introClip.duration)
            mask_clip = mask_clip.crossfadein(0.9).crossfadeout(0.9)

            # Overlay the text on the intro video
            introVideo = CompositeVideoClip([introClip, mask_clip])
            introVideo = introVideo.set_duration(introClip.duration)

            # Concatenate intro video and the full lab video (with logo)
            final_clip = concatenate_videoclips([introVideo, labClipWithLogo])

            # Save the final video with the same name as the input video
            final_clip.write_videofile(j, codec="libx264", fps=24)
