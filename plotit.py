import matplotlib.pyplot as plt

# Set up the plot
fig, ax = plt.subplots()

# Initialize a list of plots for each player
plots = []

# Iterate through each frame of data
for frame in data:
  playid = frame['playid']
  playerid = frame['playerid']
  frameid = frame['frameid']
  x = frame['x']
  y = frame['y']
  direction = frame['direction']
  degree_of_rotation = frame['degree of rotation']

  # Find the plot for the current player, or create a new one if it doesn't exist
  plot = None
  for p in plots:
    if p['playerid'] == playerid:
      plot = p
      break
  if plot is None:
    plot = {
      'playerid': playerid,
      'x': [],
      'y': []
    }
    plots.append(plot)

  # Add the new data for the current frame to the plot for the current player
  plot['x'].append(x)
  plot['y'].append(y)

  # Clear the previous plots from the plot
  for p in plots:
    p['plot'].set_data([], [])

  # Update the plots with the new data
  for p in plots:
    p['plot'], = ax.plot(p['x'], p['y'], 'o')

# Show the plot
plt.show()
