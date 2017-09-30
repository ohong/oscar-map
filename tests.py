"""
@author: Oscar Hong (@ohong)
@date: 09-30-2017
"""

import sys
import logging
import unittest
from main import OscarMap


class OscarMapTest(unittest.TestCase):

    # logs are written to 'log_file.txt'
    # highest to lowest urgency: CRITICAL > ERROR > WARNING > INFO > DEBUG
    logging.basicConfig(filename='log_file.txt', level=logging.DEBUG,
                        format='%(asctime)s - %(levelname)s - %(message)s')

    @classmethod
    def setUpClass(self):
        self.test = OscarMap(10)
        self.SetUpDone = True

    def test_0_is_empty(self):
        self.assertEqual(self.test.load(), float(0))

    def test_1_set_valid(self):
        self.assertEqual(self.test.set("alice", 0), True)
        self.assertEqual(self.test.set("alice", 0), True)
        self.assertEqual(self.test.set("alice", 9000), True)
        self.assertEqual(self.test.set("brian", 1), True)
        self.assertEqual(self.test.set("christie", 2), True)
        self.assertEqual(self.test.set("dan", 3), True)
        self.assertEqual(self.test.set("eve", 4), True)
        self.assertEqual(self.test.set("franco", 5), True)
        self.assertEqual(self.test.set("gabby", 6), True)
        self.assertEqual(self.test.set("hank", 7), True)
        self.assertEqual(self.test.set("isabella", 8), True)
        self.assertEqual(self.test.set("jimmy", 9), True)

    def test_2_set_invalid(self):
        self.assertEqual(self.test.set("oscar", 10), False)

    def test_3_get_valid(self):
        self.assertEqual(self.test.get("brian"), True)

    def test_4_get_invalid(self):
        self.assertEqual(self.test.get("alexa"), None)

    def test_5_delete_valid(self):
        self.assertEqual(self.test.delete("isabella"), 8)

    def test_6_delete_invalid(self):
        self.assertEqual(self.test.delete("jacob"), None)

    def test_7_load(self):
        self.assertEqual(self.test.load(), 0.9)
        self.test.display()


if __name__ == '__main__':
    unittest.main()
