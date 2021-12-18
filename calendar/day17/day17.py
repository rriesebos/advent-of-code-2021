# https://adventofcode.com/2021/day/17

import re


with open('input.txt') as f:
    lines = f.readlines()
    x_min, x_max, y_min, y_max = map(
        int, re.match(r'^.*x=(-?\d+)\.\.(-?\d+), y=(-?\d+)\.\.(-?\d+)$', lines[0].strip()).groups()
    )


# Part 1
# The probe is shot from y = 0 with an initial velocity of v_init. At each step the velocity is decreased by 1.
# This means that the probe is launched to a height of (v_init * (v_init + 1)) / 2 (nth partial sum).
# Consequently, when returning to y = 0, the velocity equals v_init + 1 in the negative y direction (or -(v_init + 1))
# - so at the next step the probe will go to -(v_init + 1). Therefore, the maximum initial velocity (and maximum height)
# is bound by the lower y limit of the target area (y_min), and is given by v_init = |y_min| - 1.
max_y_velocity = abs(y_min) - 1
height = (max_y_velocity * (max_y_velocity + 1)) // 2
print(height)

# Part 2
max_y_velocity = abs(y_min) - 1
count = 0
for x_velocity in range(1, x_max + 1):
    for y_velocity in range(y_min, max_y_velocity + 1):
        x, y = 0, 0
        x_vel = x_velocity
        y_vel = y_velocity
        while x < x_max and y > y_min:
            x += x_vel
            y += y_vel
            x_vel -= x_vel > 0
            y_vel -= 1

            if x_min <= x <= x_max and y_min <= y <= y_max:
                count += 1
                break

print(count)
