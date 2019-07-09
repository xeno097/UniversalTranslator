

class MeasureUnitError(Exception):

    def __init__(self, error_unit):
        print("Unit not found:", error_unit)


class InputValueError(Exception):

    def __init__(self, error_value):
        print("Bad input format:", error_value)


class FileOrPathNotFoundError(Exception):

    def __init__(self, error_directory):
        print("File or directory no found at: ", error_directory)
