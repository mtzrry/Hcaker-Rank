# Mean Olympique
def max2(a,b) :
    return (a+b+abs(a-b))/2
def min2(a,b) :
    return (a+b-abs(a-b))/2
def max4(a,b,c,d) :
    return max2(max2(a,b),max2(c,d))
def min4(a,b,c,d) :
    return min2(min2(a,b),min2(c,d))
def MO(a,b,c,d) :
    return (a+b+c+d-max4(a,b,c,d)-min4(a,b,c,d))/2

a = int(input("Masukan nilai a = "))
b = int(input("Masukan nilai b = "))
c = int(input("Masukan nilai c = "))
d = int(input("Masukan nilai d = "))

print(MO(a,b,c,d))



# LeastSquare
def math1(a,b) :
    return (a-b)**2
def math2(a,b) :
    return (a+b)**0.5
def LS(x1,x2,y1,y2) :
    return math2(math1(x1,x2),math1(y1,y2))

x1 = int(input("Masukan nilai x1 = "))
x2 = int(input("Masukan nilai x2 = "))
y1 = int(input("Masukan nilai y1 = "))
y2 = int(input("Masukan nilai y2 = "))

print(LS(x1,x2,y1,y2))