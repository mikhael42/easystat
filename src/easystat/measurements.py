"""Statistical functions related to measurements."""

import numpy as np

from easystat.shortcuts import stdev_of_mean


def result_with_uncertainty(values):
    """Return result with uncertainty from list of measurements."""
    return np.mean(values), stdev_of_mean(values)