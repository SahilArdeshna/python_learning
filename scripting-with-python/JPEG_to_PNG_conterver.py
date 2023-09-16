import sys
import os

from PIL import Image

# Grab first and second arguments
PATH = sys.argv[1]
DESTINATION = sys.argv[2]

# Check if second argument which folder path exist or create
if not os.path.exists(DESTINATION):
    os.makedirs(DESTINATION)

# loop throgh images
for filename in os.listdir(PATH):
    # convert images to png
    img = Image.open(f'{PATH}{filename}')
    name = os.path.splitext(filename)[0]
    # save images to new folder
    img.save(f'{DESTINATION}{name}.png', 'png')
