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
    
    
    #line1 = linregress(sealevel['Year'], sealevel['CSIRO Adjusted Sea Level'])
    year = np.arange(sealevel['Year'].min(), 2051, 1)
    #level = year*line1.slope + line1.intercept
    res = linregress(sealevel['Year'], sealevel['CSIRO Adjusted Sea Level'])
    
    plt.plot(year, res.intercept + res.slope* year, 'r')
    '''
    
    line1 = linregress(sealevel['Year'],
                sealevel['CSIRO Adjusted Sea Level'])
    plt.plot(sealevel['Year'], line1.intercept + line1.slope*sealevel['Year'], 'r')
    '''
    # Create second line of best fit
    sealevel2000 = sealevel[sealevel['Year']>=2000]
    
    line2 = linregress(sealevel2000['Year'], sealevel2000['CSIRO Adjusted Sea Level'])
    year2 = np.arange(sealevel2000['Year'].min(), 2051, 1)
    level2 = year2*line2.slope + line2.intercept
    
    plt.plot(year2, level2)
    
    
    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
