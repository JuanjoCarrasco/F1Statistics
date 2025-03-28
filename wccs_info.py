"""Data about constructors' champion of each session"""

import find_last_rounds
import glob_vars
import _aux
from tabulate import tabulate

def show(order_by):

    # Final standings of each driver by season
    last_rounds, _, last_rounds_constructor_data = find_last_rounds.find_lr()

    # World Constructors' Champions by season data
    table = []
    champion_constructors = []
    for year in last_rounds_constructor_data.keys():
        if last_rounds_constructor_data[year] is not None:
            for constructor in last_rounds_constructor_data[year]:
                if constructor["Position"] == "1":

                    constructor_id = constructor["constructorId"]
                    winner = glob_vars.constructors_info[constructor_id]["Name"]
                    champion_constructors.append(winner)

                    wins = _aux.int_nan(constructor["Wins"])
                    points = _aux.float_nan(constructor["Points"])
                    total_points = _aux.int_nan(glob_vars.scoring[str(year)]['Max points constructor'])

                    info = {"Season": year,
                            "Races": last_rounds[year][1],
                            "Winner": winner,
                            "Wins":  wins,
                            "W rate (%)": wins / last_rounds[year][1] * 100,
                            "Points": points,
                            "P rate (%)": points / total_points * 100
                            }

                elif constructor["Position"] == "2":
                    points_2nd = _aux.float_nan(constructor["Points"])

            info["P with 2nd"] = points - points_2nd
            table.append(info)

    print("\nFormula One World Constructors' Champions by season\n")
    # Data sorted by the selected variable.
    table = sorted(table, key=lambda x: x[order_by], reverse=True)

    #Data in table format with tabulate.
    print(tabulate(table, headers="keys", tablefmt="github", floatfmt=".1f"))
    input("\nPress any key to continue.")

    return ", ".join(set(champion_constructors))
