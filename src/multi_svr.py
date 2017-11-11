import numpy as np
import sklearn
from sklearn import svm


class MutilSVR(sklearn.base.BaseEstimator, sklearn.base.RegressorMixin):
  def __init__(self, **kwargs):
    self.__init_kwargs = kwargs

  def fit(self, X, y, **kwargs):
    X = np.array(X)
    y = np.array(y)

    # Get dimension of y
    y_dim = np.ndim(y)
    if(y_dim == 2):
      # Feature dimension
      feature_dim = len(y[0])
      # Create SVRs
      self.svrs   = [svm.SVR(**self.__init_kwargs) for _ in range(feature_dim)]

      # For each SVR
      for curr_feature_dim, svr in enumerate(self.svrs): # (curr=Current)
        # Select y
        selected_y = y[:,curr_feature_dim]
        # Fit
        svr.fit(X, selected_y, **kwargs)
    else:
      raise Exception("Dimension of y must be 2, but found %d" % y_dim)


  def predict(self, X):
    # Init predict list
    preds = []
    # For each SVR
    for curr_feature_dim, svr in enumerate(self.svrs):  # (curr=Current)
      # Predict
      pred = svr.predict(X)
      # Append to preds
      preds.append(pred)

    pred = np.column_stack(tuple(preds))
    return pred




if __name__ == '__main__':
  from sklearn import metrics
  X = [
    [0,  0],
    [0, 10],
    [1, 10],
    [1, 20],
    [1, 30],
    [1, 40]
  ]

  y = [
    [0,  0],
    [0, 10],
    [2, 10],
    [2, 20],
    [2, 30],
    [2, 40]
  ]

  regressor = MutilSVR(kernel='linear')

  regressor.fit(X, y)

  pred_y = regressor.predict(X)
  err    = metrics.mean_squared_error(y, pred_y, multioutput='raw_values')

  print('pred_y:', pred_y)
  print('err:', err)
