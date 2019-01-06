"""
Example to show available string methods in python
"""
# Replace Method
a = "1abc2abc3abc"
print(a.replace('abc', 'ABC', 2))

# Sub-Strings
# Starting index is inclusive
# Ending index is excluded
sub = a[2:6]
step = a[1:6:2]

print("****************")
print(sub)
print(step)








