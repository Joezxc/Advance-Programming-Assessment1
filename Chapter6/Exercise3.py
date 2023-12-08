import matplotlib.pyplot as plt

# Create a figure and axis
fig, ax = plt.subplots()

# Draw the solid line
ax.plot([1, 6], [2, 8], 'b-')

# Draw the dotted line
ax.plot([1, 2, 6, 8], [3, 8, 1, 10], 'r--')

# Show the plot
plt.show()