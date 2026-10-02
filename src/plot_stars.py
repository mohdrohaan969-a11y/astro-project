"""
plot_stars.py

Generates visualizations of star brightness data.
Part of Project #63 — Astronomy Data Analysis Helper Program.
"""

import csv
import matplotlib.pyplot as plt


def load_full_data(filepath):
    """
    Load star names, magnitudes, and distances from the CSV file.

    Parameters
    ----------
    filepath : str
        Path to the CSV file.

    Returns
    -------
    tuple of lists
        (star_names, magnitudes, distances)
    """
    names = []
    magnitudes = []
    distances = []
    with open(filepath, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            names.append(row['star_name'])
            magnitudes.append(float(row['magnitude']))
            distances.append(float(row['distance_ly']))
    return names, magnitudes, distances


def plot_magnitude_bar(names, magnitudes, save_path=None):
    """
    Bar chart comparing apparent magnitude across stars.
    Lower bars (more negative) = brighter stars.
    """
    plt.figure(figsize=(12, 6))
    colors = ['gold' if m == min(magnitudes) else 'steelblue' for m in magnitudes]
    plt.bar(names, magnitudes, color=colors)
    plt.axhline(0, color='gray', linewidth=0.8, linestyle='--')
    plt.xlabel("Star Name")
    plt.ylabel("Apparent Magnitude (lower = brighter)")
    plt.title("Apparent Magnitude Comparison of Bright Stars")
    plt.xticks(rotation=60, ha='right')
    plt.gca().invert_yaxis()  # brighter stars (lower mag) appear higher on chart
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=150)
    plt.show()


def plot_magnitude_vs_distance(names, magnitudes, distances, save_path=None):
    """
    Scatter plot: apparent magnitude vs distance from Earth.
    Shows that apparent brightness is not purely about actual (intrinsic) brightness.
    """
    plt.figure(figsize=(10, 7))
    plt.scatter(distances, magnitudes, color='darkorange', s=80, edgecolors='black')

    for i, name in enumerate(names):
        plt.annotate(name, (distances[i], magnitudes[i]),
                     textcoords="offset points", xytext=(5, 5), fontsize=8)

    plt.xscale('log')
    plt.xlabel("Distance from Earth (light-years, log scale)")
    plt.ylabel("Apparent Magnitude (lower = brighter)")
    plt.title("Apparent Magnitude vs Distance")
    plt.gca().invert_yaxis()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=150)
    plt.show()


if __name__ == "__main__":
    names, magnitudes, distances = load_full_data("../data/real_bright_stars.csv")

    plot_magnitude_bar(names, magnitudes, save_path="../data/magnitude_bar_chart.png")
    plot_magnitude_vs_distance(names, magnitudes, distances, save_path="../data/magnitude_vs_distance.png")
