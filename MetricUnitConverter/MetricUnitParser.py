from Errors import *


factors = dict()
factors["ym"] = -24
factors["zm"] = -21
factors["am"] = -18
factors["fm"] = -15
factors["pm"] = -12
factors["nm"] = -9
factors["µm"] = -6
factors["mm"] = -3
factors["cm"] = -2
factors["dm"] = -1
factors["m"] = 0
factors["dam"] = 1
factors["hm"] = 2
factors["km"] = 3
factors["Mm"] = 6
factors["Gm"] = 9
factors["Tm"] = 12
factors["Pm"] = 15
factors["Em"] = 18
factors["Zm"] = 21
factors["Ym"] = 24


class metric_unit_parser():

    def get_conversion_factor(self, input_unit, output_unit):

        if(self.check_measure_unit(input_unit)):
            raise MeasureUnitError(input_unit)

        if(self.check_measure_unit(output_unit)):
            raise MeasureUnitError(output_unit)

        input_factor = factors[input_unit]
        output_factor = factors[output_unit]

        exp = input_factor - output_factor

        factor = 10**exp
        return factor

    def check_measure_unit(self, unit):
        check = unit in factors
        if(check):
            return False
        return True
