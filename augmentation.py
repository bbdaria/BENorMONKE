import random
import os
from PIL import ImageEnhance, Image

folder_path = '../BENresized'  # using the resized pictures
destination_path = '../BENmodified'
# did this once for ben and then once for monkey
# folder_path = 'MONKEresized'
# destination_path = 'MONKEmodified'

# Loop through all files in the folder
for file in os.listdir(folder_path):
  print(file)
  for i in range(100):
    print(i)
    image = Image.open(os.path.join(folder_path, file))
    modified_image = image.copy()

    if random.random() < 0.5: # 50% chance
      # Decrease color intensity by a random precent
      modified_image = ImageEnhance.Color(modified_image).enhance(random.random())
    if random.random() < 0.5: # 50% chance
        # Rotate the copy by a random number of degrees
      modified_image = modified_image.rotate(random.random() * 360)

    # Save the modified image
    modified_image.save(os.path.join(destination_path, 'modified_' +str(i)+ file))

print('All images have been modified and saved to the destination folder.')





