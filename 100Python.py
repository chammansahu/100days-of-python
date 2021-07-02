#12create script that converts ranges into list of item multiplied by 10

from collections import OrderedDict
r = range(1,10)
ls = [10 * item for item in r]
#print(ls)

#13  convert range into strings

ls_string = map(str,ls)
for item in ls_string:
    #print(item)

#remove duplicates from list 
 a=[1,1,12,2,2,3,4,5,5]

a = list(set(a))
#print(a)

#If you want to keep the order, you need OrderedDict
a = ["1", 1, "1", 2]
a = list(OrderedDict.fromkeys(a))
print(a)

#print ascii 
import string

for letter in string.ascii_lowercase:
    print(letter)
