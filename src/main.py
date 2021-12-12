from TextDataReader import TextDataReader
from XmlDataReader import XmlDataReader
from FindGoodStudents import FindGoodStudents
from CalcRating import CalcRating
import argparse
import sys


def get_path_from_arguments(args) -> str:
    parser = argparse.ArgumentParser(description="Path to datafile")
    parser.add_argument("-p", dest="path", type=str, required=True,
                        help="Path to datafile")
    args = parser.parse_args(args)
    return args.path


def main():
    path = get_path_from_arguments(sys.argv[1:])
    reader = XmlDataReader()
    students = reader.read(path)
    print("Students: ", students)
    good_students = FindGoodStudents(students).find()
    print("Good students: ", good_students)


if __name__ == "__main__":
    main()
