from ws_utils.vec2 import vec2
from ws_utils.triangulate import triangulator
import math
p1 = vec2(-2, -2)
p3 = vec2(2, -2)
p2 = vec2(0, math.sqrt(8))

tr = triangulator(p1, p2, p3)

d1 = 7
d2 = 5
d3 = 7

tr.finddists(d1, d2, d3)