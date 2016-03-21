# catvideo

Looking at the video, we can see moving lines in the random noise.
Converting the video into images using `ffmpeg` and taking the difference between each one with imagemagick's `composite` gives us the flag in the 136'th difference.

Code: [catvideo.py](catvideo.py)
