import unittest
import main

class TestMain(unittest.TestCase):

    def test_add(self):
        self.assertEqual(main.add(8,2), 10)

if __name__ == '__main__':
    unittest.main()