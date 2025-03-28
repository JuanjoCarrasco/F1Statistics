"""Data about selected season."""

# Import libraries.
import glob_vars
import _aux
from tabulate import tabulate

def show(season):

    # Poles and fast laps por each driver in the season
    results_driver = {}
    last_race_contested = {"Race_id" : season[-1][0], "Year": season[-1][1]["Year"], "Rounds": len(season), "Round": len(season), "Name": ""}

    for n, race in enumerate(season):
        race_id = race[0]
        results_race = glob_vars.results_raceId.get(race_id)
        if results_race:
            for result in results_race:
                results_driver.setdefault(result["driverId"], {"Position": [], "Grid": [], "Rank": []})
                results_driver[result["driverId"]]["Position"].append(result["Position"])
                results_driver[result["driverId"]]["Grid"].append(result["Grid"])
                results_driver[result["driverId"]]["Rank"].append(result["Rank"])
        else:
            # If there is no data, we take the results up to the previous race.
            last_race_contested["Race_id"] = season[n-1][0]
            last_race_contested["Round"] = int(season[n-1][1]["Round"])
            last_race_contested["Name"] = season[n-1][1]["Name"]
            break

    # Final standings
    race_id = last_race_contested["Race_id"]
    round = last_race_contested["Round"]
    last_standings = glob_vars.driver_standings.get(race_id)

    table = []
    for standing in last_standings:
        driver_id = standing["driverId"]
        team_id = glob_vars.driver_team[race_id].get(driver_id)

        # If the driver did not participate in the last race, we look the team at the previous ones.
        while team_id is None:
            team_id = glob_vars.driver_team[season[round-1][0]].get(driver_id)
            round -= 1

        #Number of podiums
        pos = list(map(_aux.int_nan, results_driver[driver_id]["Position"]))

        info = {"Pos": standing["Position"],
                "Driver": glob_vars.drivers_info[driver_id]["Forename"] + " " + glob_vars.drivers_info[driver_id]["Surname"],
                "Team": glob_vars.constructors_info[team_id]["Name"],
                "Points": standing["Points"],
                "Wins": standing["Wins"],
                "Podiums": len(list(filter(lambda x: x <=3, pos))),
                "Poles": results_driver[driver_id]["Grid"].count("1"),
                "Fastest laps": results_driver[driver_id]["Rank"].count("1")
                }

        table.append(info)

    # Data sorted by position.
    table = sorted(table, key=lambda x: int(x["Pos"]), reverse=False)

    # Data in table format with tabulate.
    if last_race_contested["Round"] < last_race_contested["Rounds"]:
        print(f"\nSeason {last_race_contested["Year"]} not finished yet or not data available."
              f"\nResults until the {last_race_contested["Name"]} (round {last_race_contested["Round"]} of {last_race_contested["Rounds"]})\n")
    else:
        print(f"\nFinal results for the {season[0][1]["Year"]} season.\n")

    print(tabulate(table, headers="keys", tablefmt="github", floatfmt=".1f"))

    input("\nPress any key to continue.")

