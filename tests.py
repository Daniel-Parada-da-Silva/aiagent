import unittest
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content


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
    
    # def test_lorem_ipsum(self):
    #     result = get_file_content("calculator", "lorem.txt")
    #     print(result)

    def test_file_content_calculator_main(self):
        result = get_file_content("calculator", "main.py")
        print(result)

    def test_file_content_calculator_pkg_calculator(self):
        result = get_file_content("calculator", "pkg/calculator.py")
        print(result)

    def test_file_content_calculator_bin(self):
        result = get_file_content("calculator", "/bin/cat")
        print(result)


if __name__ == "__main__":
    unittest.main()