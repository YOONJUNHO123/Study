from sklearn.datasets import load_diabetes
from keras.utils import np_utils
from keras.models import Sequential, Model
from keras.layers import Dense, LSTM, Conv2D
from keras.layers import Flatten, MaxPooling2D, Dropout
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import numpy as np
import pandas as pd
'''
# data      : x 값
# target    : y 값
'''
# 1. 데이터
dataset = load_diabetes()

x = dataset.data
y = dataset.target

df = pd.DataFrame(x, columns = dataset.feature_names)
df['traget'] = y
print(df.head())
print(x)
# print(y)
print(x.shape)
print(y.shape)

print(y)

scaler = StandardScaler()
x = scaler.fit_transform(x)

pca = PCA(n_components=10)
pca.fit(x)
x = pca.transform(x)

x_train, x_test, y_train, y_test = train_test_split(x,y,random_state = 66, shuffle = True, test_size = 0.2)



# y_train = np_utils.to_categorical(y_train)
# y_test = np_utils.to_categorical(y_test)
print(x_train.shape)
print(y_train.shape)

print(x_test.shape)
print(y_test.shape)
# df_train = pd.DataFrame(x_train, columns = dataset.feature_names)
# print(df_train.head())

# df_test = pd.DataFrame(x_test, columns = dataset.feature_names)
# print(df_test.head())
# print(x_train)
# print(y_train.shape)



# 2. 모델
model = Sequential()
model.add(Dense(100, input_shape =(10,)))
model.add(Dense(5000, activation='relu'))
model.add(Dense(1,activation='relu'))
model.summary()
# 3. 학습
model.compile(optimizer='adam', loss='mse', metrics=['mse'])
model.fit(x_train, y_train, batch_size=1, epochs=100, validation_split=0.2)


# 4. 예측

loss, mse = model.evaluate(x_test, y_test)

y_predict = model.predict(x_test)

print('pred : ',y_predict)

print('loss : ',loss)
print('mse : ',mse)

from sklearn.metrics import mean_squared_error #RMSE 함수화 => 캐글 및 대회에서 정확도 지수로 많이 사용
def RMSE(y_test, y_predict):
    return np.sqrt(mean_squared_error(y_test,y_predict))
print("RMSE : ", RMSE(y_test, y_predict))

# R2구하기 0~1 사이의 값 1에 가까울수록 신뢰도가 올라감 but 맹신은 금지 (데이터의 연관성이 있긴 하나 다른 데이터의 변수도 생각해야함)
from sklearn.metrics import r2_score
r2 = r2_score(y_test, y_predict)
print("R2 : ", r2)
