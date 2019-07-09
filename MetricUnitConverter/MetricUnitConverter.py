from MetricUnitParser import metric_unit_parser
from Errors import InputValueError


class metric_unit_converter():

    def __init__(self, value, input_unit, output_unit):
        self.value = value
        self.input_unit = input_unit
        self.output_unit = output_unit

        input_checker = self.value_checker()
        if(input_checker[0]):
            raise InputValueError(input_checker[1])

        self.conversion_factor = metric_unit_parser(
        ).get_conversion_factor(input_unit, output_unit)

    def get_output_value(self):
        return self.value * self.conversion_factor

    def value_checker(self):
        check = False

        try:
            self.value = float(self.value)
        except Exception:
            return [True, self.value]

        try:
            self.input_unit = str(self.input_unit)
        except Exception:
            return [True, self.input_unit]

        try:
            self.output_unit = str(self.output_unit)
        except Exception:
            return [True, self.output_unit]

        return [check]
