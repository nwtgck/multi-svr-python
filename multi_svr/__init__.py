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
