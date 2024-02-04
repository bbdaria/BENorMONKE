import os
from PIL import Image
import math

root_directory = "BENoriginal"
output_directory = "BENresized"
# did this once for ben and the other one for monkey
# root_directory = "MONKEoriginal"
# output_directory = "MONKEresized"

size = (512, 512)  # the size of pic we want
images = []

for index1, image in enumerate(os.listdir(root_directory)):
    print(image)
    print(f"appending image num {index1}")
    images.append((Image.open(root_directory + "/" + image), image))

for index, image in enumerate(images):
    print(f"processed {math.floor(index*100/len(images))}")
    image[0].resize(size).save(output_directory + "/" + image[1])





