#!/usr/bin/env python3

# created by Youngjun Kim
# created on May 2021
# This program uses user defined functions


def calculate_area(base, height):
    # this function calculates area of a triangle

    # process
    area = base * height / 2

    # output
    print("The area is {0} cm²".format(area))

def main():
    # this function gets base and height

    # input
    base_from_user = int(input("Enter the base of a triangle: "))
    height_from_user = int(input("Enter the height of a triangle: "))
    print("")

    # call functions
    calculate_area(base_from_user, height_from_user)


if __name__ == "__main__":
    main()
