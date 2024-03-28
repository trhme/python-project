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
print(f'This will work on python 3.11 {isinstance(5, int | str)}')
# the following will work on python 3.12
print(f'This will work on python 3.12 {x['key1']}')
