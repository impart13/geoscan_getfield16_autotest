import pytest

class TestGetField16Positive:
    @pytest.mark.parametrize("hex_str,start_bit,expected", [
        ("0123", 0, "0123"),
        ("0123456789abcdef", 32, "89AB"),
        ("012345", 1, "0246"),
        ("0123456789ABCDEF0123456789ABCDEF", 111, "E6F7"),
        ("0123456789ABCDEF0123456789ABCDEF", 112, "CDEF"),
        ("F" * 32, 64, "FFFF"),
        ("0" * 32, 64, "0000"),
    ])
    def test_positive_cases(self, run_getfield16, hex_str, start_bit, expected):
        result = run_getfield16(hex_str, start_bit)
        assert result == expected


class TestGetField16Negative:
    @pytest.mark.parametrize("hex_str,start_bit", [
        ("0123456789ABCDEF", 62),
        ("0123456789ABCDEF0123456789ABCDEF", 113),
        ("C" * 16, 1000),
        ("0123", 1),
        ("0123456789ABCDEF", -1),
        ("0123456789ABCDEF", "f"),
        ("0123456789ABCDEF", "*"),
        ("0123456789ABCDEF", "3.14"),
        ("012345", "3,14"),
        ("012345", "0x10"),
        ("012345", " "),
        ("0123456789ABCDEF", "6 2"),
        ("0123456789ABCDEF", "6a"),
        ("0123456789ABCDEF", "\n"),
        ("0123456789ABCDEF", "\t"),
        ("0123456789ABCDEF", None),
        ("012345", 2147483648),
        ("012345", 4294967296),
        ("012345", 18446744073709551615),
        ("012345", -2147483648),
        ("012345", -9223372036854775808),
    ])
    def test_invalid_start_bit(self, run_getfield16, hex_str, start_bit):
        result = run_getfield16(hex_str, start_bit)
        assert any(error in result for error in ["Error", "Failed", "invalid", "TypeError"])
        
    @pytest.mark.parametrize("hex_str,start_bit", [
        ("0123456789ABCDEF0123456789ABCDEFF", 0),
        ("0x0123456789ABCDEF", 0),
        ("F"*130967, 0),
        (" ", 0),
        ("wrong_hex_string", 0),
        ("01234G", 0),
        ("0123 4567", 0),
        ("!@#$%^&*()", 0),
        ("01АБВ", 0),
        ("", 0),
        ("012", 0),
        (None, 0),
    ])
    def test_invalid_hex_string(self, run_getfield16, hex_str, start_bit):
        result = run_getfield16(hex_str, start_bit)
        assert any(error in result for error in ["Error", "Failed", "invalid", "TypeError"])