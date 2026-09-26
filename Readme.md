"""
astro_helper.py
 
A small toolkit for analyzing star brightness (magnitude) data.
Part of Project #63 — Astronomy Data Analysis Helper Program.
"""
 
import numpy as np
 
 
def mean_magnitude(data):
    """
    Calculate the average (mean) magnitude of a set of stars.
 
    Parameters
    ----------
    data : array-like
        A list or NumPy array of star magnitudes.
 
    Returns
    -------
    float
        The mean magnitude.
    """
    # TODO: implement using np.mean()
    pass
 
 
def median_magnitude(data):
    """
    Calculate the median magnitude of a set of stars.
 
    Parameters
    ----------
    data : array-like
        A list or NumPy array of star magnitudes.
 
    Returns
    -------
    float
        The median magnitude.
    """
    # TODO: implement using np.median()
    pass
 
 
def magnitude_range(data):
    """
    Calculate the range (max - min) of star magnitudes.
 
    Parameters
    ----------
    data : array-like
        A list or NumPy array of star magnitudes.
 
    Returns
    -------
    float
        The difference between the highest and lowest magnitude.
    """
    # TODO: implement using np.max() and np.min()
    pass
 
 
def relative_brightness_ratio(m1, m2):
    """
    Calculate how much brighter one star is compared to another,
    using the standard magnitude-to-brightness relation.
 
    Parameters
    ----------
    m1 : float
        Magnitude of the first star.
    m2 : float
        Magnitude of the second star.
 
    Returns
    -------
    float
        The brightness ratio between the two stars.
        (Formula: ratio = 10 ** (0.4 * (m2 - m1)))
    """
    # TODO: implement the magnitude ratio formula
    pass
 
 
def find_brightest(data):
    """
    Identify the brightest star in the dataset.
    Note: a LOWER magnitude means a BRIGHTER star.
 
    Parameters
    ----------
    data : array-like
        A list or NumPy array of star magnitudes.
 
    Returns
    -------
    float
        The magnitude value of the brightest star (the minimum value).
    """
    # TODO: implement using np.min()
    pass
 
 
if __name__ == "__main__":
    # Quick manual test — replace with real data later
    sample_data = [4.2, 3.8, 5.1, 2.9, 4.7]
 
    print("Mean:", mean_magnitude(sample_data))
    print("Median:", median_magnitude(sample_data))
    print("Range:", magnitude_range(sample_data))
    print("Brightest:", find_brightest(sample_data))
    print("Ratio (star1 vs star2):", relative_brightness_ratio(sample_data[0], sample_data[1]))