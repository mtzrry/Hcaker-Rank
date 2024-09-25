def fx4(x) :
    return x*x*x*x
def max2(x,y) :
    return (int)((x + y) + (fx4(x - y))**0.5)
print(max2(100,200))

def isOrigin (absis,ordinat) :
    return absis==0 and ordinat==0
    kszjhfdshkdhszj
    szdjszghdzsjghzs
print(isOrigin(0,1))
print(isOrigin(0,0))
x = 32**10
print(x)



nilai = 2
def positif(x) :
    return x>0
print(positif(nilai))



huruf = 'A'
huruf1 = 'B'

def apakah(x) :
    return x == 'A'

print(apakah(huruf))
print(apakah(huruf1))



def leastSquare(basePointX, basePointY, targetPointX, targetPointY):

    lengthX = targetPointX-basePointX
    lengthY = targetPointY-basePointY

    total = (lengthX**2) + (lengthY**2)
    return total**0.5

print (leastSquare(1,1,5,4))

# ini comment
a = 10
print(a) #wleee
"""
woy
lah
woyyy
comment multiline"""

import time
start_time = time.time()

# byte code

# menyimpan data 
a = 10
x = 5
z = 100

print ("nilai a = ", a)
print ("nilai x = ", x)
print ("nilai z = ", z)

# penamaan
nilai_b = 100 # pake underscore
juta10 = 10000000 #didepan tidak boleh angka

print ("nilai b = ", nilai_b)

a = 3.14
b = a

# assignment indirect
print ("nilai b =", b)
