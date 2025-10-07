from utils.objLoader import objLoader

o = objLoader("./humanHead.obj")

for index, value in enumerate(o.faceVertexIndices[::3]): #o.facev ist Liste mit vertex positionen als index
    print(f"Vertex {index}: {value}")
    # Get the vertex position
    v1 = o.faceVertexIndices[index * 3] # x index (die erste zahl des 1. dreiers)
    v2 = o.faceVertexIndices[(index * 3) + 1] # y index (die 1. zahl des 2. dreiers)
    v3 = o.faceVertexIndices[(index * 3) + 2] #  z index (die 1. zahl des 3. dreiers)
    

    print("Vertex-number: ", v1, v2, v3)

    # calculate index for vertex position data
    v_index1 = (v1 -1) * 3
    v_index2 = (v2 -1) * 3
    v_index3 = (v3 -1) * 3
    #raus kommen Referenzen/Indexe auf Koordinaten der Punkte

    print("Punkt1: ", o.vertices[v_index1], o.vertices[v_index1+1], o.vertices[v_index1+2])
    print("Punkt2: ", o.vertices[v_index2], o.vertices[v_index2+1], o.vertices[v_index2+2])
    print("Punkt3: ", o.vertices[v_index3], o.vertices[v_index3+1], o.vertices[v_index3+2])
    # hier werden nach den startindexen geschaut und für y und z zu bekommen, einfach +1 und +2raus kommen x values 
    


    v = [
        o.vertices[v_index1], o.vertices[v_index1 + 1], o.vertices[v_index1 + 2],
        o.vertices[v_index2], o.vertices[v_index2 + 1], o.vertices[v_index2 + 2],
        o.vertices[v_index3], o.vertices[v_index3 + 1], o.vertices[v_index3 + 2]
    ]

    v_transformed = mult_vec3_m4(v, combined2)


#transformation
#perspective divide