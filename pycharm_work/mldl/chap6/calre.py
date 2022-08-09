from sklearn import datasets
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn import model_selection
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from sklearn.preprocessing import PolynomialFeatures


datasets = datasets.fetch_california_housing()

x = datasets.data
y = datasets.target

print(x.shape)
print(y.shape)

dataframe = pd.DataFrame(datasets.data,columns=datasets.feature_names)
print(dataframe.head())
print(dataframe.tail())

train_input, test_input, train_target, test_target = \
 model_selection.train_test_split(x, y, random_state=42)

lr = LinearRegression()
lr.fit(train_input,train_target)

훈련점수 = lr.score(train_input, train_target)
테스트점수 = lr.score(test_input, test_target)

print(f'훈련점수 = {훈련점수}')
print(f'테스트점수 = {테스트점수}')

print(train_input[:2])
print(np.round(train_input[:2]))
print(train_target[:2])

pred = lr.predict(train_input[:2])
print(pred)
pred = lr.predict(np.round(train_input[:2]))
print(pred)

poly = PolynomialFeatures(degree=4)
poly.fit(train_input)

train_poly = poly.transform(train_input)
test_poly = poly.transform(test_input)

print(train_poly.shape)
print(test_poly.shape)

lr.fit(train_poly,train_target)

훈련점수 = lr.score(train_poly, train_target)
테스트점수 = lr.score(test_poly, test_target)

print(f'훈련점수 = {훈련점수}')
print(f'테스트점수 = {테스트점수}')


pred = lr.predict(train_poly[:2])
print(pred)
pred = lr.predict(np.round(train_poly[:2]))
print(pred)
print('----------------')

ridge = Ridge()
ridge.fit(train_poly,train_target)

pred = ridge.predict(train_poly[:2])
print(pred)
pred = ridge.predict(np.round(train_poly[:2]))
print(pred)

print('---------------')

lasso = Lasso()
lasso.fit(train_poly,train_target)

pred = lasso.predict(train_poly[:2])
print(pred)
pred = lasso.predict(np.round(train_poly[:2]))
print(pred)

훈련점수 = lasso.score(train_poly, train_target)
테스트점수 = lasso.score(test_poly, test_target)

print(f'훈련점수 = {훈련점수}')
print(f'테스트점수 = {테스트점수}')
