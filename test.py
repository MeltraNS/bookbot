x = {"apple": 1, "banana": 2, "pear": 3}
y = ["apple", "banana", "pear", "orange"]
#goal: z = {"apple":2,"banana":3,"pear":4."orange":1}
z = {}
for fruit in y:
    if fruit not in x:
        z[fruit] = 1
    else:
        z[fruit] = x[fruit]
        z[fruit] += 1
print(z)
