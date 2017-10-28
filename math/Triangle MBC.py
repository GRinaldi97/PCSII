# -*- coding: utf-8 -*-
import math
AB=int(input())
BC=int(input())
a= math.atan2(AB, BC)
print str(int(round((math.degrees(a))))) + "°"