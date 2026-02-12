from lib.report_length import *

def test_report_length_with_short_string():
    result = report_length("lina")
    assert result ==f"This string was 4 char long."

def test_report_lenght_with_long_string():
    result = report_length("wealthyandhealthy")
    assert result ==f"This string was 17 char long."

