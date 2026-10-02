"""
test_astro_helper.py
 
Test cases for astro_helper.py
Part of Project #63 — Astronomy Data Analysis Helper Program.
"""
 
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
 
from astro_helper import (
    mean_magnitude,
    median_magnitude,
    magnitude_range,
    relative_brightness_ratio,
    find_brightest,
)
 
 
def test_mean_magnitude():
    assert mean_magnitude([1, 2, 3]) == 2.0
    assert mean_magnitude([5, 5, 5]) == 5.0
    assert round(mean_magnitude([1.5, 2.5, 3.0]), 2) == 2.33
    try:
        mean_magnitude([])
        assert False, "Should have raised ValueError"
    except ValueError:
        pass
 
 
def test_median_magnitude():
    assert median_magnitude([1, 2, 3]) == 2.0
    assert median_magnitude([1, 2, 3, 4]) == 2.5
    assert median_magnitude([5]) == 5.0
    try:
        median_magnitude([])
        assert False, "Should have raised ValueError"
    except ValueError:
        pass
 
 
def test_magnitude_range():
    assert magnitude_range([1, 2, 3]) == 2
    assert round(magnitude_range([-1.46, 1.16]), 2) == 2.62
    assert magnitude_range([5, 5, 5]) == 0
    try:
        magnitude_range([])
        assert False, "Should have raised ValueError"
    except ValueError:
        pass
 
 
def test_relative_brightness_ratio():
    assert relative_brightness_ratio(0, 0) == 1.0
    assert round(relative_brightness_ratio(1, 2), 2) == 2.51
    try:
        relative_brightness_ratio("a", 2)
        assert False, "Should have raised TypeError"
    except TypeError:
        pass
 
 
def test_find_brightest():
    assert find_brightest([4.2, 3.8, 5.1, 2.9]) == 2.9
    assert find_brightest([-1.46, 0.5, 1.2]) == -1.46
    try:
        find_brightest([])
        assert False, "Should have raised ValueError"
    except ValueError:
        pass
 
 
if __name__ == "__main__":
    test_mean_magnitude()
    test_median_magnitude()
    test_magnitude_range()
    test_relative_brightness_ratio()
    test_find_brightest()
    print("All tests passed!")
 