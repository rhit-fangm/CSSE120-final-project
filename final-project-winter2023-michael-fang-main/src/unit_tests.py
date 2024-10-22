"""
This module contains code for the final course project in
CSSE 120 - Introduction to Software Development.

This module contains unit tests for project functions.

Authors: Michael Fang
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import functions
from csv_reader import read_csv

marvel_data = read_csv(
    "/Users/michaelfang/PycharmProjects/final-project-winter2023-michael-fang/data/marvel-wikia-data.csv")

DC_data = read_csv("/Users/michaelfang/PycharmProjects/final-project-winter2023-michael-fang/data/dc-wikia-data.csv")

# -----------------------------------------------------------------------------
# TODO:
#   Write your TEST functions below this _TODO_.
#   Use the standard naming convention of  run_test_FUNCTION_NAME,
#   where FUNCTION_NAME is the name of the function you are testing.
# -----------------------------------------------------------------------------
def run_test_get_new_hero_by_year():
    expected = 357 # used search in pycharm
    actual = functions.get_new_hero_by_year(1990, marvel_data)
    print(actual, expected)
    if expected == actual:
        print("Pass")

    expected = 0 # used search in pycharm
    actual = functions.get_new_hero_by_year(1600, marvel_data)
    print(actual, expected)
    if expected == actual:
        print("Pass")

    expected = 9 # DC data use a different format, so I divided the search number
    actual = functions.get_new_hero_by_year(1950, DC_data)
    print(actual, expected)
    if expected == actual:
        print("Pass")

    expected = 167 # used search in pycharm
    actual = functions.get_new_hero_by_year(2013, marvel_data)
    print(actual, expected)
    if expected == actual:
        print("Pass")


# -----------------------------------------------------------------------------
# TODO:
#   Once you have written your tests, call the test functions in  main  to
#   verify that your functions pass the tests.
#  _
#   You may then comment out the testing function calls in  main , but do
#   not remove them.
# -----------------------------------------------------------------------------

