"""Data about races."""

# Import libraries.
import glob_vars
from tabulate import tabulate

def show(race_selec, season):

    match race_selec:
        case race_selec if race_selec > 0 and race_selec <= len(season):
            race_id = season[race_selec-1][0]
            results_race = glob_vars.results_raceId.get(race_id)
            standings_race = glob_vars.driver_standings.get(race_id)

            if results_race is None:
                print("\nData not available.")
                input("Press any key to continue.")
                return

            table = []
            for result in results_race:
                driver_id = result["driverId"]
                team_id = glob_vars.driver_team[race_id].get(driver_id)
                team = glob_vars.constructors_info[team_id]["Name"]
                wdc_points = [standing["Points"] for standing in standings_race if standing["driverId"] == driver_id]
                wdc_points = wdc_points[0] if wdc_points else "\\N"
                time = result["Time"] if result["Time"] != "\\N" else glob_vars.status[result["Status_id"]]

                info = {"Pos": result["Pos_order"],
                        "Driver": glob_vars.drivers_info[driver_id]["Forename"] + " " + glob_vars.drivers_info[driver_id]["Surname"],
                        "Team": team,
                        "Laps": result["Laps"],
                        "Time": time,
                        "Grid": result["Grid"],
                        "Points": result["Points"],
                        "WDC points": wdc_points
                        }

                table.append(info)

            # Data sorted by position.
            table = sorted(table, key=lambda x: int(x["Pos"]), reverse=False)

            # Data in table format with tabulate.
            print(f"\nResults of {season[race_selec-1][1]["Name"]}.\n")
            print(tabulate(table, headers="keys", tablefmt="github", floatfmt=".1f"))

            input("\nPress any key to continue.")

        case _:
            print("\nWrong selection.")
