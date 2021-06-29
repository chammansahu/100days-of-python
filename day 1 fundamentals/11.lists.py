mulist = ['a','b','c','d',False,True,1,2,[1,2,3],4]
#type() len(mulist)

#range of indexes
print(mulist[2:5])
#check i f item exist
if 1 in mulist:
    print("yes its present")
    
#change item
mulist[1]="baanaana"

#change range of
mulist[1:3]=['x','y','z']  
#insert
mulist.insert(5,'value to be inserted')
#append insert at last
mulist.append("chamman")  
mulist.remove("value to be removed from anywhere")
#pop(index)
mulist.pop() #remove last item
mulist.pop(4)
del list #deltes list 
#lsit.clear() emty list

#loop list
for item in mulist:
    print(item)
#Print all items by referring to their index number:
for i in range(len(mulist)):
    print(mulist[i])    
      
#Looping Using List Comprehension

[print(x) for x in mulist]

# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list
