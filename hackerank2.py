def max3(a, b, c):
    if a>b:
        if a>c:
            return a
        else:
            return c
    else:
        if b>c:
            return b
        else:
            return c
        
def min3(a, b, c):
    if a<b:
        if a<c:
            return a
        else :
            return c
    else:
        if b<c:
            return b
        else:
            return c
        
def jangkauan(a, b, c):
    return max3(a, b, c)-min3(a, b, c)

def hari(d):
    if d=="senin": return 5000
    elif d=="selasa": return 14000/3
    elif d=="rabu":return 11000/3
    elif d=="kamis":return 7000/3
    elif d=="jumat":return 3000
    elif d=="sabtu": return 6800/3
    elif d=="minggu":return 1000
    
def EstimateGreatLib(d, x, y, ss, sr, ass, am, aip, r):
    if (x>=sr and x<=ss) and (y>=sr and y<=ss):
        return (y-x)*(jangkauan(ass, am, aip))/hari(d)
    elif x<sr and (y>sr and y<=ss):
        return (((sr-x)*(jangkauan(ass, am, aip))*r/100)+((y-sr)*(jangkauan(ass, am, aip)))) / hari(d) / 2
    elif (x>=sr and x<ss) and y>ss:
        return (((y-ss)*(jangkauan(ass, am, aip))*r/100)+((ss-x)*(jangkauan(ass, am, aip)))) / hari(d) / 2
    elif (x<sr and y<=sr) or (x>=ss and y>ss):
        return ((y-x)*(jangkauan(ass, am, aip))*r/100)/hari(d)
    else:
        return ((((sr-x)+(y-ss)) *r/100)+(ss-sr)) *jangkauan(ass, am, aip) / 3 / hari(d)
    


print(round(eval(input()),5))