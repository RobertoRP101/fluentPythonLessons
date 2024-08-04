x = 'abcdefghijklmnopqrstuvwxyz'
codes = [ord(x) for x in x]
print(x)
print(codes)
codes = [last:= ord(c) for c in x] # Assignment Expressions
print(last)
print(codes)