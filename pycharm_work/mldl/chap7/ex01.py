from tensorflow import keras
from sklearn.linear_model import SGDClassifier
import matplotlib.pyplot as plt

(train_input,train_target),(test_input,test_target) = keras.datasets.fashion_mnist.load_data()

print(train_input.shape)
print(train_target.shape)
train_input = train_input.reshape(-1,784)
test_input = test_input.reshape(-1,784)
train_scaled = train_input/255.0
test_scaled = test_input/255.0

sgd = SGDClassifier(loss='log',random_state=42,max_iter=5)
sgd.fit(train_scaled,train_target)

훈련점수 = sgd.score(train_scaled,train_target)
테스트점수 = sgd.score(test_scaled,test_target)
print(훈련점수)
print(테스트점수)

plt.imshow(train_input[0].reshape(28,28),cmap='gray_r')
plt.show()

plt.imshow(train_scaled[0].reshape(28,28),cmap='gray_r')
plt.show()

pred = sgd.predict(train_scaled[0].reshape(-1,784))
print(pred)
pred = sgd.predict(train_scaled[1].reshape(-1,784))
print(pred)

plt.imshow(train_scaled[1].reshape(28,28),cmap='gray_r')
plt.show()

import numpy as np
print(np.round(train_scaled[1].reshape(28,28),decimals=2))

mydata = np.random.rand(784)
print(mydata.shape)
print(mydata)

mydata = mydata.reshape(28,28)
mydata[:16,0] = 0
mydata[:16,1] = 0
mydata[:15,2] = 0
mydata[:15,3] = 0
mydata[:14,4] = 0
mydata[:14,5] = 0
mydata[:13,6] = 0
mydata[:12,7] = 0
mydata[:11,8] = 0
mydata[:10,9] = 0
mydata[:9,10] = 0
mydata[:8,11] = 0
mydata[:7,12] = 0
mydata[:6,13] = 0
mydata[:5,14] = 0
mydata[:4,15] = 0

mydata[25:28,:20] = 0
mydata[27:28,:28] = 0

plt.imshow(mydata,cmap='gray_r')
plt.show()

pred = sgd.predict(mydata.reshape(-1,784))
print(pred)
