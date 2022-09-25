import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    sealevel = pd.read_csv('sea-level-predictor\epa-sea-level.csv')
    
    # Create scatter plot
    plt.scatter(sealevel['Year'],
                sealevel['CSIRO Adjusted Sea Level'])
    
    # Create first line of best fit
    line1 = linregress(sealevel['Year'], sealevel['CSIRO Adjusted Sea Level'])
    year = np.arange(sealevel['Year'].min(), 2050, 1)
    level = year*line1.slope + line1.intercept
    
    plt.plot(year, level)
    # Create second line of best fit


    # Add labels and title

    plt.show()
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

draw_plot()