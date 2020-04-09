import unittest
from test.case.user.TestWareHouse import *

suite = unittest.TestSuite()

suite.addTest(TestWareHouse("test_1_token_1"))

unittest.TextTestRunner(verbosity=2).run(suite)