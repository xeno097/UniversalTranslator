from MetricUnitConverter import metric_unit_converter
from Errors import FileOrPathNotFoundError


class input_parser():

    def __init__(self, input_file_dir: str):
        self.input_file_dir = input_file_dir

        if(self.try_open()):
            raise FileOrPathNotFoundError(self.input_file_dir)

        self.output_file_dir = self.build_output_dir()
        self.create_output_file()
        self.reader()

    def build_output_dir(self):
        dir = self.input_file_dir.split("/")
        dir[len(dir)-1] = 'output.txt'
        dir = '/'.join(dir)
        return dir

    def create_output_file(self):
        with open(self.output_file_dir, "w") as output_file:
            output_file.close()

    def reader(self):
        with open(self.input_file_dir) as input_file:
            line = input_file.readline()
            while line:
                values = line.split(",")

                output_value = metric_unit_converter(
                    values[0], values[1], values[2]).get_output_value()

                values[len(values)-1] = (str(output_value)+'\n')
                line = ",".join(values)
                self.writer(line)
                line = input_file.readline()

    def writer(self, line):
        with open(self.output_file_dir, "a+") as output_file:
            output_file.write(line)

    def try_open(self):
        check = False
        try:
            stream = open(self.input_file_dir)
            stream.close()
        except Exception:
            check = True

        return check
