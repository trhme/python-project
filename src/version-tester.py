# This script serves as an additional check to see if we have the right version of
# python installed.  Each sections tries to run a feature that will only work in 
# the noted version and beyond. The workflow should truncate any sections that are
# beyond the specified version, and then should run the remaining script without
# errors.

print("This will work on python3.8 and older")
# everthing above will work for python 3.8 and older


x = {"key1": "value1 from x", "key2": "value2 from x"}
y = {"key2": "value2 from y", "key3": "value3 from y"}
print(f'This will work on python3.9 {x | y}')
# everthing above will work on python 3.9


def square(number: int | float) -> int | float:
    return number ** 2
print(f'This will work on python3.10: 2 squared is {square(2)}')
# everthing above will work on python 3.10


import math
print(f'This will work on python3.11  2^5 = {math.exp2(5)}')
# everthing above will work on python 3.11


import calendar
october = calendar.Month(10)
print(f'This will work on python3.12  October is month {october}')
# everthing above will work on python 3.12
