# Import, inspect and clear Global Temperatures dataset.
# Save clean dataframe as csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys
from matplotlib.animation import FuncAnimation

# read the dataset
data = pd.read_csv("Global_Temp_var_monthly.txt", delim_whitespace=True, usecols=[0, 1], header=None)
# inspect the dataset
print(data.head())
print(data.tail())
print(data.info())
# drop rows from incomplete year 2020
data = data[:-4]

# split year and month information in separate columns
# rename first column to value
# drop first column
data['year'] = data.iloc[:, 0].apply(lambda x: x.split("/")[0]).astype(int)
data['month'] = data.iloc[:, 0].apply(lambda x: x.split("/")[1]).astype(int)
data = data.rename(columns={1: "value"})
data = data.iloc[:, 1:]
print(data.head())
# set index to month and year columns
data = data.set_index(['year', 'month'])
# calculate mean from 1850 to 1900 as reference, subtract it and reset index back
data -= data.loc[1850:1900].mean()
data = data.reset_index()
print(data.head())
print(data.tail())

# define fig and polar
fig = plt.figure(figsize=(18,18))
ax1 = plt.subplot(111, projection='polar')

# The polar coordinate system is circular and uses r and theta.
# The r coordinate specifies the distance from the center and can range from 0 to infinity.
# The theta coordinate specifies the angle from the origin and can range from 0 to 2*pi.
# ax1.plot(theta, r)

# set background color of the polar to dark grey
ax1.set_facecolor('#dddddd')

# hide the polar grid
ax1.grid(False)

# theta to be x and r to be y
# hide the y-labels
ax1.axes.get_yaxis().set_ticklabels([])

# create list of x-labels
months = [' Jan ', '      Feb ', '      Mar', '      Apr ', '         May ', '         June ', ' July ', 'Aug      ', 'Sep      ', 'Oct      ', 'Nov      ', ' Dec      ']
N = len(months)
# What will be the angle of each axis in the plot? (we divide the plot / number of variable)
angles = [n / float(N) * 2 * np.pi for n in range(N)]
angles += angles[:1]
# Put the first axis to be on top:
ax1.set_theta_offset(np.pi / 2)
ax1.set_theta_direction(-1)
# Draw one axe per variable + add labels labels
plt.xticks(angles[:-1], months, fontfamily='Segoe UI', fontsize='45', color='#343a40')

# define and draw the circles for 1, 1.5 and 2 centigrades Celsius
full_circle_thetas = np.linspace(0, 2*np.pi, 1000)
red_line_one_radii = [2.0]*1000
red_line_two_radii = [2.5]*1000
red_line_three_radii = [3.0]*1000
ax1.plot(full_circle_thetas, red_line_one_radii, c='red')
ax1.plot(full_circle_thetas, red_line_two_radii, c='red')
ax1.plot(full_circle_thetas, red_line_three_radii, c='red')
ax1.text(np.pi*2, 2.0, "1.0 C", color="red", ha='center', fontdict={'fontsize': 45})
ax1.text(np.pi*2, 2.5, "1.5 C", color="red", ha='center', fontdict={'fontsize': 45})
ax1.text(np.pi*2, 3.0, "2.0 C", color="red", ha='center', fontdict={'fontsize': 45})

# define limit of y
ax1.set_ylim(0, 3.25)

# define year text
year_text = ax1.text(0.5, 0.5, "", color="#343a40", ha='center', transform=ax1.transAxes, fontdict={'fontsize': 45})

# create list of the years
years = data['year'].unique()

def init():
    year_text.set_text('')
    return year_text

def update(i):
    '''
    :param i: loop of the list of the years, calculate r and theta, plot them following colo scheme defined,
    and update variable year_text with the year
    :return: year_text
    '''
    year = years[i]
    r = data[data['year'] == year]['value'] + 1 # add 1 to avoid negative values
    theta = np.linspace(0, 2*np.pi, 12)
    ax1.plot(theta, r, c=plt.cm.cool(i*2))
    year_text.set_text(str(year))
    return year_text

# define the animation using function FuncAnimation
anim = FuncAnimation(fig, update, init_func=init, frames=len(years), interval=50, blit=False)
# save animation as a gif, set background color off white ('#f8f9fa')
anim.save('ClimateSpiral.gif', dpi=120, writer='MovieWriter', savefig_kwargs={'facecolor': '#f8f9fa'})
