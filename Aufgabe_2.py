import os

def save_ppm(width, height, buffer):
    # Create a path and file and open it for writing
    output_path = os.path.join(os.path.dirname(__file__), "output")
    output_file = os.path.join(output_path, "image.ppm")
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

def set_raster_coordinate(x, y, r, g, b) :
    offset = 3 * x + (width * 3) * y
    buffer[offset] = r
    buffer[offset + 1] = g
    buffer[offset + 2] = b


#perspective divide

def perspective_divide(p, image_plane_distance) :
    return [
        image_plane_distance * p[0] / p[2],
        image_plane_distance * p[1] / p[2],
        image_plane_distance,
    ]


#view space to raster space 
def view_to_raster(v, width, height) :
    raster_X = ((v[0] + 1) / 2) * width
    raster_Y = ((1 - v[1]) / 2) * height

    return [round(raster_X), round(raster_Y)]

#framebuffer
width = 500
height = 500

buffer_length = width * height * 3

buffer = [100] * buffer_length # change brightness 0 (white) - 255 (black)



#project point
# here one can zoom too if you change the values
cube = [
    [-1.0, -1.0, -6],
    [-1.0, 1.0, -6],
    [-1.0, -1.0, -8],
    [-1.0, 1.0, -8],
    [1.0, -1.0, -6],
    [1.0, 1.0, -6],
    [1.0, -1.0, -8],
    [1.0, 1.0, -8],
]

for v in cube :
    screen_space_point = perspective_divide(v, -3) #zoom in or out (the smaller the number = zoom)
    raster_point = view_to_raster(screen_space_point, width, height)
    set_raster_coordinate(raster_point[0], raster_point[1], 255, 20, 147) #change color of points

save_ppm(width, height, buffer)

