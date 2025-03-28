"""Drivers data."""

# Import libraries.
import glob_vars
import _aux
import find_last_rounds
import numpy as np
from tabulate import tabulate
from datetime import date
import inflect
import unidecode

p = inflect.engine()

def show(drivers_in):

    drivers_list = []
    for i, name in enumerate(drivers_in.split(",")):
        name = unidecode.unidecode(name.strip().lower())
        if " " in name: # If blank space, the first and last name have been entered
            try:
                forename, surname = name.split(" ")
                forename = unidecode.unidecode(forename.strip().lower())
                surname = unidecode.unidecode(surname.strip().lower())

                drivers_list.append([(driverId, info["Forename"], info["Surname"])
                                      for driverId, info in glob_vars.drivers_info.items()
                                      if forename == unidecode.unidecode(info["Forename"].lower())
                                      and surname == unidecode.unidecode(info["Surname"].lower())
                                      ])
            except (ValueError):
                print(f"{name} not found")

        else:
            drivers_list.append([(driverId, info["Forename"], info["Surname"])
                                  for driverId, info in glob_vars.drivers_info.items()
                                  if name in unidecode.unidecode(info["Forename"].lower())
                                  or name in unidecode.unidecode(info["Surname"].lower())
                                  ])

        if len(drivers_list[i]) == 0:
            print(f"{name} not found")

        elif len(drivers_list[i]) == 1:
            drivers_list[i] = drivers_list[i][0]

        elif len(drivers_list[i]) > 1:
            for j, names_duplicated in enumerate(drivers_list[i], 1):
                print(f"Enter {j} for {names_duplicated[1]} {names_duplicated[2]}") #name and surname
            while True:
                try:
                    sel = int(input("Select: "))
                    if sel < 0:
                        print("Wrong selection")
                    else:
                        drivers_list[i] = drivers_list[i][sel-1]
                        break
                except (ValueError, IndexError):
                    print("Wrong selection")

    if len(drivers_list) == 1 and not drivers_list[0]:
        return

    table = []
    for driver_info in drivers_list:
        if driver_info:
            info = {}
            for key, value in glob_vars.drivers_info[driver_info[0]].items():  # "driverId"
                if key != "DriverRef":
                    info.update({key: value})

            # Number of drivers' world championships.
            _, last_rounds_driver_data, _ = find_last_rounds.find_lr()
            wdc = 0
            wdc_year = []
            for year in last_rounds_driver_data.keys():
                if last_rounds_driver_data[year] is not None:
                    for driver in last_rounds_driver_data[year]:
                        if driver["Position"] == "1":
                            if driver["driverId"] == driver_info[0]:
                                wdc += 1
                                wdc_year.append(str(year))
                                break
                            else:
                                break

            # Positions
            pos = list(map(_aux.int_nan, glob_vars.results_driverId[driver_info[0]]["Position"]))

            info.update({"Races": len(glob_vars.results_driverId[driver_info[0]]["Grid"]), #Total number of races
                         "WDCs": wdc,   #Number of world driver championships
                         "Wins": glob_vars.results_driverId[driver_info[0]]["Position"].count("1"), #Number of wins
                         "Podiums": len(list(filter(lambda x: x <=3, pos))), #Number of podiums
                         "Poles": glob_vars.results_driverId[driver_info[0]]["Grid"].count("1"), #Total number of pole positions
                         "Points": np.nansum(list(map(_aux.float_nan, glob_vars.results_driverId[driver_info[0]]["Points"]))), #Total number of points
                         "Fastest laps": glob_vars.results_driverId[driver_info[0]]["Rank"].count("1")  #Total number of fastest laps
                        })

            table.append(info)

    if len(table) == 1:               
         print(f"\nThe {table[0]["Nationality"]} {table[0]["Forename"]} "  
               f"{table[0]["Surname"]} was born on "
               f"{(date.fromisoformat(table[0]["Date of birth"])).strftime('%B %d, %Y')}.\n"
               f"He has won {p.number_to_words(int(table[0]["WDCs"]), threshold = 10)} "
               f"World Drivers' {p.plural("Championship", table[0]["WDCs"])} ({p.join(wdc_year)}).\n"
               f"{table[0]["Surname"]} has participated in " 
               f"{p.number_to_words(int(table[0]["Races"]), threshold = 10)} "
               f"{p.plural("race", table[0]["Races"])} "
               f"and has won {p.number_to_words(int(table[0]["Wins"]), threshold = 10)}. \n"
               f"He has achieved {p.number_to_words(int(table[0]["Podiums"]), threshold = 10)} "
               f"{p.plural("podium", table[0]["Podiums"])}, "
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
        table = sorted(table, key=lambda x: (x["WDCs"], x["Wins"]), reverse=True)
        print("\n" + tabulate(table, headers = "keys", tablefmt="github"))

    input("\nPress any key to continue.")



def teammates():
    pass



