x = 10
while x <= 20:
    print(x)
    x += 2
    if x == 18:
        break
print()
y = 5
while y <= 20:
    y += 2
    if y == 17:
        continue
    print(y)
print()

z = 5
while z <= 10:
    print(z)
    z += 1
else:
    print("Finished")
