import numpy as np
import matplotlib.pyplot as plt
import cv2
import time

from sklearn.neighbors import KNeighborsClassifier


x_data = np.array([

    #O
    [0, 255, 255, 255, 0,
     255, 0, 0, 0, 255,
     255, 0, 0, 0, 255,
     255, 0, 0, 0, 255,
     0, 255, 255, 255, 0],
    [0, 255, 255, 255, 0,
     255, 255, 0, 0, 255,
     255, 0, 0, 0, 255,
     255, 0, 0, 0, 255,
     0, 255, 255, 255, 0],
    [0, 255, 255, 255, 0,
     255, 0, 0, 255, 255,
     255, 0, 0, 0, 255,
     255, 0, 0, 0, 255,
     0, 255, 255, 255, 0],
    #X
    [255, 0, 0, 0, 255,
     0, 255, 0, 255, 0,
     0, 0, 255, 0, 0,
     0, 255, 0, 255, 0,
     255, 0, 0, 0, 255],
    [255, 255, 0, 0, 255,
     0, 255, 0, 255, 0,
     0, 0, 255, 0, 0,
     0, 255, 0, 255, 0,
     255, 0, 0, 0, 255],
    [255, 0, 0, 255, 255,
     0, 255, 0, 255, 0,
     0, 0, 255, 0, 0,
     0, 255, 0, 255, 0,
     255, 0, 0, 0, 255]
])
y_data = np.array([
    [0],
    [0],
    [0],
    [1],
    [1],
    [1]
])
y_data = ['o']*3 + ['x']*3
labels = ['오', '엑스']

start_time = time.time()
knclf = KNeighborsClassifier(n_neighbors=2)
knclf.fit(x_data,y_data)
end_time = time.time()

print('걸린시간 = ',end_time-start_time)

pred = knclf.predict(x_data[0].reshape(-1,25))
print(pred)


for i in range(6):
    plt.title(f'target ={y_data[i]} ')
    plt.imshow(x_data[i].reshape(5,5),cmap='gray_r')
    plt.savefig(f'x_data[{i}]_plt.png')
    #plt.show()
    plt.close()

# for i in range(6):
#    cv2.imwrite(f'x_data[{i}]_cv.png',x_data[i].reshape(5,5))
