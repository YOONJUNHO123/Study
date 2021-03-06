# 1.데이터

import numpy as np
x_train = np.array([[1,2,3,4,5], [2,3,4,5,6], [3,4,5,6,7]])
y_train = np.array([6,7,8])

x_train = x_train.reshape(x_train.shape[0], x_train.shape[1],1)

# RNN은 순차형(sequential) 데이터를 모델링하는데 최적화된 구조

# print(x_train.shape) (3,5,1)
# print(y_train.shape) (3,)

# print(x_train)

#2. 모델 구성
from keras.models import Sequential
from keras.layers import Dense, LSTM, GRU, SimpleRNN
from keras.models import load_model
# from keras.layers import Dense, SimpleRNN

model = load_model("savetest01.h5")

model.summary() 


# 3. 훈련
model.compile(loss = 'mse', optimizer = 'adam', metrics=['mse'])
from keras.callbacks import EarlyStopping, TensorBoard # 웹에서 우리의 모델을 볼 수 있는 TensorBoard를 사용해보자
tb_hist = TensorBoard(log_dir = "D:\Study\keras\graph", histogram_freq =  0, write_graph = True, write_images=True) # 이 코드를 model.fit전에 삽입한다 그리고 fit의 callbacks를 수정해준다
early_stopping = EarlyStopping(monitor = 'loss', patience = 10, mode = 'min')
model.fit(x_train, y_train, epochs=1000, batch_size = 1, verbose=3, callbacks=[early_stopping,tb_hist] )
# 4. 예측
x_predict = np.array([[4,5,6,7,8]])
print(x_predict.shape)
x_predict = x_predict.reshape(x_predict.shape[0], x_predict.shape[1], 1)
print("x_predict.shape : ", x_predict.shape)
y_predict = model.predict(x_predict)
print(y_predict)