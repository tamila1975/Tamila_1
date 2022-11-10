n = 100
n1 = [x for x in range(2,n) if x % 2 == 0]
n2 = [n1[i:i+5] for i in range(0, len(n1), 5)]
print(n2)
