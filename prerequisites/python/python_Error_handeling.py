try:
    print(m)
except:
    print("Error!")

print()

n = 3
try:
    print(n)
except:
    print("Error!")
else:
    print("No Errors!")
finally:
    print("The \"the try expect is finished\" ")


try:
    z = "10"
    z *= z
    print(z)
except NameError:
    print("Name Error")
except:
    print("Error!")


try:
    print(f)
except NameError as err:
    print(err)
except Exception as err:
    print(err)



raise Exception('sorry! Crashed')
