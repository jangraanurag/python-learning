
#datatypes
#Numeric:Integer,float,complex no
#sequence:List,tuple,string
#Dictionary
#set
#list,dictionary,set are immutable
a=2
b=3.0
c=2+2j
print(a,"is type of",type(a))
print(b,"is type of",type(b))
print(c,"is type of",type(c))
d="I am king";
print(d,"is type of",type(d))
e=''' hjhjhj
hhjhj
hjhjhj
hjhjhj'''
print (e,"is type of",type(e),"with '''")
#list
l=[1,2.0,1+3j,"list"]
print(l,"is type of",type(l))
# tuple
# tuple is like list par koi updation nhi ho sakta
t=(10,20,30)
print(t,type(t))
#dictionary
d={1:"Anurag",2:"Anil"}
print(d,type(d))
print(d[1])
#set
#set only contain unique elements
myset={1,2,3}
print(myset,type(myset))