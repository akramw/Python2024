## in pythone 14 data type inbild.
## @int @float @complex @bool and @str is a Fundamentel data type.

####### int 38208653 and we can repersent 4 way     .
i=575765 #Decimal.
type(i)
i=0B1111 #Binary.
i=0O1111 #Octal.
i=0X1111 #Hexa decimal.

####### float 123.0025 while we need floting point value like salary: 2000.50, Deasiel price: 89.30.
# Only Decimal value allow only.
f=123.456
type(f)
f=1.2e3  #Exponential From allow in float
print(f)

####### complex while we need mathamatice turm or program
c=10+20j
type(c)
print(c)

###### bool True/Fals to represent some logical value True/Fals
# Captiel T and F is mandatory
a=10
b=20
c=a<b
print(c) #True
b=True  # value is 1
b=False # value is 0
b=True + True
print(b)

###### str 'wasim' or String is sequence of characters text/word/sentens/Doc.. enclose within Single quotes 'wasim' Dubble quotes "wasim" 
# also we can use triple Single or double """ wasim akram""" for multi line.
s='wasim'
s="wasim"
s="""wasim
        akram"""
type(s)

    #Slice-Index-Step Operrator
    #s[begin:end:step]
s='durgasoft' #Index stsrt with '0' and end always (-1)  also (+ve) (-ve) Index posible 
s[0] #itwill print 'd'
s[3] #it will print 'g'
s[0:3] #urg
s[1:10:2] #step
s='durga'
s=s*10 #10time print
print(s)

###### bytes [10,20,30,40] data typegroup of byte number just like array
by=[10,20,30,40]
b=bytes(by)
type(b)

###### bytearray [10,20 can change,30,40] data type also same as bytes only change it's mutable we can change te data.
bya=[10,20,30,40]
b=bytearray(bya)
type(b)
b[0]=120 # data can changable
for i in b : print(i)

###### list [ ] Squere data type to represent a group of values as a single entaty where Order is Preserved and Duplicate are allow.
l=[10,20,30,10,'durga'] #Duplicate/slice-Index-Step Operrator and repetable allow
type(l)

###### tuple ( ) Paranthases same as list only it's Immutable(Data Non changable)
t=(10,20,'durga',True,10)
type(t)
t[0]

###### range represent a sequence of value or numbr and Immutable non changeble data
r=range(0,10)
for i in r:print(r)
r=range(10,50)
for i in r:print(r)
r=range(10,50,5)
for i in r:print(r)

###### set{10,20,30,10,20} to represent group of value in single entaty but Order and duplicate are not allow
# Index and Slice is not allow but Mutable we can change the data
s={10,20,30,10,20,30}
s.add('durga')
s.remove(20)
print(s) #it will remove duplicate recod

###### frozenset {10,20,30,10,20} same as set only change it's Immutable Non changable data..
# Group of qunick value but no one allow to change or list of token no one allow to change or duplicate
s={10,20,30,40}
fs=frozenset(s)
type(fs)

###### dict {} (Dictionary) to represent a group of Object as Key-Value pairs like Roll-Name,Word-Meaning,MobileNo-Name
#Eampaty {} curly brase always dict
d={100:'durga',200:'shiva',300:'ravi'}
type(d)
#d1[100]='suny'  #its mutable and Older value replace weith new value not Key value
#d1[200]='buny'

###### None None value should associtated with somthing.
def f1():   #this is one function whic is not retuning any this
        a=10

def f2(): print("Hello")
print(f1(),f2())
