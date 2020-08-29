from rearrange import rearrange_name
import unittest

class TestRearrange(unittest.TestCase):
    def test_basic(self):
        testcase = 'Wassay, Abdul'
        expected = 'Abdul Wassay'
        self.assertEqual(rearrange_name(testcase), expected)

unittest.main()