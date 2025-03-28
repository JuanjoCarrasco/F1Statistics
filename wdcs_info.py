"""Processes data of the world champions."""

# Import libraries.
import glob_vars
import _aux
import find_last_rounds
from tabulate import tabulate
from dateutil.relativedelta import relativedelta
from datetime import date

def show(order_by):
    
    # Final standings of each driver by season
    last_rounds, last_rounds_driver_data, _ = find_last_rounds.find_lr()

    # World Drivers' Champions by season data
    table = []
    champion_drivers = []
    for year in last_rounds_driver_data.keys():
        if last_rounds_driver_data[year] is not None:
            for driver in last_rounds_driver_data[year]:
                if driver["Position"] == "1":

                    driver_id = driver["driverId"]
                    winner = f'{glob_vars.drivers_info[driver_id]["Forename"]} {glob_vars.drivers_info[driver_id]["Surname"]}'
                    champion_drivers.append(winner)

                    age = relativedelta(date.fromisoformat(glob_vars.races[last_rounds[year][0]]["Date"]),
                                        date.fromisoformat(glob_vars.drivers_info[driver_id]["Date of birth"])).years

                    team_id = (glob_vars.driver_team[last_rounds[year][0]]).get(driver_id)

                    # If the driver did not participate in the last race, we look the team at the previous ones.
                    n=1
                    while team_id is None:
                        team_id = (glob_vars.driver_team[str(int(last_rounds[year][0])-n)]).get(driver_id)
                        n+= 1

                    team = glob_vars.constructors_info[team_id]["Name"]

                    wins = _aux.int_nan(driver["Wins"])
                    points = _aux.float_nan(driver["Points"])
                    total_points = _aux.int_nan(glob_vars.scoring[str(year)]['Max points'])

                    info = {"Season": year,
                            "Races": last_rounds[year][1],
                            "Winner": winner,
                            "Age": age,
                            "Team": team,
                            "Wins":  wins,
                            "W rate (%)": wins / last_rounds[year][1] * 100,
                            "Points": points,
                            "P rate (%)": points / total_points * 100
                            }

                elif driver["Position"] == "2":
                    points_2nd = _aux.float_nan(driver["Points"])

            info["P with 2nd"] = points - points_2nd
            table.append(info)

    print("\nFormula One World Drivers' Champions by season\n")
    # Data sorted by the selected variable.
    table = sorted(table, key=lambda x: x[order_by], reverse=True)

    #Data in table format with tabulate.
    print(tabulate(table, headers="keys", tablefmt="github", floatfmt=".1f")) # maxcolwidths=[None, 8]
    input("\nPress any key to continue.")

    return ", ".join(set(champion_drivers))
