import os

def save_ppm(frame) : 
    output_path = os.path.join(os.path.dirname(__file__), "output")
    output_file = os.path.join(output_path, "image.{f}.ppm".format(f=frame))
    os.makedirs(output_path, exist_ok=True)
    ppm_file = open(output_file, "w")
    print("save PPM")

    width = 256
    height = 256
    header = "P3\n{w} {h}\n255\n".format(w=width, h=height)
    ppm_file.write(header)

    for x in range(0, width) :
        for y in range(0, height) :
            red = (x + frame) % 256
            green = (x + y + frame) % 256
            blue = (y + frame) % 256
            value =" {r} {g} {b} ".format(r=red, g=green, b=blue)
            #value = " {r} {g} {b} ".format(r=x, g=y, b=0) x and y values, no blue values (0) 
            ppm_file.write(value)

    
    ppm_file.close()

start = 0
end = 255
for t in range(start, end):
    print("Frame: ", t)
    save_ppm(t)

#save_ppm()


