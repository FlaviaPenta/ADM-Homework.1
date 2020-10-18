#!/usr/bin/env python
# coding: utf-8

# In[1]:


#########################-----------HOMEWORKS 1-----------##################################


# In[ ]:


#######################-----INTRODUCTION excercise-----------###########################


# In[ ]:


#SAY 'HELLO WORLD' WITH PYTHON

if __name__ == '__main__':
    my_string = "Hello, World!"
    print(my_string)


# In[ ]:


#PYTHON IF-ELSE

if __name__ == '__main__':
    n = int(raw_input().strip())

    if n%2 != 0:
        print('Weird')
    else:
        if n >=2 and n<=5:
            print('Not Weird')
        if n >=6 and n<=20:
            print('Weird')
        if n>20:
            print('Not Weird')


# In[ ]:


#ARITHMETIC OPERATOR

if __name__ == '__main__':
    a = int(raw_input())
    b = int(raw_input())

    print(a+b)
    print(a-b)
    print(a*b)


# In[ ]:


#PYTHON: DIVISION

from __future__ import division

if __name__ == '__main__':
    a = int(raw_input())
    b = int(raw_input())
    print(a//b)
    print(a/b)


# In[ ]:


#LOOPS

if __name__ == '__main__':
    n = int(raw_input())
    for i in range(n):
        print(i*i)


# In[ ]:


#WRITE A FUNCTION

def is_leap(year):
    leap = False
    if year%400==0:
        leap=True
    if year%400!=0:
        if year%100==0:
            leap=False
        if year%100!=0:
            if year%4==0:
                leap=True 
    
    return leap


# In[ ]:


#PRINT FUNCTION

from __future__ import print_function

if __name__ == '__main__':
    n = int(raw_input())
    s=''
    for i in range(1,n+1):
        s=s+str(i)
    print(s)


# In[ ]:


#############################--------------DATA TYPES excercises--------------###############################


# In[ ]:


#LIST COMPREHENSIONS


if __name__ == '__main__':
    l=[]
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

        
    for i in range(x+1):
        for j in range (y+1):
            for k in range (z+1):
                if ((i+j+k)<n or (i+j+k)>n) and ([i,j,k] not in l):
                    l.append([i,j,k])

           
    print(l)


# In[ ]:


#FIND THE RUNNER-UP SCORE!

if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, input().split())
l=[]
for i in arr:
    l.append(i)
l.sort()
h=[]
for i in l:
    if i not in h:
        h.append(i)
print(h[-2])


# In[ ]:


#NESTED LISTS

if __name__ == '__main__':
    
    diz={}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        diz[name]=score
    punteggi=diz.values()
    punteggi.sort()
    l=[]
    for i in punteggi:
        if i not in l:
            l.append(i)
    a=l[1]
    tuple1=diz.items()
    tuple1.sort()
    diz=dict(tuple1)
    for key in diz:
        if diz[key]==a:
            print(key)


# In[ ]:


#FINDING THE PERCENTAGE

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        line = input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = input()
    lista=student_marks[query_name]
    somma=0
    for i in lista:
        somma=somma+i
    media=format((somma/3),'.2f')
    print(media)


# In[ ]:


#LISTS

if __name__ == '__main__':
    N = int(input())
    l=[]
    for i in range(N):
        comando=input().split()
        
        
        if comando[0]=='insert':
            l.insert(int(comando[1]),int(comando[2]))
        if comando[0]=='print':
            print(l)
        if comando[0]=='remove':
            l.remove(int(comando[1]))
        if comando[0]=='append':
            l.append(int(comando[1]))
        if comando[0]=='sort':
            l.sort()
        if comando[0]=='pop':
            l.pop(int(len(l)-1))
        if comando[0]=='reverse':
            l.reverse()


# In[ ]:


#TUPLES

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    print(hash(tuple(integer_list)))


# In[ ]:


#######################---------------STRING excercise------------------######################


# In[ ]:


#sWAP cASE

def swap_case(s):
    stringa=''
    for i in s:
        if i.isupper()== True:
            i=i.lower()
            stringa=stringa+i

        else:
            i=i.upper()
            stringa=stringa+i
    return stringa


# In[ ]:


#STRING SPLIT AND JOIN

def split_and_join(line):
    return line.replace(' ', '-')


# In[ ]:


#WHAT'S YOUR NAME?

