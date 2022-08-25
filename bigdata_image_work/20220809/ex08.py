import numpy as np
import matplotlib.pyplot as plt

img = np.random.randint(0,255,size=512*512).reshape(-1,512)
print(img.shape)

plt.imshow(img,cmap='gray_r')
plt.show()

img[100:200,200:300] = 255
plt.imshow(img,cmap='gray_r')
plt.show()