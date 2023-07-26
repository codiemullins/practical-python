# bounce.py
#
# Exercise 1.5
height = 100
bounce = 3 / 5

for i in range(10):
    height = height * bounce
    print(i + 1, round(height, 4))
