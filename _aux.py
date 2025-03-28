"""Auxiliary functions to parse data."""

# Import libraries.
import numpy as np

def int_nan(s):
    """This function tries to convert a string to an int."""

    try:
        i = int(s)
    except ValueError:
        i = np.nan
    return i


def float_nan(s):
    """This function tries to convert a string to a float."""
    try:
        i = float(s)
    except ValueError:
        i = np.nan
    return i
