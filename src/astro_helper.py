"""
astro_helper.py
 
A small toolkit for analyzing star brightness (magnitude) data.
Part of Project #63 — Astronomy Data Analysis Helper Program.
"""
 
import numpy as np
import csv
 
 
def load_data(filepath):
    """
    Load star magnitudes from a CSV file.
 
    Parameters
    ----------
    filepath : str
        Path to the CSV file (must have a 'magnitude' column).
 
    Returns
    -------
    list of float
        The list of magnitude values read from the file.
    """
    magnitudes = []
    with open(filepath, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            magnitudes.append(float(row['magnitude']))
    return magnitudes
 
 
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
    return np.mean(data)
 
 
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
    return np.median(data)
 
 
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
    return np.max(data) - np.min(data)
 
 
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
    return 10 ** (0.4 * (m2 - m1))
 
 
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
    return np.min(data)
 
 
if __name__ == "__main__":
    sample_data = load_data("../data/sample_stars.csv")
 
    print("Mean:", mean_magnitude(sample_data))
    print("Median:", median_magnitude(sample_data))
    print("Range:", magnitude_range(sample_data))
    print("Brightest:", find_brightest(sample_data))
    print("Ratio (star1 vs star2):", relative_brightness_ratio(sample_data[0], sample_data[1]))