def print_full_name(a, b):
    print('Hello '+a+' '+b+'! You just delved into python.')


# In[ ]:


#MUTATIONS

def mutate_string(string, position, character):
    l=[]
    for i in string:
        l.append(i)
    l[position]=character
    return "".join(l)


# In[ ]:


#FIND A STRING

def count_substring(string, sub_string):
    count=0
    for i in range(len(string)):
        if string[i:].startswith(sub_string)==True:
            count=count+1

    return count


# In[ ]:


#STRING VALIDATORS

if __name__ == '__main__':
    s = input()
    a=False
    b=False
    c=False
    d=False
    e=False
    for i in s:
        if i.isalnum()==True:
            a=True  
        if i.isalpha()==True:
            b=True 
        if i.isdigit()==True:
            c=True
        if i.islower()==True:
            d=True 
        if i.isupper()==True:
            e=True
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)


# In[ ]:


#TEXT ALIGNMENT

lung=input()
lung=int(lung)


#for the top
s='H'
for i in range(lung):
    
    print((s*i).rjust(lung-1)+s+(s*i).ljust(lung-1))
    

#PER IL CORPO
for i in range(lung+1):
    print((s*lung).center(lung*2)+(s*lung).center(lung*6))

#metà
for i in range((lung+1)//2):
    print((s*lung*5).center(lung*6))

#PER IL CORPO
for i in range(lung+1):
    duespazi='  '
    print((s*lung).center(lung*2)+(s*lung).center(lung*6))

#per la fine
for i in range(lung):
    print(((s*(lung-1-i)).rjust(lung)+s+(s*(lung-i-1)).ljust(lung)).rjust(lung*6))


# In[ ]:


#TEXT WRAP



def wrap(string, max_width):
    s=''
    for letter in string:
        if len(s)<max_width:
            s=s+letter
        else:
            print(s)
            s=''
            s=s+letter
    return s
        


# In[ ]:


#DESIGNER DOOR MAT

cose=input()
l=cose.split()

altezza=int(l[0])
lunghezza=int(l[1])
s='.|.'
for i in range(1,altezza+1):
    
    if i==((altezza+1)/2):
        print('WELCOME'.center(lunghezza,'-'))
    if i<((altezza+1)/2):
        print(s.center(lunghezza,'-'))
        s=s+'.|.'+'.|.'
    if i>((altezza+1)/2):
        s=s[:-6]
        print(s.center(lunghezza,'-'))


# In[ ]:


#STRING FORMATTING

def print_formatted(number):
    binario=bin(number)[2:]
    lunghezza=len(binario)
    for i in range(1,number+1):
        
        a=bin(i)
        binary=a[2:]
        if oct(i)[0]=='0' or oct(i)[0]=='o':
            octi=oct(i)[1:]
        if oct(i)[1]=='0' or oct(i)[1]=='o':
            octi=oct(i)[2:]
        s=str(hex(i)[2:])
        parola=''
        for j in s:
            if j.isalpha()==True:
                parola=parola+j.upper()
            else:
                parola=parola+j
        print(str(i).rjust(lunghezza)+' '+str(octi).rjust(lunghezza)+' '+parola.rjust(lunghezza)+' '+str(binary.rjust(lunghezza)))


# In[ ]:


#ALPHABET RANGOLI

def print_rangoli(size):
    import string
    alpha = string.ascii_lowercase

    #inizio
    l=[]
    s=alpha[size-1]
    i=0
    stringa='-'
    k=0
    for i in range(1,size+1):
        oper=(size*3)+(size-3)
        stringa=s.center(oper,'-')
        print(stringa)
        s=s[:k+1]+'-'+alpha[size-i-1]+'-'+s[k:]
        l.append(stringa)
        
        k=k+2
    l.pop(-1)
    for i in range(len(l)-1,-1,-1):
        print(l[i])


# In[ ]:


#CAPITALIZE!

# Complete the solve function below.
def solve(s):
    nome=''
    nome=s[0].upper()
    for i in range(1,len(s)):
        if s[i-1]==' ':
            nome=nome+s[i].upper()
        else:
            nome=nome+s[i]
    return nome


# In[ ]:


#THE MINION GAME

def minion_game(string):
    
    
    vowels = 'AEIOU'
    kevsc = 0
    stusc = 0
    for i in range(len(string)):
        if string[i] in vowels:
            kevsc += (len(string)-i)
        else:
            stusc += (len(string)-i)
    if kevsc > stusc:
        print("Kevin", kevsc)
    elif kevsc < stusc:
        print("Stuart", stusc)
    else:
        print("Draw")   


# In[ ]:


#MERGE THE TOOLS!

def merge_the_tools(string, k):
    lista=[]
    for i in string:
        lista.append(i)
    l=[]
   
    numero=(len(lista))/k

    for i in range(1,numero+1):
        for i in range(1,k+1):
            a=1
            l.append(lista[0])
            lista=lista[a:]
            a=a+1

        l1=[]
        for i in l:
            if i not in l1:
                l1.append(i)
        s=''
        for i in l1:
            s=s+i
        l=[]
        print(s)


# In[ ]:


#############################---------------SETS excercises----------###########################


# In[ ]:


#INTRODUCTION TO SETS

def average(array):
    
    
    sett=set(array)
    somma=0
    for i in sett:
        i=int(i)
        somma=somma+i
    average=somma/(len(sett))
    return average


# In[ ]:


#NO IDEA!

hdoiu=input()
array=input()
a=input()
b=input()
A=set(a.split())
B=set(b.split())
l=array.split()
happiness=0
for i in l:
    if i in A:
        happiness=happiness+1
    if i in B:
        happiness=happiness-1
print(happiness)


# In[ ]:


#SYMMETRIC DIFFERENCE

bla=input()
m=input()
bl1=input()
n=input()
M=set(m.split())
N=set(n.split())
diff=(M.difference(N)).union(N.difference(M))
l=[]
for i in diff:
    l.append(i)
l=list(map(int,l))
l.sort()
for i in l:
    print(i)


# In[ ]:


#SET .ADD()

a=int(input())
sett=set()
for i in range(1,a):
    n=input()
    sett.add(n)
print(len(sett))


# In[ ]:


#SET .DISCARD() , .REMOVE(), POP()

gh = int(input())
s = set(map(int, input().split()))
n=int(input())
for i in range(n):
    comando=input().split()
    if comando[0]=='remove':
        s.remove(int(comando[1]))
    if comando[0]=='pop':
        s.pop()
    if comando[0]=='discard':
        s.discard(int(comando[1]))
somma=0
for i in s:
    somma=somma+i
print(somma)


# In[ ]:


#SET .UNION() OPERATION

gh=input()
A=set(map(int,input().split()))
a=input()
B=set(map(int,input().split()))
conto=len(A|B)
print(conto)


# In[ ]:


#SET .INTERSECTION() OPERATION

asd=input()
eng=set(map(int,input().split()))
asdd=input()
fran=set(map(int,input().split()))
print(len(eng.intersection(fran)))


# In[ ]:


#SET .DIFFERENCE() OPERATION

sas=input()
eng=set(map(int,input().split()))
asd=input()
fran=set(map(int,input().split()))
print(len(eng-fran))


# In[ ]:


#SET .SYMMETRIC_DIFFERENCE() OPERATION

asd=input()
eng=set(map(int, input().split()))
asdd=input()
fran=set(map(int, input().split()))
print(len(eng^fran))


# In[ ]:


#SET MUTATIONS

asd=input()
s=set(map(int, input().split()))
n=int(input())
for i in range(n):
    comando=input().split()
    set1=set(map(int, input().split()))
    if comando[0]=='intersection_update':
        s.intersection_update(set1)
    if comando[0]=='symmetric_difference_update':
        s.symmetric_difference_update(set1)
    if comando[0]=='difference_update':
        s.difference_update(set1)
    if comando[0]=='update':
        s.update(set1)
somma=0
for i in s:
    somma=somma+i
print(somma)


# In[ ]:


#THE CAPTAIN'S ROOM

from collections import Counter

a=int(input())
l=input().split()
co=Counter(l)
for (key,value) in co.items():
    if value==1:
        print(key)


# In[ ]:


#CHECK SUBSET

for i in range(int(input())):
    nA=int(input())
    A=input().split()
    nB=int(input())
    B=input().split()
    res=True
    for i in A:
        if i not in B:
            res=False
            break
    print(res)


# In[ ]:


#CHECK STRICT SUPERSET


A=input().split()
res=True
for i in range(int(input())):
    B=input().split()
    for i in B:
        if i not in A:
            res=False
            break
print(res)


# In[ ]:


#################################-------------------COLLECTIONS excercises---------------############################


# In[ ]:


#COLLECTION.COUNTER()

from collections import Counter

a=int(input())
l=input().split()
for i in l:
    i=int(i)
dicti=Counter(l)

tot=0

for i in range(int(input())):
    cust=input().split()
    numero=cust[0]
    price=int(cust[1])
    if dicti[numero]>0:
        dicti[numero]=dicti[numero]-1
        tot=tot+price
print(tot)


# In[ ]:


#DEFAULTDICT TUTORIAL

from collections import defaultdict
a=input().split()
n=int(a[0])
m=int(a[1])
d=defaultdict(list)
for i in range(1,n+1):
    elem=input()
    
    d[elem].append(str(i))
    
for i in range(m):
    elem=input()
    if elem in d.keys():
        print(' '.join(d[elem]))
    else: 
        print(-1)


# In[ ]:


#COLLECTIONS.NAMEDTUPLE()

from collections import namedtuple
n=int(input())
columns=' '.join(input().split())
l=columns.split()
Student=namedtuple('Student', columns)
mark=0
for i in range(n):
    l_dati=(' '.join(input().split())).split()
    
    studente=Student(l_dati[0], l_dati[1], l_dati[2], l_dati[3])
    mark=mark+int(studente.MARKS)
print(mark/n)
   


# In[ ]:


#COLLECTIONS.ORDEREDDICT()

from collections import OrderedDict
d=OrderedDict()
for i in range(int(input())):
    l=input().split()
    key=''
    for i in l:
        if i.isalpha()==True:
            key=key+' '+i
            key=' '.join(key.split())
        if i.isnumeric()==True:
            if key in d.keys():
                d[key]=int(d[key])+int(i)
            else:
                d[key]=int(i)

for i in d:
    s=i+' '+str(d[i])
    print(s)


# In[ ]:


#WORD ORDER



from collections import OrderedDict
l=[]
d=OrderedDict()
for i in range(int(input())):
    a=input()
    if a not in d:
        d[a]=1
    else:
        d[a]=d[a]+1
print(len(d.keys()))
s=''
for i in d.values():
    s=s+str(i)+' '
print(s)


# In[ ]:


#COLLECTIONS.DEQUE()

from collections import deque
d = deque()
for i in range(int(input())):
    l=input().split()
    if l[0]=='append':
        d.append(l[1])
    if l[0]=='appendleft':
        d.appendleft(l[1])
    if l[0]=='pop':
        d.pop()
    if l[0]=='popleft':
        d.popleft()
s=''
for i in d:
    s=(s+i+' ')
    
print(s.strip())


# In[ ]:


#COMPANY LOGO


from collections import OrderedDict


if __name__ == '__main__':
    s = input()

    d=OrderedDict()
    for i in s:
        if i not in d.keys():
            d[i]=s.count(i)
    d=OrderedDict(sorted(d.items()))

    l=[]
    valori=[]
    chiavi=[]

    for i in d.values():
        valori.append(int(i))

    for i in d.keys():
        chiavi.append(i)
        
    while len(l)<3:
        for i in valori:
            if i==max(valori) and len(l)<3 :
                indice=valori.index(i)
                l.append(chiavi[indice])
                valori.remove(i)
                chiavi.remove(chiavi[indice])
    for i in l:
        s=i+' '+str(d[i])
        print(s)


# In[ ]:


#PILING UP!

from collections import deque
for i in range(int(input())):
    lung=int(input())
    d=deque(map(int,input().split()))
    cubo=[]
    limite=2**31
    risp='Yes'
    while len(d)>=0:
        fatto='no'
        if len(d)==1:
            cubo.append(d[0])
            risp='Yes'
            break
        
        if d[0]<=limite and d[0]>=d[-1]:
            cubo.append(d[0])
            limite=d[0]
            d.popleft()
            fatto='si'
        if d[-1]<=limite and fatto=='no' and d[-1]>=d[0]:
            cubo.append(d[-1])
            limite=d[-1]
            d.pop()
            fatto='si'
        
        if d[0]>limite or d[-1]>limite:
            risp='No'
            break
    print(risp)
    


# In[ ]:


###################################-----------------------DATA AND TIME excercises-------------------#######################


# In[ ]:


#CALENDAR MODULE

import calendar
data=list(map(int, input().split()))
giorno=calendar.weekday(data[2],data[0],data[1])
if giorno==0:
    print('MONDAY')
if giorno==1:
    print('TUESDAY')
if giorno==2:
    print('WEDNESDAY')
if giorno==3:
    print('THURSDAY')
if giorno==4:
    print('FRIDAY')
if giorno==5:
    print('SATURDAY')
if giorno==6:
    print('SUNDAY')


# In[ ]:


#TIME DELTA

#!/bin/python3

import math
import os
import random
import re
import sys
import datetime

def time_delta(t1, t2):
    
    t1=datetime.datetime.strptime(t1,'%a %d %b %Y %H:%M:%S %z' )
    t2=datetime.datetime.strptime(t2,'%a %d %b %Y %H:%M:%S %z' )
    return str(int((abs(t1-t2)).total_seconds()))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()




# In[ ]:


#########################-----------------------EXCEPTIONS excercise---------------############################


# In[ ]:


#EXCEPTIONS


for i in range(int(input())):
    
    try:
        inp=list(map(int,input().split()))
        print(inp[0]//inp[1])
    except BaseException as e:
        print('Error Code:',e)


# In[ ]:


#########################------------------------BUILT-INS excercises----------------------################################


# In[ ]:


#ZIPPED!

a,b=list(map(int,input().split()))
l=[]
for i in range(b):
    l.append(list(map(float,input().split())))
tup=tuple(zip(*tuple(l)))
for i in tup:
    avg=sum(i)/b
    print(avg)


# In[ ]:


#ATHLETE SORT

import math
import os
import random
import re
import sys
from collections import OrderedDict



if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())
    arr=sorted(arr,key=lambda x:x[k])
    for i in arr:
        x=' '.join(list(map(str, i)))
        print(x)


# In[ ]:


#GINORTS

lower=[]
upper=[]
odd_digit=[]
even_digit=[]
for i in(input()):
    if i.isalpha()==True:
        if i.islower()==True:
            lower.append(i)
        else:
            upper.append(i)
    if i.isnumeric()==True:
        if int(i)%2!=0:
            odd_digit.append(str(i))
        else:
            even_digit.append(str(i))
s=''.join(sorted(lower))+''.join(sorted(upper))+''.join(sorted(odd_digit))+''.join(sorted(even_digit))
print(s)


# In[ ]:


#####################----------------PYTHON FUNCTIONALS excercise-----------------###########################


# In[ ]:


#MAP AND LAMBDA FUNCTION

cube=lambda x: x**3
def fibonacci(n):
    l=[]
    if n==0:
        return l
    l.append(0)
    if n==1:
        return l
    
    l.append(1)
    if n==2:
        return l
    for i in range(2,n):
        l.append(l[i-1]+l[i-2])
    
    return l


# In[ ]:


#############################--------------REGEX AND PARSING excercises-------------------#########################


# In[ ]:


#DETECT FLOATING POINT NUMBER

import re
for i in range(int(input())):
    n=input()
    print(bool(re.match('[-+]?[0-9]*[.][0-9]+$', n)))


# In[ ]:


#RE.SPLIT()

import re
regex_pattern = r"[,.]"
print("\n".join(re.split(regex_pattern, input())))


# In[ ]:


#VALIDATING ROMAN NUMBERS


regex_pattern = r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"

import re
print(str(bool(re.match(regex_pattern, input()))))


# In[ ]:


#GROUP(), GROUPS() AND GROUPDICT()

import re

m=re.search(r'([0-9a-zA-Z]+)\1', input())
if bool(m)==True:
    print(m.group(1))
else:
    print(-1)


# In[ ]:


#RE.FINDALL() AND RE.FINDITER()

import re
v='AEIOUaeiou'
c='bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'


m=re.findall(r'(?<=['+c+'])(['+v+']{2,})(?=['+c+'])', input().strip())
if len(m)>0:
    for i in m:
        print(i)
else:
    print(-1)


# In[ ]:


#RE.START() AND RE.END()

import re
s,t=input(),input()
i=0
if re.search(t,s):
    while i+(len(t))<(len(s)) and re.search(t,s[i:]) :
        m=re.search(t,s[i:])
        print('({0}, {1})'.format(i+m.start(),i+m.end()-1))
        i=i+m.start()+1
else:
    print('({0}, {1})'.format(-1,-1))


# In[ ]:


#REGEX SUBSTITUTION

import re
for i in range(int(input())):
    s=input()
    t=re.sub(r'(?<= )\&\&(?= )', 'and', s)
    u=re.sub(r'(?<= )\|\|(?= )', 'or', t)
    print(u)


# In[ ]:


#VALIDATING PHONE NUMBERS

import re
for i in range(int(input())):
    n=input()
    if re.match(r'[789][0-9]{9}$',n):
        print('YES')
    else:
        print('NO')


# In[ ]:


#VALIDATING AND PARSING EMAIL ADDRESSES

import re
for i in range(int(input())):
    l=list(map(str,input().split()))
    mail=l[1].strip().strip('<').strip('>')
    m=re.match(r'[A-Za-z][A-Za-z0-9\-\.\_]+(@)[A-Za-z]+[.][A-Za-z]{1,3}$', mail)
    if m:
        print(' '.join(l))
    


# In[ ]:


#HEX COLOR CODE

import re
for i in range(int(input())):
    
    l=re.findall(r'[#][ABCDEFabcdef0-9]{3}[;,)]|[#][ABCDEFabcdef0-9]{6}[;,)]', input())
    for i in l:
        print(i[:len(i)-1])


# In[ ]:


#HTML-PARSER - PART 1

from html.parser import HTMLParser
a=int(input())

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print('Start :', tag)
        for i in attrs:
            print('->', i[0],'>',i[1])
    def handle_endtag(self, tag):
        print('End   :', tag)

    def handle_startendtag(self, tag, attrs):
        print('Empty :', tag)
    
        for i in attrs:
            print('->', i[0],'>',i[1])
parser=MyHTMLParser()
for i in range(a):
    
    parser.feed(input())


# In[ ]:


#HTML PARSER - PART 2

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self,data):
        if len(data.split('\n'))>1:
            print('>>> Multi-line Comment')
        else:
            print('>>> Single-line Comment')
        print(data)
    def handle_data(self,data):
        if data!='\n':
            print('>>> Data')
            print(data)

