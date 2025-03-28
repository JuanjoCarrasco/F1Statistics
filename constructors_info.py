"""Data about constructors."""

# Import libraries.
import glob_vars
import _aux
import find_last_rounds
import numpy as np
from tabulate import tabulate
#from datetime import date
import inflect
import unidecode

p = inflect.engine()

def show(constructors_in):

    constructors_list = []
    for i, name in enumerate(constructors_in.split(",")):
        name = unidecode.unidecode(name.strip().lower())
        constructors_list.append([(constructorId, info["Name"], info["Nationality"])
                                 for constructorId, info in glob_vars.constructors_info.items()
                                 if name == unidecode.unidecode(info["Name"].lower())
                                 ])

        if len(constructors_list[i]) == 0:
            print(f"{name} not found")

        elif len(constructors_list[i]) == 1:
            constructors_list[i] = constructors_list[i][0]

    if len(constructors_list) == 1 and not constructors_list[0]:
        return

    table = []
    for constructor_info in constructors_list:
        if constructor_info:
            info = {}

            last_rounds, last_rounds_driver_data, last_rounds_constructor_data = find_last_rounds.find_lr()

            # Number of constructors' world championships.
            wcc = 0
            wcc_year = []
            for year in last_rounds_constructor_data.keys():
                if last_rounds_constructor_data[year] is not None:
                    for constructor in last_rounds_constructor_data[year]:
                        if constructor["Position"] == "1":
                            if constructor["constructorId"] == constructor_info[0]:
                                wcc += 1
                                wcc_year.append(str(year))
                                break
                            else:
                                break

            # Number of drivers' world championships.
            wdc = 0
            wdc_year = []
            for year in last_rounds_driver_data.keys():
                if last_rounds_driver_data[year] is not None:
                    for driver in last_rounds_driver_data[year]:
                        if driver["Position"] == "1":

                            team_id = (glob_vars.driver_team[last_rounds[year][0]]).get(driver["driverId"])
                            # If the driver did not participate in the last race, we look at the previous ones.
                            n=1
                            while team_id is None:
                                team_id = (glob_vars.driver_team[str(int(last_rounds[year][0])-n)]).get(driver["driverId"])
                                n+= 1

                            if team_id == constructor_info[0]:
                                wdc += 1
                                wdc_year.append(str(year))
                                break
                            else:
                                break

            # Positions
            pos = list(map(_aux.int_nan, glob_vars.results_constructorId[constructor_info[0]]["Position"]))

            info.update({"Name": constructor_info[1],
                         "Nationality": constructor_info[2],
                         "Races": len(glob_vars.results_constructorId_points[constructor_info[0]].get("Points")), #Total number of races
                         "WCCs": wcc,   #Number of world constructors' championships
                         "WDCs": wdc,
                         "Wins": glob_vars.results_constructorId[constructor_info[0]]["Position"].count("1"), #Number of wins
                         "Podiums": len(list(filter(lambda x: x <=3, pos))), #Number of podiums
                         "Poles": glob_vars.results_constructorId[constructor_info[0]]["Grid"].count("1"), #Total number of pole positions
                         "Points": np.nansum(list(map(_aux.float_nan, glob_vars.results_constructorId_points[constructor_info[0]].get("Points")))), #Total number of points
                         #"Points2": np.nansum(list(map(_aux.float_nan, glob_vars.results_constructorId[constructor_info[0]].get("Points")))), #Total number of points
                         "Fastest laps": glob_vars.results_constructorId[constructor_info[0]]["Rank"].count("1")  #Total number of fastest laps
                        })

            table.append(info)

    if len(table) == 1:
        print(f"\nThe {table[0]["Nationality"]} team {table[0]["Name"]} has won "
              f"{p.number_to_words(int(table[0]["WCCs"]), threshold = 10)} "
              f"World Constructors' {p.plural("Championship", table[0]["WCCs"])} ({p.join(wcc_year)}) "
              f"and {p.number_to_words(int(table[0]["WDCs"]), threshold = 10)} "
              f"World Drivers' {p.plural("Championship", table[0]["WDCs"])} ({p.join(wdc_year)}).\n"
              f"{table[0]["Name"]} has participated in "
              f"{p.number_to_words(int(table[0]["Races"]), threshold = 10)} "
              f"{p.plural("race", table[0]["Races"])} "
              f"and has won {p.number_to_words(int(table[0]["Wins"]), threshold = 10)}. \n"
              f"This team has achieved {p.number_to_words(int(table[0]["Podiums"]), threshold = 10)}"
              f" {p.plural("podium", table[0]["Podiums"])}, "
              f"{p.number_to_words(int(table[0]["Poles"]), threshold = 10)} "
              f"{p.plural("pole", table[0]["Poles"])}, "
              f"{p.number_to_words(int(table[0]["Points"]), threshold = 10)} "
              f"{p.plural("point", table[0]["Points"])} and "
              f"{p.number_to_words(int(table[0]["Fastest laps"]), threshold = 10)} "
              f"fastest {p.plural("lap", table[0]["Fastest laps"])}."
             )

         #input("\nPress any key to continue.")
         #teammates(driver_info[0])

    else:
        table = sorted(table, key=lambda x: x["WCCs"], reverse=True)
        print("\n" + tabulate(table, headers = "keys", tablefmt="github"))

    input("\nPress any key to continue.")




