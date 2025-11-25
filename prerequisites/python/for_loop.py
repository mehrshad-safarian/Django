fruits = ["kiwi", "pineapple", "appel", "orange"]

for x in "Mehrshad":
    print(x)
    if (x == 'h'):
        break
print()
# 'break' stops the loop immediately.
# When 'break' runs, the loop ends right away.
# The program continues from the first line after the loop.

for x in 'Mehrshad':
    if (x == 'h'):
        continue
    print(x)
# 'continue' skips the rest of the current loop iteration.
# It does not stop the loop; it just jumps to the next iteration.
# Any code after 'continue' in the loop will not run for that turn.
print(range(7))
for x in range(7):
    print(f"\4\t{x}")

for x in fruits:
    print(x)
else:
    print("Finished!")