html=''
parser=MyHTMLParser()
for i in range(int(input())):
    html=html+input().rstrip()+'\n'
parser.feed(html)


# In[ ]:


#DETECT HTML TAGS, ATTRIBUTES AND ATTRIBUTE VALUES

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self,tag, attrs):
        print(tag)
        for i in attrs:
            print('->',i[0],'>',i[1])

parser=MyHTMLParser()
html=''
for i in range(int(input())):
    html=html+input().rstrip()+'\n'
parser.feed(html)


# In[ ]:


#VALIDATING UID

import re

for i in range(int(input())):
    a=input().strip()
    res='Invalid'
    if bool(re.search('(.*[0-9].*){3,}',a)) and bool(re.search('(.*[A-Z].*){2,}', a)) and bool(re.match('[A-Za-z0-9]{10,10}$', a)):
        for i in a:
            if a.count(i)==1:
                res='Valid'
            else:
                res='Invalid'
                break
        print(res)


    else:
        print('Invalid')


# In[ ]:


#VALIDATING CREDIT CARD NUMBERS

import re
for i in range(int(input())):
    res='si'
    n=input().strip()
    if re.match(r'[0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{4}$', n):
        n=n.split('-')
        n=(''.join(n)).strip()
    else:
        n=''.join(n)
    
  
    
    i=0


    while i<(len(n)-1):
        try:
            if n[i]==n[i+1] and n[i]==n[i+2] and n[i]==n[i-1]:
                res='no'
                break
            else:
                res='si'
                i=i+1
        except IndexError:
            i=i+1
        

    
    if res=='si' and re.match(r'(^[456]{1})([0-9]{15})$', n):
        print('Valid')

    else:
        print('Invalid')


