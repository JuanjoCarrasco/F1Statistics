"""Global variables to store data from .csv files."""


def init_glob_vars():
    """Initialize Global variables."""
    global drivers_info, driver_standings, races, results_driverId, \
        results_raceId, driver_team, status, scoring, constructors_info, \
        constructor_standings, results_constructorId, \
        results_constructorId_points, results_constructor_raceId_points, \
        min_year, max_year

    drivers_info = {}
    driver_standings = {}
    races = {}
    results_driverId = {}
    results_raceId = {}
    driver_team = {}
    status = {}
    scoring = {}
    constructors_info = {}
    constructor_standings = {}
    results_constructorId = {}
    results_constructorId_points = {}
    results_constructor_raceId_points = {}
    min_year = 0
    max_year = 0
