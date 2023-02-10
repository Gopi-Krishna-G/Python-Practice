# Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string.
# If the string length is less than 2, return instead of the empty string.

input_string = input("Enter a string ")


def first_last(a):
    """returns first 2 and last 2"""
    if len(a) < 2:
        return
    else:
        print(f'{a[0:2]} {a[-2:]}')


first_last(input_string)
