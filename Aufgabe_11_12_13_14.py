import random
from utils.objLoader import objLoader

o = objLoader("./humanHead.obj")

import math
import os

print(f"Lade {len(o.vertices) // 3} Vertices und {len(o.faceVertexIndices) // 3} Faces")

colors = []
for face in o.faceVertexIndices:
    color = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
    colors.append(color)


def save_ppm(width, height, buffer, time):
    # Create a path and file and open it for writing
    output_path = os.path.join(os.path.dirname(__file__), "output")
    output_file = os.path.join(output_path, "image.{time}.ppm".format(time=time))
    os.makedirs(output_path, exist_ok=True)
    ppm_file = open(output_file, "w")

    # Write the header
    width = width
    height = height
    header = "P3\n{w} {h}\n255\n".format(w=width, h=height)
    ppm_file.write(header)

    # Loop over buffer, after every third iteration add new line
    for index, value in enumerate(buffer):
        color_value = "{v} ".format(v=value)
        if (index + 1) % 3 == 0:
            color_value = color_value + "\n"
        ppm_file.write(color_value)

    print("file saved {time}".format(time=time))
    ppm_file.close()

def set_raster_coordinate(x, y, r, g, b):
    offset = 3 * x + (width * 3) * y
    buffer[offset] = r
    buffer[offset + 1] = g
    buffer[offset + 2] = b

def perspective_divide(p, screen_distance):
        return [
        screen_distance * p[0] / p[2],
        screen_distance * p[1] / p[2],
        screen_distance,
    ]
 
def view_to_raster(v, width, height):
    raster_X = ((v[0] + 1) / 2) * width
    raster_Y = ((1 - v[1]) / 2) * height

    return [round(raster_X), round(raster_Y)]

def m4_x_m4(a, b):
    return [
        # row 1
        a[0] * b[0] + a[1] * b[4] + a[2] * b[8] + a[3] * b[12],
        a[0] * b[1] + a[1] * b[5] + a[2] * b[9] + a[3] * b[13],
        a[0] * b[2] + a[1] * b[6] + a[2] * b[10] + a[3] * b[14],
        a[0] * b[3] + a[1] * b[7] + a[2] * b[11] + a[3] * b[15],
        # row 2
        a[4] * b[0] + a[5] * b[4] + a[6] * b[8] + a[7] * b[12],
        a[4] * b[1] + a[5] * b[5] + a[6] * b[9] + a[7] * b[13],
        a[4] * b[2] + a[5] * b[6] + a[6] * b[10] + a[7] * b[14],
        a[4] * b[3] + a[5] * b[7] + a[6] * b[11] + a[7] * b[15],
        # row 3
        a[8] * b[0] + a[9] * b[4] + a[10] * b[8] + a[11] * b[12],
        a[8] * b[1] + a[9] * b[5] + a[10] * b[9] + a[11] * b[13],
        a[8] * b[2] + a[9] * b[6] + a[10] * b[10] + a[11] * b[14],
        a[8] * b[3] + a[9] * b[7] + a[10] * b[11] + a[11] * b[15],
        # row 4
        a[12] * b[0] + a[13] * b[4] + a[14] * b[8] + a[15] * b[12],
        a[12] * b[1] + a[13] * b[5] + a[14] * b[9] + a[15] * b[13],
        a[12] * b[2] + a[13] * b[6] + a[14] * b[10] + a[15] * b[14],
        a[12] * b[3] + a[13] * b[7] + a[14] * b[11] + a[15] * b[15],
    ]

def vec3_to_vec4(v):
    return [v[0], v[1], v[2], 1]

def mult_vec3_m4(v, m):
    v4 = vec3_to_vec4(v)
    return [
        v4[0] * m[0] + v4[1] * m[4] + v4[2] * m[8] + v4[3] * m[12],
        v4[0] * m[1] + v4[1] * m[5] + v4[2] * m[9] + v4[3] * m[13],
        v4[0] * m[2] + v4[1] * m[6] + v4[2] * m[10] + v4[3] * m[14],
        v4[0] * m[3] + v4[1] * m[7] + v4[2] * m[11] + v4[3] * m[15],
    ]

def rot_x(rad): #hier rotation verändert, math.cos muss immer da stehen wo die 1 ist + 1 0 0 ist Stützvektor (sihe folien)
    m = [
        1, 0, 0,
        0, math.cos(rad), -math.sin(rad),
        0, math.sin(rad), math.cos(rad)
    ]
    return m

def rot_y(rad): 
    m = [
        math.cos(rad), 0, math.sin(rad),
        0, 1, 0,
        -math.sin(rad), 0, math.cos(rad), 
    ]
    return m

def rot_z(rad): 
    m = [
        math.cos(rad), -math.sin(rad), 0,
        math.sin(rad), math.cos(rad), 0,
        0, 0, 1
    ]
    return m

def m3_to_m4(m):
    return [
        m[0], m[1], m[2], 0,
        m[3], m[4], m[5], 0,
        m[6], m[7], m[8], 0,
        0, 0, 0, 1,
    ]

def easeInOutCubic(x):
    if x < 0.5:
        return 4 * x * x * x
    else:
        return 1 - math.pow(-2 * x + 2, 3) / 2