# In[ ]:


#VALIDATING POSTAL CODES

import re

regex_integer_in_range = '^[1-9][0-9]{5}$'
regex_alternating_repetitive_digit_pair = r"([0-9]*([0][0-9][0])[0-9]*)|([0-9]*([1][0-9][1])[0-9]*)|([0-9]*([2][0-9][2])[0-9]*)|([0-9]*([3][0-9][3])[0-9]*)|([0-9]*([4][0-9][4])[0-9]*)|([0-9]*([5][0-9][5])[0-9]*)|([0-9]*([6][0-9][6])[0-9]*)|([0-9]*([7][0-9][7])[0-9]*)|([0-9]*([8][0-9][8])[0-9]*)|([0-9]*([9][0-9][9])[0-9]*)"


regex_integer_in_range = r"^[1-9][0-9]{5}$"
regex_alternating_repetitive_digit_pair = r"(\d)(?=.\1)"
P = input()

print (bool(re.match(regex_integer_in_range, P)) 
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)


# In[ ]:


#MATRIX SCRIPT



import math
import os
import random
import re
import sys




first_multiple_input = input().rstrip().split()

riga = int(first_multiple_input[0])

col = int(first_multiple_input[1])

matrix = []
l=[]

for i in range(riga):
    matrix.append(input())

