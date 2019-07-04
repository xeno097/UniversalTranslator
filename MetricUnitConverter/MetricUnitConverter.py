from MetricUnitParser import metric_unit_parser


class metric_unit_converter():

    def __init__(self, value, input_unit, output_unit):
        self.value = float(value)
        self.input_unit = input_unit
        self.output_unit = output_unit
        self.conversion_factor = metric_unit_parser(
        ).get_conversion_factor(input_unit, output_unit)

    def get_output_value(self):
        return self.value * self.conversion_factor
