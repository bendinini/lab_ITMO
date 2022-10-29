import sys
import math

R = float(input("Введите значение R: "))
x = float(input("Введите значение x: "))

# 1) Значение x в интервале [-3R; -2R]
if -3*R <= x and x <= -2*R:
    y = math.sqrt(R**2 - (x+2*R)**2) * -1

# 2) Значение x в интервале (-2R; -R]
elif -2*R <= x and x <= -R:
    y = x+R

# 3) Значение x в интервале (-R; 0]
elif -R <= x and x <= 0:
    y = math.sqrt(R**2 - x**2)

# 4) Значение x в интервале (0; R]
elif 0 <= x and x <= R:
    y = R-x

# 5) Значение x в интервале (R; 3R]
elif R <= x and x <= 3*R:
    y = (x-R)/(R*2)*R

# 6) В остальных случаях
else:
    print("Значение y неопределено.")
    sys.exit()

print("Значение y: " + str(y) + ".")


