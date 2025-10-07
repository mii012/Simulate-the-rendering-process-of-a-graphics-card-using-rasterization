import math
import os

from utils.objLoader import objLoader


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
    print(m)
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

o = objLoader("./humanHead.obj")

width = 200
height = 200
buffer_length = width * height
buffer = [10] * buffer_length * 3


translation =[
            1, 0, 0, 0,
            0, 1, 0, 0,
            0, 0, 1, 0,
            0, 0, -0.3, 1  #untere zeile verändern: verschiedene Positionen des Objekts (x,y,z li -> re)
            ]
            
         
frames = 50
for t in range(0, frames):

    # normalize frame number
    normalized_t = t / frames

    # create eased value
    eased_value = easeInOutCubic(normalized_t)
    # create angle for rotation:
    # scale the normalized value back up, so
    # it fits into the animation range:
    angle = (360 / frames) * (eased_value * frames)

    buffer = [10] * buffer_length * 3

    radians = math.radians(angle)
    rotation = m3_to_m4(rot_x(radians))
    combined = m4_x_m4(rotation, translation)
    
    for index, val in enumerate(o.vertices[::3]):
        start_index = index * 3
        v = [
            o.vertices[start_index],
            o.vertices[start_index + 1],
            o.vertices[start_index + 2],
        ]

        v_transformed = mult_vec3_m4(v, combined)
        if v_transformed[2] > 0:
           continue
        # v_transformed is now homogeneous but with 4th component set to 1.
        # Our perspective_divide function simply ignores it.
        screen_space_point = perspective_divide(v_transformed, -1)
        raster_point = view_to_raster(screen_space_point, width, height)

        if not 0 <= raster_point[0] <= width - 1:
            continue

        if not 0 <= raster_point[1] <= height - 1:
            continue

        set_raster_coordinate(raster_point[0], raster_point[1], 200, 200, 0)

    save_ppm(width, height, buffer, t)