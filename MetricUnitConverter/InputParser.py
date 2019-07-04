from MetricUnitParser import metric_unit_parser


class input_parser():

    def __init__(self, file_dir: str):
        self.file_dir = file_dir
        self.converter = metric_unit_parser()

    def reader(self):
        with open(self.file_dir) as input_file:
            line = input_file.readline()
            while line:
                line = str(line)
                values = line.split(",")
                print(line)
                line = input_file.readline()
