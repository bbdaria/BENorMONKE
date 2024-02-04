import os
from PIL import Image

MONKEfolder_path = '../MONKEmodified'
MONKEdestination_path = '../MONKEpredict'
BENfolder_path = '../BENmodified'
BENdestination_path = '../BENpredict'

for file in os.listdir(BENfolder_path):

   if "cb01c75a-8474-471d-aea1-1c7c2e03801f" in file or "8f04982f-cd33-4876-a709-4c86c99588f9" in file \
      or "a3bc0916-111b-4e54-9549-1249f6655e80" in file:

         OBSpath = os.path.join(BENfolder_path, file)
         DESpath = os.path.join(BENdestination_path, file)
         image = Image.open(OBSpath)
         image.save(DESpath)
         os.remove(OBSpath)

for file in os.listdir(MONKEfolder_path):

   if "images (6)(1)" in file:

        OBSpath = os.path.join(MONKEfolder_path, file)
        DESpath = os.path.join(MONKEdestination_path, file)
        image = Image.open(OBSpath)
        image.save(DESpath)
        os.remove(OBSpath)







