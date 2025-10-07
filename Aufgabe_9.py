def v2_substract(v1, v2):
    return [
        v1[0] - v2[0],
        v1[1] - v2[1]
    ]

def determinant(m):
    return m[0] * m[3] - m[1] * m[2]

def makeMatrix(v1, p1):
    return [
        v1[0], p1[0],
        v1[1], p1[1],
    ]

a = [1, 7]
b = [2, 3]
c = [4, 5]
p = [1.5, 1.5]

v_edge_ab = v2_substract(b, a)
v_edge_bc = v2_substract(c, b)
v_edge_ca = v2_substract(a, c)

v_ap = v2_substract(p, a)
v_bp = v2_substract(p, b)
v_cp = v2_substract(p, c)

det_a = determinant(makeMatrix(v_edge_ab, v_ap))
det_b = determinant(makeMatrix(v_edge_bc, v_bp))
det_c = determinant(makeMatrix(v_edge_ca, v_cp))

if det_a >= 0 and det_b >= 0 and det_c >= 0:
    print("Point is inside the triangle")

elif det_a < 0 and det_b < 0 and det_c < 0:
    print("Point is outside the triangle")

elif det_a == 0 and det_b == 0 and det_c == 0:
    print("Point is on the edge")