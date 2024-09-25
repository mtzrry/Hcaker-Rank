
def fx2(x) :
    return x*x
print(fx2(2))

def fx3v1 (x) :
    return x*x*x
print (fx3v1(5+7))

def max2(x,y) :
    return((x+y)+(x-y)) // 2

def max3(x,y,z) :
    return max2(max2(x,y),z)

print(max2(2,1))
print(max3(1,2,8))

def positif (x,y) :
    return x==0 and y==0

print(positif(0,0))
print(positif(1,0)) 

def positif (x,y) :
    return x==0 or y==0

print(positif(0,0))
print(positif(1,0)) 

def jarak(x1,y1,x2,y2) :
    x=(x2-x1)
    y=(y2-y1)

    total = (x**2) + (y**2)
    return total**0.5

print(jarak(1,1,4,5))

def fx2(x) :
    print(x*x)

fx2(2)