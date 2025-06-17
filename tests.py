import unittest
from functions.get_files_info import get_files_info


class TestCalculator(unittest.TestCase):
    def test_calculator_root(self):
        result = get_files_info("calculator", ".")
        print(result)

    def test_calculator_pkg(self):
        result = get_files_info("calculator", "pkg")
        print(result)

    def test_calculator_bin(self):
        result = get_files_info("calculator", "/bin")
        print(result)

    def test_calculator_parent(self):
        result = get_files_info("calculator", "../")
        print(result)


if __name__ == "__main__":
    unittest.main()