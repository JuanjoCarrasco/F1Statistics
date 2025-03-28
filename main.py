"""
@author: Juan José Carrasco Fernández.

Main file.

"""


# Import libraries.
import glob_vars
import load_data
import wdcs_info
import drivers_info
import races_info
import season_info
import wccs_info
import constructors_info
import sys
import inflect
from tabulate import tabulate
from pyfiglet import Figlet
from datetime import date

p = inflect.engine()

def main():
    """Display title, initialize global variables, load data
    and display the main menu.
    """
    title()
    glob_vars.init_glob_vars()
    load_data.load()
    main_selection()


def title():
    """Use figlet to display the program title using ASCII art fonts."""
    figlet = Figlet()
    # Alternative fonts: big, digital, slant, small, digital
    figlet.setFont(font="standard")
    print(figlet.renderText("Formula 1 World Championship"))  # (1950 - 2024)


def main_selection():
    """Display the main selection menu."""
    print("\nSelect data to retrieve:"
          "\n    -Press 1 for World Drivers' Champions."
          "\n    -Press 2 for World Constructors' Champions."
          "\n    -Press 3 for data about drivers."
          "\n    -Press 4 for data about constructors."
          "\n    -Press 5 for data about a season."
          "\n    -Press 6 for data about circuits."
          "\n    -Press 7 for info about F1 World Championship dataset."
          "\n    -Press 'e' to exit.")
    menu_selec = input("Select: ")

    match menu_selec:
        case "1":
            menu_sort("Drivers")
        case "2":
            menu_sort("Constructors")
        case "3":
            drivers_in = input("\nEnter the surname of one or more drivers separated by commas: ")
            drivers_info.show(drivers_in)
            main_selection()
        case "4":
            constructors_in = input("\nEnter name of one or more constructors separated by commas: ")
            constructors_info.show(constructors_in)
            main_selection()
        case "5":
            season_menu()
        #case "6":
        #    input("\nEnter the name of one or more circuits separated by commas: ")  # x =
        case "6":
            info_database()
        case "e":
            sys.exit("\nSee you next time!\n")
        case _:
            print("\nWrong selection.")
            main_selection()


def menu_sort(drivers_or_constructors):
    """Display the menu for sorting results."""
    print("\nSelect variable to sort results:"
          "\n    -Press 1 to sort by season."
          # "\n    -Press 2 to sort by driver's age."
          "\n    -Press 2 to sort by wins."
          "\n    -Press 3 to sort by win rate."
          "\n    -Press 4 to sort by points."
          "\n    -Press 5 to sort by points rate."
          "\n    -Press 6 to sort by points difference with the second classified."
          "\n    -Press 'r' to return."
          "\n    -Press 'e' to exit.")
    order_selec = input("Select: ")

    order_var = ["Season", "Wins", "W rate (%)", "Points", "P rate (%)",
                 "P with 2nd"]  # "Age",
    order_s = ["1", "2", "3", "4", "5", "6"]

    match order_selec:
        case order_selec if order_selec in order_s:
            if drivers_or_constructors == "Drivers":
                champion_drivers = wdcs_info.show(order_var[int(order_selec)-1])

                print("\nFormula One World Drivers' Champions")
                drivers_info.show(champion_drivers)

                menu_sort("Drivers")

            elif drivers_or_constructors == "Constructors":
                champion_constructors = wccs_info.show(order_var[int(order_selec)-1])

                print("\nFormula One World Constructors' Champions")
                constructors_info.show(champion_constructors)

                menu_sort("Constructors")

        case "r":
            main_selection()
        case "e":
            sys.exit("\nSee you next time!\n")
        case _:
            print("Wrong selection \n")
            menu_sort()


def season_menu():
    """Display the season menu."""
    x = input(f"\nEnter the year of a season (from {glob_vars.min_year} to {glob_vars.max_year}) or 'r' to return: ")

    if x == "r":
        main_selection()
    else:
        try:
            year = int(x)
            if year < glob_vars.min_year or year > glob_vars.max_year:
                print("Please enter a valid year.")
                season_menu()
            else:
                # info: Year, Round, Date, Name
                season = [(race_id, info) for race_id, info in
                          glob_vars.races.items() if int(info["Year"]) == year]

                season = sorted(season, key=lambda x: int(x[1]["Round"]),
                                reverse=False)

                race_menu(season)

        except (ValueError):
            print("Please enter a valid year.")


def race_menu(season):
    """Display the race menu."""
    print("\nSelect race to show results:")

    for race in season:
        print(f"    -Press {race[1]["Round"]} for {race[1]["Name"]} ({date.fromisoformat(race[1]["Date"])}).")

    print("\n    -Press 'f' to final results of the season."
          "\n    -Press 'r' to return."
          "\n    -Press 'e' to exit.")

    race_selec = input("Select: ")

    if race_selec == "f":
        season_info.show(season)
        race_menu(season)
    elif race_selec == "r":
        season_menu()
    elif race_selec == "e":
        sys.exit("\nSee you next time!\n")
    else:
        try:
            race_selec = int(race_selec)
            races_info.show(race_selec, season)
            race_menu(season)

        except (ValueError):
            print("\nWrong selection.")
            race_menu(season)


def info_database():
    """Information about the F1 database."""
    print("\nF1 World Championship dataset contains records of all F1 races, drivers, constructors, "
          "qualifying, circuits, lap times and pit stops from 1950 to 2024. \n")

    table = {}
    table["Seasons"] = [len(glob_vars.scoring)]
    table["Races"] = [len(glob_vars.races)]
    table["Drivers"] = [len(glob_vars.drivers_info)]
    table["Constructors"] = [len(glob_vars.constructors_info)]

    print(tabulate(table, headers = "keys", tablefmt="github"))
    input("\nPress any key to continue.")
    main_selection()


if __name__ == "__main__":
    main()
