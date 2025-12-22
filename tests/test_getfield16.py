import pytest

class TestGetField16Positive:
    @pytest.mark.parametrize("hex_str,start_bit,expected", [
        ("0123456789ABCDEF", 0, "0123"),
        ("0123456789abCDEF", 32, "89AB"),
        ("012345", 1, "0246"),
        ("0123456789ABCDEF0123456789ABCDEF", 111, "E6F7"),
        ("0123456789ABCDEF0123456789ABCDEF", 112, "CDEF"),
        ("FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF", 64, "FFFF"),
        ("00000000000000000000000000000000", 64, "0000"),
    ])
    def test_positive_cases(self, run_getfield16, hex_str, start_bit, expected):
        result = run_getfield16(hex_str, start_bit)
        assert result == expected


class TestGetField16Negative:
    @pytest.mark.parametrize("hex_str,start_bit", [
        ("0123456789ABCDEF", 62),
        ("0123456789ABCDEF0123456789ABCDEF", 113),
        ("0123", 1),
        ("0123456789ABCDEF", -1),
        ("0123456789ABCDEF", "f"),
        ("0123456789ABCDEF", "*"),
        ("0123456789ABCDEF", 3.14),
        ("012345", "3,14"),
    ])
    def test_invalid_start_bit(self, run_getfield16, hex_str, start_bit):
        result = run_getfield16(hex_str, start_bit)
        assert "Error"  or "Failed" in result, f"Ожидалась ошибка, получено: '{result}'"
        
    @pytest.mark.parametrize("hex_str,start_bit", [
        ("0123456789ABCDEF0123456789ABCDEFF", 0),
        ("wrong_hex_string", 0),
        ("01234G", 0),
        ("0123 4567", 0),
        ("!@#$%^&*()", 0),
        ("01АБВ", 0),
        ("", 0),
        ("012", 0),
    ])
    def test_invalid_hex_string(self, run_getfield16, hex_str, start_bit):
        result = run_getfield16(hex_str, start_bit)
        assert "Error" or "Failed" in result, f"Ожидалась ошибка, получено: '{result}'"