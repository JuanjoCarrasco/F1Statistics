"""Find data about last race of each season"""

import glob_vars
import _aux

def find_lr():
    """Championship results for each driver and constructor by season."""

    # ID and round of races of each season
    rounds_season = {}
    for race_id, value in glob_vars.races.items():
        rounds_season.setdefault(_aux.int_nan(value["Year"]), {}).update({race_id: _aux.int_nan(value["Round"])})

    # ID and round of the last race of each season
    last_rounds = {year: max(rounds.items(), key=lambda x: x[1]) for year, rounds in rounds_season.items()}

    # Final standings of each driver by season
    last_rounds_driver_data = {year: glob_vars.driver_standings.get(round[0]) for year, round in last_rounds.items()}

    # Final standings of each constructor by season
    last_rounds_constructor_data = {year: glob_vars.constructor_standings.get(round[0]) for year, round in last_rounds.items()}

    return last_rounds, last_rounds_driver_data, last_rounds_constructor_data
