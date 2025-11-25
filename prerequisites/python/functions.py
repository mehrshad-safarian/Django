# A function is a block of code that only runs when it is called.
# You can pass data to a function using parameters.
# A function can use these parameters to perform any calculations
# or actions it needs to do.
# A function can also return data if necessary.

import time

# Define a function that takes one normal parameter 'cc'
# and any number of extra arguments using *args
def my_func(cc, *args):
    # Print the first value with the text IRAN
    print(f"IRAN{cc}")
    
    # Loop through all additional arguments in *args
    for n in args:
        # Print each argument with the text IRAN
        print(f"IRAN {n}")

# Call the function with one main parameter and two extra arguments
my_func(" ZAMIN", "SHAHR", "MALL")


def my_func(fname, lname):
    print(f"Drood {fname} {lname}")
my_func("Iran","Irani")

# Define a function that takes one normal parameter 'fname'
# and any number of keyword arguments using **kwargs
def my_func(fname, **kwargs):
    # Print a greeting using 'fname' and the keyword argument 'lname'
    print(f"Drood {fname} {kwargs['lname']}")

# Call the function using keyword arguments for both parameters
my_func(fname="Iran", lname="Irani")

# Get base number from user first
base = int(input("Please enter your base number: "))
# Get exponent (power) from user
power = int(input("Please enter your exponent (power) number: "))
# Define function to calculate base^power
def my_func1(x, y):
    print("calculating...")
    time.sleep(5)
    return x ** y
# Call the function and store the result
result = my_func1(base, power)
# Print the result
print("Result: {}".format(result))

def my_func(x):
    pass


"""
1) *args کی استفاده میشه؟
وقتی نمی‌دونی چند تا ورودی معمولی (بدون اسم) قرار هست به تابع داده بشه.
مثال:
def add_numbers(*args):
    for n in args:
        print(n)

فراخوانی:
add_numbers(10, 20, 30, 40)

چه اتفاقی میفته؟
همه ورودی‌ها به صورت tuple می‌رن داخل args
مناسب وقتی تعداد پارامترها نامشخص باشه
به درد لیست ورودی‌های متعدد بدون اسم می‌خوره.

2)**kwargs کی استفاده میشه؟
وقتی نمی‌دونی چند تا ورودی با اسم (keyword arguments) قرار هست وارد تابع بشه.
مثال:
def user_info(**kwargs):
    print(kwargs)

فراخوانی:
user_info(name="Ali", age=20, city="Tehran")

چه اتفاقی میفته؟
ورودی‌ها به صورت یک دیکشنری ذخیره می‌شن
کلیدها همون اسم پارامترها هستن
وقتی ورودی‌ها باید اسم‌دار باشن و بخوای کلید–مقدار داشته باشی.

جمع‌بندی خیلی کوتاه
*args = ورودی‌های متعدد بدون اسم → tuple
مثال: func(1, 2, 3, 4)

**kwargs = ورودی‌های متعدد با اسم → dict
مثال: func(name="Ali", age=30)"""