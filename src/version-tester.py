# This script serves as an additional check to see if we have the right version of
# python installed.  Each sections tries to run a feature that will only work in 
# the noted version and beyond. The workflow should truncate any sections that are
# beyond the specified version, and then should run the remaining script without
# errors.
# the following will work for python 3.8 and older
print("This will work on python 3.8 and older")

# the following will work on python 3.9
x = {"key1": "value1 from x", "key2": "value2 from x"}
y = {"key2": "value2 from y", "key3": "value3 from y"}
print(f'This will work on python 3.9 {x | y}')

# the following will work on python 3.10
def square(number: int | float) -> int | float:
    return number ** 2
print(f'This will work on python 3.10: 2 squared is {square(2)}')

# the following will work on python 3.11
import math
print(f'This will work on python 3.11  2^5 = {math.exp2(5)}')

# the following will work on python 3.12
import calendar
october = calendar.Month(10)
print(f'This will work on python 3.12  October is month {october}')
