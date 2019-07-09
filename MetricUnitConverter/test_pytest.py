import pytest
from InputParser import *
from MetricUnitParser import *
from MetricUnitConverter import *


def test_IfFileDoesNotExist_Raises_FIleNotFoundException():
    pass


def test_IfMeasureUnitIsNotInDict_Raises_MeasureUnitError():
    test_unit_parser = metric_unit_parser()
    with pytest.raises(MeasureUnitError):
        assert test_unit_parser.get_conversion_factor("gm", "Ym")


def test_IfInputLineNotCorrect_Raises_InputValueError():

    with pytest.raises(InputValueError):
        assert metric_unit_converter("ab", "m", "m")


def test_With5_m_m_Returns_5():
    test_conversion = metric_unit_converter("5", "m", "m")
    assert test_conversion.get_output_value() == 5.0


def test_Withm_cm_Returns_100():
    test_conversion = metric_unit_parser()
    assert test_conversion.get_conversion_factor("m", "cm") == 100


def test_Withmm_m_Returns_decimal001():
    test_conversion = metric_unit_parser()
    assert test_conversion.get_conversion_factor("mm", "m") == 0.001
