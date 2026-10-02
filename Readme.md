# Astronomy Data Analysis Helper Program

A small Python toolkit for analyzing star brightness (magnitude) data.
Built as Project #63 for the Astronomy & Astrophysics coursework.

## What It Does

This program provides reusable functions to analyze a set of star
magnitudes (brightness values):

- `mean_magnitude(data)` — average magnitude of the dataset
- `median_magnitude(data)` — median magnitude of the dataset
- `magnitude_range(data)` — difference between brightest and dimmest star
- `relative_brightness_ratio(m1, m2)` — how much brighter one star is than another
- `find_brightest(data)` — identifies the brightest star (lowest magnitude)

All functions include input validation (empty data raises `ValueError`,
invalid types raise `TypeError`) and are documented with docstrings.

## Project Structure

```
astro-helper/
├── src/
│   └── astro_helper.py       # Main program with all functions
├── tests/
│   └── test_astro_helper.py  # Test cases for every function
├── data/
│   └── sample_stars.csv      # Sample dataset (star name + magnitude)
└── README.md
```

## How to Run

1. Make sure Python 3 and NumPy are installed:
   ```bash
   pip install numpy
   ```

2. Run the main program (uses the sample dataset by default):
   ```bash
   cd src
   python astro_helper.py
   ```

3. Run the test suite to verify everything works:
   ```bash
   cd tests
   python test_astro_helper.py
   ```
   Expected output: `All tests passed!`

## Example Usage

```python
from astro_helper import mean_magnitude, find_brightest, relative_brightness_ratio

stars = [4.2, 3.8, 5.1, 2.9, 4.7]

print(mean_magnitude(stars))              # average brightness
print(find_brightest(stars))              # brightest star's magnitude
print(relative_brightness_ratio(4.2, 3.8)) # how much brighter star2 is than star1
```

## How to Reuse This Program

- Replace `data/sample_stars.csv` with your own dataset (same two columns:
  `star_name,magnitude`) and it will work automatically.
- Import any function individually into your own script using
  `from astro_helper import <function_name>`.
- All functions accept both Python lists and NumPy arrays as input.

## Notes

- A **lower magnitude** value means a **brighter** star (astronomical
  magnitude scale is reversed and logarithmic).
- The sample dataset used here contains real bright stars (Sirius, Vega,
  Betelgeuse, etc.) with their actual approximate magnitudes.

## Author

Mohammad Rohaan
Naura Sarfaraz