# Aufgabe 13 - rasterkoordinaten subtrahieren für 2d vektoren
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

#Aufgabe 18 AABB
def bbox(face_vertices_raster_coordinates, width, height):
# Initialize AABB with raster dimensions
    bboxmin = [width, height]
    bboxmax = [0, 0]

    # Loop over vertices, update bboxmin/bboxmax:
    for v in face_vertices_raster_coordinates:
        # v is now the raster-coordinate of a vertex
        bboxmin[0] = min(bboxmin[0], v[0]) # take the smaller value
        bboxmin[1] = min(bboxmin[1], v[1])
        bboxmax[0] = max(bboxmax[0], v[0]) # take the larger value
        bboxmax[1] = max(bboxmax[1], v[1])

    # Return a list of lists:
    # [[x,y],[x,y,]]
    return [bboxmin, bboxmax]

width = 200
height = 200
buffer_length = width * height
buffer = [55] * buffer_length * 3


translation =[
            1, 0, 0, 0,
            0, 1, 0, 0,
            0, 0, 1, 0,
            0, 0, -6, 1  #untere zeile verändern: verschiedene Positionen des Objekts (x,y,z li -> re)
            ]

frames = 25

for t in range(0, frames):
    buffer = [55] * buffer_length * 3
    normalized_t = t / frames
    eased_value = easeInOutCubic(normalized_t)
    angle = (360 / frames) * (eased_value * frames)
    radians = math.radians(angle)
    rotationy = m3_to_m4(rot_y(radians))
    #rotation = m4_x_m4(rotationy, m3_to_m4(rot_x(radians))) #rotationxy
   
    combined = m4_x_m4(rotationy, translation)

    for index, value in enumerate(o.faceVertexIndices[::3]):
        #print(f"Face {index}: {value}")
        # Get the vertex position
        v1 = o.faceVertexIndices[index * 3]
        v2 = o.faceVertexIndices[(index * 3) + 1]
        v3 = o.faceVertexIndices[(index * 3) + 2]

        v_index1 = (v1 -1) * 3
        v_index2 = (v2 -1) * 3
        v_index3 = (v3 -1) * 3

        v_faces = [
            o.vertices[v_index1], o.vertices[v_index1 + 1], o.vertices[v_index1 + 2],
            o.vertices[v_index2], o.vertices[v_index2 + 1], o.vertices[v_index2 + 2],
            o.vertices[v_index3], o.vertices[v_index3 + 1], o.vertices[v_index3 + 2]
        ]
        #print (v_faces)
        raster_coordinates = []

        for index, val in enumerate(v_faces[::3]):
            start_index = index * 3
                
            #raster koordinaten werden erstellt
            v = [
                v_faces[start_index],
                v_faces[start_index + 1],
                v_faces[start_index + 2]
            ]

            v_transformed = mult_vec3_m4(v, combined)

            #if v_transformed[2] > 0:
            #  continue

            screen_space_point = perspective_divide(v_transformed, -20)
            raster_point = view_to_raster(screen_space_point, width, height)

            #if not 0 <= raster_point[0] <= width - 1:
               # continue

            #if not 0 <= raster_point[1] <= height - 1:
               # continue

            #set_raster_coordinate(raster_point[0], raster_point[1], 200, 200, 0)
            raster_coordinates.extend(raster_point)
        
        a = [raster_coordinates[0], raster_coordinates[1]]
        b = [raster_coordinates[2], raster_coordinates[3]]
        c = [raster_coordinates[4], raster_coordinates[5]]
        

        v_edge_ab = v2_substract(b, a)
        v_edge_bc = v2_substract(c, b)
        v_edge_ca = v2_substract(a, c)
        #print("raster coordinates: ", raster_coordinates)   

        m2_face = [v_edge_ab[0], v_edge_ab[1], v_edge_ca[0], v_edge_ca[1]]

        face_area = determinant(m2_face)
        
        [bbox_min, bbox_max] = bbox([a,b,c], width, height)

        for y in range (bbox_min[1], bbox_max[1]):
            for x in range(bbox_min[0], bbox_max[0]):
                p = [x, y]
                v_ap = v2_substract(p, a)
                v_bp = v2_substract(p, b)
                v_cp = v2_substract(p, c)

                det_a = determinant(makeMatrix(v_edge_ab, v_ap))
                det_b = determinant(makeMatrix(v_edge_bc, v_bp))
                det_c = determinant(makeMatrix(v_edge_ca, v_cp))

                #Aufgabe 14
                if det_a == 0  and det_b == 0 and det_c == 0:
                    continue

                if det_a >= 0 and det_b >= 0 and det_c >= 0:

                    weight_a = det_b - face_area
                    weight_b = det_c - face_area
                    weight_c = 1 - weight_a - weight_b

                    if not 0 <= p[0] <= width -1:
                        continue
                    if not 0 <= p[1] <= height -1:
                        continue
                    set_raster_coordinate(p[0], p[1], 
                                        int(255 * weight_a),
                                        int(255 * weight_b),
                                        int(255 * weight_c))
                else:
                    pass

    save_ppm(width, height, buffer, t)


