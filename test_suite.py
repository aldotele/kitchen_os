import unittest
from tests.test_kitchen_os import TestKitchenOS


def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(TestKitchenOS("test_kitchen_os"))
    return test_suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
