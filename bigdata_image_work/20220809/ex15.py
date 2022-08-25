import pandas as pd
import numpy as np

data = pd.read_excel('carprice.xlsx')
x_data = data[['년식','종류','연비','마력','토크','연료','하이브리드','배기량','중량','변속기']].to_numpy()
print(x_data[:5])
y_data = data['가격'].to_numpy()
print(y_data[:5])

np.savez('carprice.npz',x_data=x_data,y_data=y_data)