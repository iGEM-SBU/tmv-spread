import numpy as np
from scipy.spatial import Delaunay


def check(test, arr):
    return any(np.array_equal(x, test) for x in arr)


def write_link(a, b):
    for p in tri.simplices:
        if not (check([p[a], p[b]], tri.convex_hull) or check([p[b], p[a]], tri.convex_hull)):
            f.write(str(p[a]) + "\n")
            f.write(str(p[b]) + "\n")


points = []

# Generate 300 points separated by a minimum distance of 15 in a 400 * 400 grid
count = 1

# Initialize first point
pt = list(np.random.randint(-200, 200, size=2))
points.append(pt)

while True:
    num_cells = input("Enter the number of cells (50 - 450): ")
    if num_cells.isnumeric():
        num_cells = int(num_cells)
        break
    print("Invalid value.")

while count < num_cells:
    # Try dropping dorn more points
    flag = True
    # Get a trial point
    pt_t = list(np.random.randint(-200, 200, size=2))
    # See how far it is away from existing points
    for point in points:
        distance = ((point[0] - pt_t[0]) ** 2 + (point[1] - pt_t[1]) ** 2) ** 0.5
        if distance < 15:
            flag = False
            break
    if flag:
        count += 1
        points.append(pt_t)

points = np.array(points)
tri = Delaunay(points)

with open("points.txt", "w+") as f:
    for p in points:
        f.write(str(p[0]) + "\n")
        f.write(str(p[1]) + "\n")

with open("links.txt", "w+") as f:
    write_link(0, 1)
    write_link(0, 2)
    write_link(1, 2)
