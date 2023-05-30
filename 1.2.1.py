objects = [1, 2, 1, 2, 3, True, False, True, False, "true"]
objects1 = []
for i in objects:
    objects1.append(id(i))
print(len(set(objects1)))

