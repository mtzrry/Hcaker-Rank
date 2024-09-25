# defisini type
# type point : <x:integer, y:integer>
# {<x,y> adalah sebuah point dengan x sebagai absis dan y sebagai ordinat}

# definisi dan spesifikasi selektor
# Absis : point -> real
#   {Absis (P), memberikan absis point P}
# Ordinat : point -> real
#   {Ordinat (P), memberikan Ordinat point P}

# definisi dan spesifikasi konstruktor
# make_point : 2 real -> point
# {make_point(a,b), membentuk sebuah point dari a dan b, dimana a sebagai absis dan b sebagai ordinat}

# definisi dan spesifikasi predikat
# IsOrigin? : point -> boolean
# {IsOrigin(P), benar jika P adalah titik origin yaitu <0,0>}

# definisi operator/fungsi lain terhadap point
# fx2 : integer -> integer
# {fx2(x), mengembalikan nilai dari x dikali x}

from math import sqrt

def Is_Origin(a,b) -> bool :
    return a == 0 and b == 0
def fx2(x) :
    return x*x
def make_point(a,b) :
    return [a,b]
def Absis(P) :
    return P[0]
def Ordinat(P) :
    return P[1]
def jarak(P1,P2) :
    return sqrt(fx2(Absis(P1)-Absis(P2))+fx2(Ordinat(P1)-Ordinat(P2)))
def jarak_1(P) :
    return sqrt(fx2(Absis(P))+fx2(Ordinat(P)))

p = make_point(1,2)
q = make_point(1,2)

print(jarak(p,q))
print(jarak_1(p))