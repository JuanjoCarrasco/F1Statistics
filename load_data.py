"""load the Formula 1 World Championship data."""

# Import libraries.
import glob_vars
import csv
import sys


def load():
    """Load F1 data from.csv files."""
    # Load drivers data
    try:
        with open("Data/drivers.csv", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                glob_vars.drivers_info[row["driverId"]] = {
                    "DriverRef": row["driverRef"],
                    "Forename": row["forename"],
                    "Surname": row["surname"],
                    "Code": row["code"],
                    "Number": row["number"],
                    "Date of birth": row["dob"],
                    "Nationality": row["nationality"]
                }

    except FileNotFoundError:
        sys.exit("drivers.csv does not exist")

    # Load driver standings
    try:
        with open("Data/driver_standings.csv", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                glob_vars.driver_standings.setdefault(row["raceId"], []).append(
                    {"driverId": row["driverId"],
                     "Points": row["points"],
                     "Position": row["position"],
                     "Wins": row["wins"]
                     })

    except FileNotFoundError:
        sys.exit("driver_standings.csv does not exist")

    # Load races
    try:
        with open("Data/races.csv", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                glob_vars.races[row["raceId"]] = {"Year": row["year"],
                                                  "Round": row["round"],
                                                  "Date": row["date"],
                                                  "Name": row["name"]
                                                  }

        years = set([data["Year"] for data in glob_vars.races.values()])
        glob_vars.min_year = int(min(years))
        glob_vars.max_year = int(max(years))

    except FileNotFoundError:
        sys.exit("races.csv does not exist")

    # Load results of races
    try:
        with open("Data/results.csv", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                glob_vars.results_raceId.setdefault(row["raceId"], []).append(
                    {"driverId": row["driverId"],
                     "Constructor_id": row["constructorId"],
                     "Grid": row["grid"],
                     "Position": row["position"],
                     "Pos_order": row["positionOrder"],
                     "Status_id": row["statusId"],
                     "Points": row["points"],
                     "Laps": row["laps"],
                     "Time": row["time"],
                     "Rank": row["rank"]
                     })

                glob_vars.results_driverId.setdefault(
                    row["driverId"], {"Grid": [], "Points": [], "Position": [],
                                      "Rank": []})
                glob_vars.results_driverId[row["driverId"]]["Grid"].append(
                    row["grid"])
                glob_vars.results_driverId[row["driverId"]]["Points"].append(
                    row["points"])
                glob_vars.results_driverId[row["driverId"]]["Position"].append(
                    row["position"])
                glob_vars.results_driverId[row["driverId"]]["Rank"].append(
                    row["rank"])  # Fastests laps

                glob_vars.results_constructorId.setdefault(
                    row["constructorId"], {"Grid": [], "Points": [],
                                           "Position": [], "Rank": []})
                glob_vars.results_constructorId[row["constructorId"]]["Grid"].append(
                    row["grid"])
                glob_vars.results_constructorId[row["constructorId"]]["Points"].append(
                    row["points"])
                glob_vars.results_constructorId[row["constructorId"]]["Position"].append(
                    row["position"])
                glob_vars.results_constructorId[row["constructorId"]]["Rank"].append(
                    row["rank"])  # Fastests laps

                glob_vars.driver_team.setdefault(row["raceId"], {}).update(
                    {row["driverId"]: row["constructorId"]})

    except FileNotFoundError:
        sys.exit("results.csv does not exist")

    # Load status
    try:
        with open("Data/status.csv", encoding="utf-8") as f:
            reader = csv.DictReader(f, delimiter=',')
            for row in reader:
                glob_vars.status[row["statusId"]] = row["status"]

    except FileNotFoundError:
        sys.exit("status.csv does not exist")

    # Load scoring system
    # This file is self-made and is not part of the F1 database.
    # It contains information about the scoring system for each season.
    try:
        with open("Data/scoring_systemsV3.csv", encoding="utf-8") as f:
            reader = csv.DictReader(f, delimiter=';')
            for row in reader:
                glob_vars.scoring[row["Season"]] = {
                    "Max points": row["MaxPoints"],
                    "Max points constructor": row["MaxPointsConstructor"]}

    except FileNotFoundError:
        sys.exit("scoring_systemsV3.csv does not exist")

    # Load constructors info
    try:
        with open("Data/constructors.csv", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                glob_vars.constructors_info[row["constructorId"]] = {
                    "Constructor_ref": row["constructorRef"],
                    "Name": row["name"],
                    "Nationality": row["nationality"],
                }

    except FileNotFoundError:
        sys.exit("constructors.csv does not exist")

    # Load constructors results
    try:
        with open("Data/constructor_results.csv", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                glob_vars.results_constructorId_points.setdefault(
                    row["constructorId"], {"Points": []})
                glob_vars.results_constructorId_points[row["constructorId"]]["Points"].append(
                    row["points"])

                glob_vars.results_constructor_raceId_points.setdefault(row["raceId"], []).append(
                    {"constructor_id": row["constructorId"],
                     "Points": row["points"],
                     })

    except FileNotFoundError:
        sys.exit("constructor_results.csv does not exist")

    # Load constructor standings
    try:
        with open("Data/constructor_standings.csv", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                glob_vars.constructor_standings.setdefault(row["raceId"], []).append(
                    {"constructorId": row["constructorId"],
                     "Points": row["points"],
                     "Position": row["position"],
                     "Wins": row["wins"]
                     })

    except FileNotFoundError:
        sys.exit("constructor_standings.csv does not exist")