for i in range(col):
    for j in matrix:
        l.append(j[i])
l=''.join(l)
l=re.sub(r'([a-zA-Z0-9])[^a-zA-Z0-9]+([A-Z0-9a-z])', r'\1 \2', l)
print(l)


# In[ ]:


###################--------------------XML excercises----------------#############################


# In[ ]:


#XML 1

import sys
import xml.etree.ElementTree as etree


def get_attr_number(node):
    score=0
    for child in (node.iter()):
        score=score+len(child.attrib)
    return score
        

if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))


# In[ ]:


#XML 2

import xml.etree.ElementTree as etree

maxdepth = -1
def depth(elem, level):
    global maxdepth
    
    if (level == maxdepth):
        maxdepth += 1
        
    for child in elem:
        depth(child, level + 1)

if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)


# In[ ]:


######################-----------------------CLOSURES AND DECORATIONS excercises-------------###########################


# In[ ]:


#STANDARDIZE MOBILE NUMBER USING DECORATORS

import re

def wrapper(f):
    def fun(l):
        l1=[]
        for i in l:
            
            
            l1.append('+91 '+i[-10:-5]+' '+i[-5:])
        l1=sorted(l1)
        for i in l1:
            print(i)
    return fun        

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 


# In[ ]:


#DECORATORS 2 - NAME DIRECTORY

