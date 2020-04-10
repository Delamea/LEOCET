#! ../venv/scripts python3
# encoding: utf-8

"""This file launches the software with provided tools"""
from App.data.load import updateDataFiles


def main():
    """ This function initialize and launch the app."""
    updateDataFiles()
    print("The software is ready !")


if __name__ == "__main__":
    main()
else:
    print("Error: this file is not a module or a package...")
