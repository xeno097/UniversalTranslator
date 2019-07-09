from InputParser import input_parser
import sys


def main():
    input_dir = sys.argv[1:][0]
    converter = input_parser(input_dir)
    print("Completed")
