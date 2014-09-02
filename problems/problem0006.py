sum_of_squared = sum([x**2 for x in range(1, 101)])
squared_sum = sum([x for x in range(1, 101)])**2

print squared_sum - sum_of_squared
