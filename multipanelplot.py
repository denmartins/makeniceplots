import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

# Check ColorBrew (https://colorbrewer2.org) for nice, colorblind-friendly colors
colors = ['#2b8cbe', '#7bccc4', '#238b45']

# Set global matplotlib parameters
mpl.rcParams['lines.linewidth'] = 1.2
mpl.rcParams['lines.markersize'] = 6
mpl.rcParams['font.size'] = 14

# Remove plot edges
mpl.rcParams['axes.spines.right'] = False
mpl.rcParams['axes.spines.top'] = False

mpl.rcParams['axes.grid'] = True
mpl.rcParams['axes.grid.axis'] = 'y'
mpl.rcParams['grid.alpha'] = 0.3

# Use LaTeX-friendly font
mpl.rcParams['font.family'] = 'TeX Gyre Termes'
mpl.rcParams["mathtext.fontset"] = "stix"

x_data_1 = np.arange(0, 101, 10)
y_data_1 = x_data_1 * 50

x_data_2 = np.arange(0, 101, 10)
y_data_2 = x_data_2**2

x_data_3 = np.arange(0, 101, 10)
y_data_3 = x_data_3**2.2

fig = plt.figure(1, figsize=(8, 4.5))

# Create multipanel plot (lines, columns)
gridpanel = gridspec.GridSpec(1, 3)

# Set space between panels
gridpanel.update(wspace=0.2, hspace=0.2)

# First panel
first_subplot = fig.add_subplot(gridpanel[0, 0])
plt.plot(x_data_1, y_data_1, color=colors[0], marker='o', mfc='white', linestyle='-', label='dataset-1')
plt.legend()
plt.ylabel('y label')

# Second panel
second_subplot = fig.add_subplot(gridpanel[0, 1])
plt.plot(x_data_2, y_data_2, color=colors[1], marker='s', mfc='white', linestyle='--', label='dataset-2')
plt.tick_params(labelleft=False) # Turn off ylabels
plt.legend()

# Plot xlabel just for the center panel
plt.xlabel('x label')

# Third panel
third_subplot = fig.add_subplot(gridpanel[0, 2])
plt.plot(x_data_3, y_data_3, color=colors[2], marker='x', mfc='white', linestyle='-.', label='dataset-3')
plt.tick_params(labelleft=False) # Turn off ylabels
plt.legend()

# Show horizontal grid lines only
#plt.grid(axis='y', alpha=.3)

plt.savefig('outputfigs/multipanelplot.svg', bbox_inches='tight', format='svg')
plt.savefig('outputfigs/multipanelplot.pdf', bbox_inches='tight', format='pdf')
plt.show()