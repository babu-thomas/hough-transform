import cv2
import numpy as np
from matplotlib import pyplot as plt


def get_edge_points(img):
    dims = img.shape
    edge_points = []
    for x in range(dims[0]):
        for y in range(dims[1]):
            if(img[x][y] == 255):
                edge_points.append((x, y))
    return edge_points

def graph(formula, x_range):
    x = np.array(x_range)
    y = formula(x)
    plt.plot(x, y)

def hough_space_curve(x, y):
    return lambda theta: x * np.cos(theta) + y * np.sin(theta)

img = cv2.imread("input.png")
cv2.imshow("img", img)
img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("img_grey", img_grey)

edge_points = get_edge_points(img_grey)
lines = cv2.HoughLines(img_grey, 1, np.pi/180, 200)

rho_vals = []
theta_vals = []

for i in range(0, len(lines)):
    for rho, theta in lines[i]:
        rho_vals.append(rho)
        theta_vals.append(theta)
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = rho * a
        y0 = rho * b
        x1 = int(x0 + 1000 * -b)
        y1 = int(y0 + 1000 * a)
        x2 = int(x0 - 1000 * -b)
        y2 = int(y0 - 1000 * a)
        cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

for x, y in edge_points:
    graph(hough_space_curve(x, y), np.arange(-10, 10))

plt.show()
cv2.imshow("img_lines", img)
cv2.waitKey(0)