import operator
def age(x):
    return int(x[2])


def person_lister(f):
    def inner(people):
         
        return map(f, sorted(people, key=age))          
    return inner
        


    

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')


# In[ ]:


######################----------------------NUMPY excercises----------------------###################################


# In[ ]:


#ARRAYS


import numpy

def arrays(arr):
    b=numpy.array(arr,float)
    return b[::-1]

arr = input().strip().split(' ')
result = arrays(arr)
print(result)


# In[ ]:


#SHAPE AND RESHAPE

import numpy as np

b=np.array(input().split(), int)
print(np.reshape(b,(3,3)))


# In[ ]:


#TRANSPOSE AND FLATTEN


import numpy as np
nm=input().split()
row=int(nm[0])
col=int(nm[1])
l=[]
for i in range(row):

    l.append(np.array(input().split(), int))
b=np.array(l)
print(np.transpose(b))
print(b.flatten())


# In[ ]:


#CONCATENATE

import numpy as np

a=input().split()
row1,row2,col=int(a[0]),int(a[1]),int(a[2])

l=[]
l1=[]
for i in range(row1):
    l.append(input().split())
for i in range(row2):
    l1.append(input().split())
a=np.array(l,int)
b=np.array(l1,int)
print(np.concatenate((a,b),axis=0))




