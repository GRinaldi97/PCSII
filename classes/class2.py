import math
class Points(object):
    def __init__(self, x, y, z):
        self.x=float(x)
        self.y=float(y)
        self.z=float(z)
    def __sub__(self, no):
        return Points(self.x-no.x, self.y-no.y, self.z-no.z)
    def dot(self, no):
        return sum([self.x*no.x, self.y*no.y,self.z*no.z]) 
    def cross(self, no):
        return (self.y*no.z-self.z*no.y, self.x*no.z-self.z*no.x, self.x*no.y-self.y*no.x)
    def abso(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)
L=[]
for i in range(4):
    a=raw_input().split()
    L.append(map(float,a))
A = Points(*L[0])
B = Points(*L[1])
C = Points(*L[2])
D = Points(*L[3])
X= Points(*list((B-A).cross(C-B)))
Y= Points(*list((C-B).cross(D-C)))
cosalpha= math.acos(X.dot(Y)/(X.abso()*Y.abso()))
print str(round(math.degrees(cosalpha), 2))
