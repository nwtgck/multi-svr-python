import multi_svr
from sklearn import metrics

X = [
  [0, 0],
  [0, 10],
  [1, 10],
  [1, 20],
  [1, 30],
  [1, 40]
]

y = [
  [0, 0],
  [0, 10],
  [2, 10],
  [2, 20],
  [2, 30],
  [2, 40]
]

#  Create SVR
regressor = multi_svr.MutilSVR(kernel='linear')
# Fit
regressor.fit(X, y)
# Predict
pred_y = regressor.predict(X)
# Calc errors
errs = metrics.mean_squared_error(y, pred_y)

print('pred_y:', pred_y)
print('errs:', errs)