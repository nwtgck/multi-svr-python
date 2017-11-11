import unittest
import multi_svr

class MultiSVRTest(unittest.TestCase):

  def test_dummy(self):
    self.assertEqual(1, 1) # TODO impl


def suite():
  suite = unittest.TestSuite()
  suite.addTest(unittest.makeSuite(MultiSVRTest))
  return suite