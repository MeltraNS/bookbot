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
#print(z)
xx = "I ATE AN APPLE THIS MORNING!  YOOOOOOOOOOOO"
yy = xx.lower()
zz = {}
for character in yy:
    if character not in zz and character.isalpha() == True:
        zz[character] = 1
    elif character.isalpha() == False:
        pass
    else:
        zz[character] += 1

w = []
for i in zz:
    w.append((i, zz[i]))
sorted_list = sorted(w, key=lambda v: v[1], reverse=True)
print(sorted_list)
