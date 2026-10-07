import unittest

import pantry


class PackageTest(unittest.TestCase):
    def test_version(self):
        self.assertEqual(pantry.__version__, "0.0.0")


if __name__ == "__main__":
    unittest.main()
