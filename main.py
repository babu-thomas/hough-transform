import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("input.png")
cv2.imshow("img", img)
img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("img_grey", img_grey)

lines = cv2.HoughLines(img_grey, 1, np.pi/180, 200)

rho_vals = []
theta_vals = []

for x in range(0, len(lines)):
    for rho, theta in lines[x]:
        rho_vals.append(rho)
        theta_vals.append(np.rad2deg(theta))
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = rho * a
        y0 = rho * b
        x1 = int(x0 + 1000 * -b)
        y1 = int(y0 + 1000 * a)
        x2 = int(x0 - 1000 * -b)
        y2 = int(y0 - 1000 * a)
        cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

cv2.imshow("img_lines", img)
cv2.waitKey(0)
