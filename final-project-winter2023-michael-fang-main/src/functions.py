"""
This module contains code for the final course project in
CSSE 120 - Introduction to Software Development.

This module contains functions written for the project.

Authors: Michael Fang
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import matplotlib.pyplot as plt
from csv_reader import read_csv

# -----------------------------------------------------------------------------
# DONE:
#   Write your functions below this _TODO_.
#   Make sure each function has a complete doc-string to go with it!
#  _
#   Alternatively, you may write your functions in multiple files. A good
#   organizational strategy is to group functions by purpose. All function
#   code files should be named  <description of functions>_functions.py  ,
#   where  <description of functions>  is a placeholder.
# -----------------------------------------------------------------------------

import os

marvel_data = read_csv(
    "/Users/michaelfang/PycharmProjects/final-project-winter2023-michael-fang/data/marvel-wikia-data.csv")
DC_data = read_csv("/Users/michaelfang/PycharmProjects/final-project-winter2023-michael-fang/data/dc-wikia-data.csv")

page_id, name, urlslug, ID, ALIGN, EYE, HAIR, SEX, GSM, ALIVE, APPEARANCES, FIRST_APPEARANCE, Year \
    = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12


def run_visualization():
    """
    Side effects: the function ask for visualization user wants to see and calls the appropriate function
    """
    print()
    print("Visualization Manuel")
    print()
    print("Options: ")
    print("1 Number of New Heroes by year(line plot)")
    print("2 Number of New Female Heroes by year(line plot)")
    print("3 Good, Bad, and Neutral Characters(pie chart)")
    print("4 Gender Gep of New Heroes by year(bar plot)")
    print()

    vis_choice = input("Enter visualization you want to see: ")
    if vis_choice == "1":
        print()
        data_set = int(input("Enter the data set you want to check(0 for Marvel, 1 for DC): "))
        start_year = int(input("Enter the starting year: "))
        end_year = int(input("Enter the ending year: "))
        if data_set == 0:
            run_vis_1(start_year, end_year, marvel_data)
        elif data_set == 1:
            run_vis_1(start_year, end_year, DC_data)
    elif vis_choice == "2":
        print()
        data_set = int(input("Enter the data set you want to check(0 for Marvel, 1 for DC): "))
        start_year = int(input("Enter the starting year: "))
        end_year = int(input("Enter the ending year: "))
        if data_set == 0:
            run_vis_2(start_year, end_year, marvel_data)
        elif data_set == 1:
            run_vis_2(start_year, end_year, DC_data)
    elif vis_choice == "3":
        print()
        data_set = int(input("Enter the data set you want to check(0 for Marvel, 1 for DC): "))
        if data_set == 0:
            print("Marvel Data: ")
            run_vis_3(marvel_data)
        elif data_set == 1:
            print("DC data: ")
            run_vis_3(DC_data)
    elif vis_choice == "4":
        print()
        data_set = int(input("Enter the data set you want to check(0 for Marvel, 1 for DC): "))
        start_year = int(input("Enter the starting year: "))
        end_year = int(input("Enter the ending year: "))
        if data_set == 0:
            run_vis_4(start_year, end_year, marvel_data)
        elif data_set == 1:
            run_vis_4(start_year, end_year, DC_data)
    else:
        print("Invalid Input")


def run_statistics():
    """
    Side effects: the function ask for statistics user wants to see and calls the appropriate function
    """
    print("Statistics Options: ")
    print("1, Number of Living Marvel Superheroes")
    print("2, Number of Living DC superheroes")
    print("3, Number of male character that are alive")
    print("4, Number of female character that are alive")

    stats_choice = input("Enter statistics you want to see: ")
    if stats_choice == "1":
        print()
        run_stats_1()
    elif stats_choice == "2":
        print()
        run_stats_2()
    elif stats_choice == "3":
        print()
        data_set = int(input("Enter the data set you want to check(0 for Marvel, 1 for DC): "))
        if data_set == 0:
            print("Marvel Data: ")
            run_vis_3(marvel_data)
        elif data_set == 1:
            print("DC data: ")
            run_stats_3(DC_data)
    elif stats_choice == "4":
        print()
        data_set = int(input("Enter the data set you want to check(0 for Marvel, 1 for DC): "))
        if data_set == 0:
            print("Marvel Data: ")
            run_stats_4(marvel_data)
        elif data_set == 1:
            print("DC data: ")
            run_stats_4(DC_data)
    else:
        print("Invalid Inputs")
        return_to_main()


def run_vis_1(start_year, end_year, data_set):
    """
    parameter: start_year, end_year, data_set

    side effects: run visualization with the given parameters

    :param start_year:
    :param end_year:
    :param data_set:
    :return:
    """
    x_data = ()
    y_data = ()
    for i in range(start_year, end_year + 1):
        y_data += (get_new_hero_by_year(i, data_set),)
        x_data += (i,)

    plot(x_data, y_data, "year", "New Heroes", "New Heroes by year", "../plots/visualization_1.png")
    print("Figure saved to plots")
    return_to_main()


def run_vis_2(start_year, end_year, data_set):
    """
    parameter: start_year, end_year, data_set

    side effects: run visualization with the given parameters

    :param start_year:
    :param end_year:
    :param data_set:
    :return:
    """
    x_data = ()
    y_data = ()
    for i in range(start_year, end_year + 1):
        y_data += (get_female_hero_by_year(i, data_set),)
        x_data += (i,)

    plot(x_data, y_data, "year", "Female Heroes", "Female Heroes by year", "../plots/visualization_2.png")
    print("Figure saved to plots")
    return_to_main()


def run_vis_3(data_set):
    """
    parameter: start_year, end_year, data_set

    side effects: run visualization with the given parameters

    :param data_set:
    :return:
    """
    align = ["Good", "Bad", "Neutral"]
    data = get_good_bad_neutral(data_set)

    fig, ax = plt.subplots()
    ax.pie(data, labels=align)

    if data_set == marvel_data:
        ax.set_title("Good, Bad and Neutral Marvel")
    elif data_set == DC_data:
        ax.set_title("Good, Bad and Neutral DC")

    plt.show()
    fig.savefig("../plots/visualization_3.png")
    print("Figure saved to plots")
    return_to_main()


def run_vis_4(start_year, end_year, data_set):
    """
    parameter: start_year, end_year, data_set

    side effects: run visualization with the given parameters

    :param start_year:
    :param end_year:
    :param data_set:
    :return:
    """
    x_data = ()
    y_data = ()
    for i in range(start_year, end_year + 1):
        y_data += (get_gender_gap(i, data_set), )
        x_data += (i, )

    fig, ax = plt.subplots()
    plt.bar(x_data, y_data, width=0.5)

    if data_set == marvel_data:
        ax.set_title("Gender Gap Marvel")
    elif data_set == DC_data:
        ax.set_title("Gender Gap DC")

    plt.show()
    fig.savefig("../plots/visualization_4.png")
    print("Figure saved to plots")
    return_to_main()

def run_stats_1():
    """
    side effects: run the statistics calculation and print the results
    :return:
    """
    count = 0
    for i in range(1, len(marvel_data)):
        if marvel_data[i][9] == "Living Characters":
            count += 1

    print(count, " Marvel heroes are currently alive")
    print("Figure saved to plots")
    return_to_main()

def run_stats_2():
    """
    side effects: run the statistics calculation and print the results

    :return:
    """
    count = 0
    for i in range(1, len(DC_data)):
        if DC_data[i][9] == "Living Characters":
            count += 1

    print(count, " DC heroes are currently alive")
    print("Figure saved to plots")
    return_to_main()


def run_stats_3(data_set):
    """
    side effects: run the statistics calculation and print the results

    :param data_set:
    :return:
    """
    count = 0
    for i in range(1, len(data_set)):
        if data_set[i][9] == "Living Characters" and data_set[i][SEX] == "Male Characters":
            count += 1

    print(count, " male heroes are currently alive")
    print("Figure saved to plots")
    return_to_main()


def run_stats_4(data_set):
    """
    side effects: run the statistics calculation and print the results

    :param data_set:
    :return:
    """
    count = 0
    for i in range(1, len(data_set)):
        if data_set[i][9] == "Living Characters" and data_set[i][SEX] == "Female Characters":
            count += 1

    print(count, " female heroes are currently alive")
    print("Figure saved to plots")
    return_to_main()


def plot(x, y, x_label, y_label, title, save_path):
    """
    side effects: plot the figure and save it

    :param x:
    :param y:
    :param x_label:
    :param y_label:
    :param title:
    :param save_path:
    :return:
    """
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_title(title)
    ax.grid()

    plt.show()
    fig.savefig(save_path)

def get_new_hero_by_year(year, data_set):
    """
    side effects: find the number of new heroes from the given dataset in the given year

    :param year:
    :param data_set:
    :return:
    """
    count = 0
    for i in range(len(data_set)):
        if data_set[i][12] == year:
            count += 1

    return count


def get_female_hero_by_year(year, data_set):
    """
    side effects: find the number of female heroes from the given year and dataset
    :param year:
    :param data_set:
    :return:
    """
    count = 0
    for i in range(len(data_set)):
        if data_set[i][7] == "Female Characters" and data_set[i][12] == year:
            count += 1

    return count


def get_male_hero_by_year(year, data_set):
    """
    side effects: find the number of male heroes from the given year and dataset
    :param year:
    :param data_set:
    :return:
    """
    count = 0
    for i in range(len(data_set)):
        if data_set[i][7] == "Male Characters" and data_set[i][12] == year:
            count += 1
    return count

def get_gender_gap(year, data_set):
    """
    side effects: get the difference between male heroes and female heroes from the year and dataset
    :param year:
    :param data_set:
    :return:
    """
    return get_male_hero_by_year(year, data_set) - get_female_hero_by_year(year, data_set)

def get_good_bad_neutral(data_set):
    """
    side effects:get the number of good, bad, and neutral characters from the given dataset
    :param data_set:
    :return: [good, bad, neutral]
    """
    good_count = 0
    bad_count = 0
    neutral_count = 0
    for i in range(len(data_set)):
        if data_set[i][4] == "Good Characters":
            good_count += 1
        elif data_set[i][4] == "Bad Characters":
            bad_count += 1
        elif data_set[i][4] == "Neutral Characters":
            neutral_count += 1

    return [good_count, bad_count, neutral_count]


def return_to_main():
    """
    side effects: give user the options from the main menu
    :return:
    """
    print()
    vis_or_stats = input("What else? (visualize enter 0 or statistics enter 1): ")
    print()
    if vis_or_stats == "0":
        run_visualization()
    elif vis_or_stats == "1":
        run_statistics()
    else:
        print("invalid input")

# -----------------------------------------------------------------------------
# TODO:
#   Write unit tests for your functions in  unit_tests.py
# -----------------------------------------------------------------------------
