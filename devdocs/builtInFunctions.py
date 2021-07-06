import string
# builtins

# abs(9.0)
# all()
# any()
# ascii()
# bin(10)
# chr(119)

ln = list(range(1,10))
lc = [string.ascii_uppercase]

print(chr(223))
print(eval('2+2'))
def isEven(n):
    return n%2==0
filter(isEven,ln)

print(bin(2551231233))
4
print(max(ln))

lsmap = map(lambda x:x**2,ln)
for item in lsmap:
    print(item)
       