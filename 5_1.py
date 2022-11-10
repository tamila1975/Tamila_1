numbers = [4, 8, 10, 17, 21, 30, 60, 54, 13, 60, 80, 100]
m = 2
k = 6
first_five = [x for x in numbers[::] if x % m == 0 and x > k]
print(first_five[0:5])
