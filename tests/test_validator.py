import unittest
from app.utility.validator import validate_name, validate_id, validate_phone_number


class TestUtility(unittest.TestCase):
    def test_validate_name_with_valid_input_int(self):
        self.assertEqual(False, validate_name("1234"))

    def test_validate_name_with_valid_input(self):
        self.assertEqual(True, validate_name("ปอซ่า"))

    def test_validate_name_with_valid_input_string(self):
        self.assertEqual(False, validate_name("ชายปอ007"))

    def test_validate_name_with_valid_input_string_char(self):
        self.assertEqual(False, validate_name("มีไรหรอ!"))

    def test_validate_name_with_valid_input_string_char_space(self):
        self.assertEqual(False, validate_name("xkp ss"))

    def test_validate_name_with_valid_input_string_char_None(self):
        self.assertEqual(False, validate_name(""))


if __name__ == '__main__':
    unittest.main()  # pragma: no cover
