''' unvollständig, aber wichtige Kommentare

for index, value in enumerate(o.faceVertexIndices[::3]): #o.facev ist Liste mit vertex positionen als index
    #print(f"Vertex {index}: {value}")
    # Get the vertex position
    v1 = o.faceVertexIndices[index * 3] # x index (die erste zahl des 1. dreiers)
    v2 = o.faceVertexIndices[(index * 3) + 1] # y index (die 1. zahl des 2. dreiers)
    v3 = o.faceVertexIndices[(index * 3) + 2] #  z index (die 1. zahl des 3. dreiers)
    

    #print("Vertex-number: ", v1, v2, v3)

    # calculate index for vertex position data
    v_index1 = (v1 -1) * 3
    v_index2 = (v2 -1) * 3
    v_index3 = (v3 -1) * 3
    #raus kommen Referenzen/Indexe auf Koordinaten der Punkte
            
         

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


    # loop over faces:
    for index, val in enumerate(o.faceVertexIndices[::3]):
    #   v = [x,y,z,x,y,z,x,y,z] (komisches schaubild wo ich und koko lang dran saßen)
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


    #   rasterpoints = []
        raster_coordinates = []
    #   for index, val in enumerate(v[::3]):
        for index, val in enumerate(v_faces[::3]):
            start_index = index * 3
                
            #raster koordinaten werden erstellt
            v = [
                v_faces[start_index],
                v_faces[start_index + 1],
                v_faces[start_index + 2]
            ]

    #       transformation
            v_transformed = mult_vec3_m4(v, combined)
             
    #       projektion
            screen_space_point = perspective_divide(v_transformed, -1)

    #       raster_point = raster coordinates
            raster_point = view_to_raster(screen_space_point, width, height)

    #       rasterpoints.extend(raster_point)
            raster_coordinates.extend(raster_point)

            print(raster_point)  




for y in range 

'''  

  