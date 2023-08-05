from operator import truediv


l=[1,2,3,4,5]
print(type(l),l[2])
l=[
    [1,2,3,4],
    ['a','b','c','d'],
    ['!','@','#','$']
   ]
print(l);
print(l[0][0])
print(l[0:2])
print(l[0][0:4:1])
#toreverse
print(l[0][-1::-1])

#create a list of 1 to 100
ml=[]
for a in range(1,101):
    ml.append(a)

print(ml)
evenlist=[h for h in range(1,101) if h%2==0]
print(evenlist)
#del= remove element, pop(index)=remove and return element,remove(value)= remove first matching element 
l1=[1,2,3,4]
l1.pop(2)
print(l1)
l2=[1,2,4,2,5]
l2.remove(2)
print(l2)
l3=[10,20,30]
del l3[1]
print(l3)
#insert(index,value)=insert value at any index,append(value)=append value at end of list,extend(list)=extend a list
m1=[1,2,3]
m1.insert(1,5)
print(m1);
m2=[4,5,6]
m2.append(7);
print(m2)
m3=[7,8,9]
m3.extend(m2)
print(m3)
# list functions are min(),max(),count(),reverse(),index()
#count()=count the occurence of elements in a list
print(l2.count(2))
#max()=find the highest value from list
max_l2=max(l2)
print(max_l2)
#min() get lowest value from list
print(min(l2))
#sort() sort list in acesending order
n1=[1,2,3,5,4]
print(n1)
n1.sort()
print(n1)
#sort(reverse=true) sort list in decending order
n1.sort(reverse=True)
print(n1)
#reverse a list
n1.reverse()
print(n1)
#index() return index no of a element
print(n1.index(2))
