import unittest
import os
from main import KitchenOS


class TestKitchenOS(unittest.TestCase):
    def setUp(self):
        file_name_1 = "input1"  # CHANGE HERE to test with different files
        f1 = open(os.path.join("files", file_name_1), "r")
        self.os = KitchenOS(f1)
        f1.close()

    def test_kitchen_os(self):
        self.assertEqual(self.os.optimal_sequence, "V V V V M")  # CHANGE HERE the expected output
