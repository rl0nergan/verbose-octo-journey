#!/Library/Frameworks/Python.framework/Versions/3.8/bin/python3

from PIL import Image
import os
i = 0
for fn in os.listdir("./start"):
  i += 1
  im = Image.open("./start/{}".format(fn))
  new_im = im.rotate(90).resize((480, 411)).copy().save(fp = "./end/{}{}.jpeg".format("new_image", str(i)))


