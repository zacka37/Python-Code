import numpy as np
from sklearn import preprocessing, svm
from sklearn.model_selection import cross_val_predict, train_test_split
from sklearn.linear_model import LinearRegression
import pandas as pd
import quandl, math, datetime
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

df = quandl.get('WIKI/Googl')

print(df.head())
df = df[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume']]
df["HL_PCT"] = (df['Adj. High'] - df['Adj. Close']) / df['Adj. Close'] * 100
df["PCT_CHANGE"] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100
df = df[['Adj. Close','HL_PCT','PCT_CHANGE','Adj. Volume']]

forcast_col = 'Adj. Close'
df.fillna(-99999, inplace=True)
# predict 10% of the data
forcast_out = int(math.ceil(0.1*len(df)))

df['label'] = df[forcast_col].shift(-forcast_out)
# print(df.tail())

x = np.array(df.drop(['label'],1))

x = preprocessing.scale(x)

x = preprocessing.scale(x)
x = x[:-forcast_out]
x_lately = x[-forcast_out:]
#df.dropna(inplace=True)
df.dropna(inplace=True)
y = np.array(df['label'])
y = np.array(df['label'])
# train 20% of the data
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=.2)
clif = LinearRegression(n_jobs = -1)
clif.fit(x_train, y_train)
accuracy = clif.score(x_test,y_test)

forcasr_set = clif.predict(x_lately)

# print(forcasr_set, accuracy, forcast_out)
df['Forecast'] = np.nan

last_date = df.iloc[-1].name
last_unix = last_date.timestamp()
one_day = 86400
next_unix = last_unix + one_day

for i in forcasr_set:
    next_date = datetime.datetime.fromtimestamp(next_unix)
    next_unix += one_day
    df.loc[next_date] = [np.nan for _ in range(len(df.columns)-1)] + [i]
df["Adj. Close"].plot()
df['Forecast'].plot()
plt.legend(loc=4)
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()