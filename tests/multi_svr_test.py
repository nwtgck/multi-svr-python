import unittest
from sklearn import metrics

import multi_svr

class MultiSVRTest(unittest.TestCase):

  def test_prediction(self):
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
    errs = metrics.mean_squared_error(y, pred_y, multioutput='raw_values')

    # Errors should be small
    assert(errs[0] < 0.05)
    assert(errs[1] < 0.05)


def suite():
  suite = unittest.TestSuite()
  suite.addTest(unittest.makeSuite(MultiSVRTest))
  return suite