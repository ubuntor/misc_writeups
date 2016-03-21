import os

os.system('ffmpeg -i catvideo.mp4 -f image2 %06d.png')

images = [i for i in sorted(os.listdir('.')) if i[-4:] == '.png' and len(i) == 10]
for i in range(len(images)-1):
    print(images[i],images[i+1])
    os.system('composite %s %s -compose difference diff%s'% (images[i],images[i+1],images[i]))

# see diff000136.png
