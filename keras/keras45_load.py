# keras45_load.py

import numpy as np
from keras.models import Sequential
from keras.layers import Dense, LSTM

# 1. 데이터

a = np.array(range(1,11))
print(a)
size = 5                    # time_steps = 5

def split_x (x_list, size):
    x_list = []
    for i in range(len(a) - size +1 ):
        xset = a[i:size+i]
        x_list.append(xset)
    return np.array(x_list)

# def split_y (y_list, size):
#     y_list = []
#     for j in range(len(a) - size ):
#         yset = a[size + j]
#         y_list.append(yset)
#     return np.array(y_list)

# data_x = split_x(a,5)
# data_y = split_y(a,5)

# print(data_x.shape)
# print(data_y.shape)

# print(data_x)
# print(data_y)


# data_x = data_x.reshape(data_x.shape[0],data_x.shape[1],1)

dataset = split_x(a, size)      #(6,5)
print(dataset)

x1 = dataset[:, 0:4]
y1 = dataset[:, 4]
print(x1)
print(y1)


x1 = x1.reshape(x1.shape[0], x1.shape[1],1)
# x1 = np.reshape(x1, (6,4,1))
print(x1.shape)


# 2. 모델
from keras.models import load_model
model1 = load_model('./model/save_keras44.h5')
model1.add(Dense(10,name = 'a'))
model1.add(Dense(20,name = 'b'))
model1.add(Dense(30,name = 'c'))
model1.add(Dense(50,name = 'q'))
model1.add(Dense(1,name = '3'))

model1.summary()


# 3. 훈련
from keras.callbacks import EarlyStopping
earlystopping = EarlyStopping(monitor='loss', patience=10, mode='min')
model.compile(optimizer = 'adam', loss = 'mse', metrics=['mse'])
model.fit(x1, y1, epochs=140, callbacks=[earlystopping], batch_size=1, verbose=1)

# 4. 예측, 평가
loss, mse = model.evaluate(x1, y1, batch_size=1)

print("loss : ", loss)
print("mse : ", mse)


x = model.predict(x1)
print("predict : ",x)
