import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


data_path = "../../PlantDataset/IMG_6223.JPG"

image = Image.open(data_path)
image = np.asarray(image)

plt.imshow(image)
plt.show()
