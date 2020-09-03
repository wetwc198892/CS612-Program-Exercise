a,b,c = [3,3],[-1,-1],[2,-0.5]
lenA = ((a[0]-b[0])**2 + (a[1]-b[1])**2)**0.5
lenB = ((b[0]-c[0])**2 + (b[1]-c[1])**2)**0.5
lenC = ((c[0]-a[0])**2 + (c[1]-a[1])**2)**0.5
if lenA + lenB > lenC and lenB + lenC > lenA and lenC + lenA > lenB:
    area = abs(a[0]*b[1] + b[0]*c[1] + c[0]*a[1] - a[0]*c[1] - b[0]*a[1] - c[0]*b[1])/2
    print(area)
else:
    print('Does not form a triangle')