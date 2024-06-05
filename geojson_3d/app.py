import matplotlib.pyplot as plt
import json
from mpl_toolkits.mplot3d import Axes3D

# Load the GeoJSON file
with open("geometry.json") as f:
    json_file = f.read()

    data = json.loads(json_file)

    # Create a new plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    z_offset = 1

    # Plot each polygon in the MultiPolygon
    index = -1
    for polygon in data["coordinates"]:
        index += 1
        # if index != 10:
            # continue

        for linear_ring in polygon:
            x, y, z = zip(*[(point[0], point[1], point[2]) for point in linear_ring])
            ax.plot(x, y, z)
            ax.scatter(x, y, z, color='red')  # Add dots at the location coordinates
        

    # Show the plot
    plt.show()