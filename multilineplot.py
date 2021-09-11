import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

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
plt.plot(x_data_1, y_data_1, color=colors[0], marker='o', mfc='white', linestyle='-', label='dataset-1')
plt.plot(x_data_2, y_data_2, color=colors[1], marker='s', mfc='white', linestyle='--', label='dataset-2')
plt.plot(x_data_3, y_data_3, color=colors[2], marker='x', mfc='white', linestyle='-.', label='dataset-3')

plt.xlabel('x label')
plt.ylabel('y label')
plt.legend()

plt.savefig('outputfigs/multilineplot.svg', bbox_inches='tight', format='svg')
plt.savefig('outputfigs/multilineplot.pdf', bbox_inches='tight', format='pdf')
plt.show()