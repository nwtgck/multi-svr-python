# multi_svr - Multiple-targets Support Vector Regression

[![Build Status](https://travis-ci.org/nwtgck/multi-svr-python.svg?branch=develop)](https://travis-ci.org/nwtgck/multi-svr-python) [![Coverage Status](https://coveralls.io/repos/github/nwtgck/multi-svr-python/badge.svg?branch=develop)](https://coveralls.io/github/nwtgck/multi-svr-python?branch=develop)
 
 
 ## Installation
 
 ```bash
 pip3 install git+https://github.com/nwtgck/multi-svr-python
 ```
 
 
 ## Usage
 
 ```python
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
 ```
 
 ## How to test
 
 ```bash
 cd <this repo
 python setup.py test
 ```