# In[ ]:


#ZEROS AND ONES

import numpy as np

x=list(map(int,input().split()))
print(np.zeros(x,dtype=int))
print(np.ones(x,dtype=int))


# In[ ]:


#EYE AND IDENTITY

import numpy as np


l=list(map(int, input().split()))
print(str(np.eye(l[0], l[1])).replace('1',' 1').replace('0',' 0'))


# In[ ]:


#ARRAY MATHEMATICS

import numpy as np
n, m = map(int, input().split())
a, b = (np.array([input().split() for _ in range(n)], dtype=int) for _ in range(2))
print(a+b, a-b, a*b, a//b, a%b, a**b, sep='\n')


# In[ ]:


#FLOOR, CEIL AND RINT

import numpy as np
np.set_printoptions(sign=' ')

a=np.array(input().split(),float)
print(np.floor(a))
print(np.ceil(a))
print(np.rint(a))


# In[ ]:


#SUM AND PROD

import numpy as np
m=list(map(int,input().split()))
l=[]
for i in range(m[0]):
    l.append(list(map(int,input().split())))
res=1
for i in (np.sum(l,axis=0)):
    res=res*i
print(res)




# In[ ]:


#MIN AND MAX

import numpy as np
g=list(map(int,input().split()))
l=[]
for i in range(g[0]):
    l.append(input().split())
a=np.array(l,int)
b=np.min(a,axis=1)
print(max(b))


# In[ ]:


#MEAN, VAR AND STD

import numpy as np
np.set_printoptions(sign=' ')
np.set_printoptions(legacy='1.13')

g=list(map(int, input().split()))
l=[]
for i in range(g[0]):
    l.append(input().split())
a=np.array(l,int)
print(np.mean(a,axis=1))
print(np.var(a,axis=0))
print(np.std(a,axis=None))


# In[ ]:


#DOT AND CROSS


import numpy as np
n=int(input())
arr1,arr2=[(np.array([list(map(int,input().split())) for _ in range(n)])) for _ in range(2)]
print (np.dot(arr1,arr2))


# In[ ]:


#INNER AND OUTER

import numpy as np

a=np.array(input().split(),int)
b=np.array(input().split(),int)
print(str(np.inner(a,b)))
print(np.outer(a,b))


# In[ ]:


#POLYNOMIALS

import numpy as np
print(np.polyval(np.array(input().split(),float),int(input())))




# In[ ]:


#LINEAR ALGEBRA

import numpy as np
n=int(input())
l=[]
for i in range(n):
    l.append(input().split())
a=np.array(l,float)
print(round((np.linalg.det(a)),2))


# In[ ]:


#######################################----------BIRTHDAY CAKE CANDLES---------------#################################


# In[ ]:


#!/bin/python3

import math
import os
import random
import re
import sys


def birthdayCakeCandles(candles):
    maxx=0
    count=0
    for i in candles:
        if i>=maxx:
            
            maxx=i
    n=candles.count(maxx)
    return n
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()


# In[ ]:


#############################-----------NUMBER LINE JUMPS-----------########################################


# In[ ]:


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    pos1=x1
    pos2=x2
    i=0
    while (pos1)!=(pos2):
        pos1=pos1+v1
        pos2=pos2+v2
        i=i+1
        if i==9999:
            return 'NO'
    return 'YES'
        
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()


# In[ ]:


##########################---------------------------VIRAL ADVERTISING-----------------##########################


# In[ ]:


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the viralAdvertising function below.
def viralAdvertising(n):
    y=2
    k=2
    i=1
    while i<n:
        i=i+1
        if (y*3)%2==0: 
            y=(y*3)/2
            
        else:
            y=((y*3)-1)/2
        k=k+y
    return int(k)



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()


# In[ ]:


#############################-----------------RECURSIVE DIGIT SUM-------------------#####################################


# In[ ]:


import math
import os
import random
import re
import sys


def superDigit(n, k):
    if len(n) == 1:
        return int(n)
    summ=0
    for i in n:
        summ=summ+int(i)
    p = summ * k
    return superDigit(str(p), 1)
    
        
    




    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = nk[0]

    k = int(nk[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()


# In[ ]:


####################----------------INSERTION SORT - PART 1-----------------#############################


# In[ ]:


#!/bin/python3

import math
import os
import random
import re
import sys
# Complete the insertionSort1 function below.
def insertionSort1(n, arr):
    num=arr[n-1]
    for i in range(n-2,-1,-1):
        if arr[i]>num:
            arr[i+1]=arr[i]
            s=''
            for j in arr:
                s=s+str(j)+' '
            print(s)
        else:
            
            arr[i+1]=num
            s=''
            for j in arr:
                s=s+str(j)+' '
            print(s)
            break
    if arr[0]>num:
        arr[0]=num
        s=''
        for j in arr:
            s=s+str(j)+' '
        print(s)
    


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)


# In[ ]:


####################------------INSERTION SORT - PART2----------------########################


# In[ ]:


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the insertionSort2 function below.
def insertionSort2(n, arr):
    for i in range(1,n):
        num=arr[i]
        ind=i-1
        while arr[ind]>num and ind>=0:
            arr[ind+1]=arr[ind]
            ind=ind-1
        arr[ind+1]=num
        print(' '.join(list(map(str,arr))))





if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)


# In[ ]:




