import unittest
from tests.TestUtils import TestUtils
class ExceptionalTest(unittest.TestCase):
    def test_exceptional(self):
        test_obj = TestUtils()
        test_obj.yakshaAssert("TestExceptional",True,"boundary")
        print("TestExceptional = Passed")
