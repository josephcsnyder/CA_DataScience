# simple linear regression project
# start by entering your datapoints below

datapoints = [(1, 2), (2, 0), (3, 4), (4, 4), (5, 3)]

slope_max = 100
slope_min = -100
slope_step_size = 0.01

intercept_max = 200
intercept_min = -200
intercept_step_size = 0.01

possible_ms = [number * slope_step_size for number in range(slope_min, slope_max + 1)]
possible_bs = [number * intercept_step_size for number in range(intercept_min, intercept_max + 1)]


def get_y(m, b, x):
    y = m * x + b
    return y


def calculate_error(m, b, point):
    x_point, y_point = point
    y = get_y(m, b, x_point)
    difference_y = (y - y_point)
    distance = abs(difference_y)
    return distance


def calculate_all_error(m, b, point):
    total_error = 0
    for point in datapoints:
        error = calculate_error(m, b, point)
        total_error += error
    return total_error


smallest_error = (float("inf"))
best_m = 0
best_b = 0

for m in possible_ms:
    for b in possible_bs:
        error = calculate_all_error(m, b, datapoints)
        if error < smallest_error:
            best_m = m
            best_b = b
            smallest_error = error

print("Best fit slope (m): " + str(best_m))
print("Best fit intercept (b): " + str(best_b))
print("Returned 'best fit' error: " + str(smallest_error))
