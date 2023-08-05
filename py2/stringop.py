w="welcome to python"
#print 6th character from start or left
print(w[6])
#print first character from right or end
print(w[-1])
#print a range
print(w[0:7])
#print all after a index
print(w[4:])
#print with increment
print(w[4::2])
print(w[4:8:2])
#right slicing
print(w[-1::-1])
print(len(w))
#range(start index:value to reach:increment)
for a in range(len(w)-1,-1,-1):
    print(a,":",w[a])
for a in w:
    print(a)

n=w.lower()
print(n)
m=w.upper()
print(m)
o=w.capitalize()
print(o)
#capitalize every letter after non alpha char
txt = "hello b2b2b2 and 3g3g3g"

x = txt.title()

print(x)
#find(char,startpos) or find(char)
print(w.find('e',2))
#index(char,startpos) or index(char)
#index return error if value not found but find return -1
print(w.index('e',2))
#isalpha() return true if all are apha bets else return false
w1="welcome"
print(w.isalpha(),w1.isalpha())
#isalnum() is all alphha numeric only
print(w.isalnum(),w1.isalnum())
#isdigit() true if contain only no
print(w.isdigit(),"234".isdigit())
#chr(int) return ascii char
print(chr(65),type(chr(65)))
#ord(unicode char) return integer
print(ord('A')) 
txt1="{0}{1} welcomes {2}".format("Anurag","Jangra","Python")
txt2="{fname}{lname} welcomes {lang}".format(fname="Anurag",lname="Jangra",lang="Python")
txt3="{}{} welcomes {}".format("Anurag","Jangra","Python")


print(txt1,txt2,txt3)
#print lname in left of 20 character
txt4="{fname}{lname:20} welcomes {lang}".format(fname="Anurag",lname="Jangra",lang="Python")
print(txt4)
#print lname at center of 20 chars
txt5="{fname}{lname:^20} welcomes {lang}".format(fname="Anurag",lname="Jangra",lang="Python")
print(txt5)
#print  lname right of 20chars 
txt6="{fname}{lname:>20} welcomes {lang}".format(fname="Anurag",lname="Jangra",lang="Python")
print(txt6)