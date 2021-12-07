import pandas as pd
from sklearn.naive_bayes import GaussianNB
from joblib import dump


data = pd.read_csv('pong_data.csv')
train_x = data[['ball_x', 'ball_y']]
print(train_x.shape)
train_y = data['paddle_y']
print(train_y.shape)

model = GaussianNB()
model.fit(train_x, train_y)
dump(model, 'modelG.joblib')