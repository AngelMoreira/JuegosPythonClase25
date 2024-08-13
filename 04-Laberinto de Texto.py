def laberinto():
    laberinto = {
        "entrada": {"norte": "pasillo", "sur": None, "este": None, "oeste": None},
        "pasillo": {"norte": "biblioteca", "sur": "entrada", "este": "cuarto oscuro", "oeste": "oficina"},
        "cuarto oscuro": {"norte": None, "sur": None, "este": None, "oeste": "pasillo"},
        "oficina": {"norte": None, "sur": None, "este": "pasillo", "oeste": "almacen"},
        "almacen": {"norte": None, "sur": None, "este": "oficina", "oeste": None},
        "biblioteca": {"norte": "salon", "sur": "pasillo", "este": None, "oeste": None},
        "salon": {"norte": "salida", "sur": "biblioteca", "este": None, "oeste": "jardin"},
        "jardin": {"norte": None, "sur": None, "este": "salon", "oeste": "bodega"},
        "bodega": {"norte": None, "sur": None, "este": "jardin", "oeste": None},
        "salida": {"norte": None, "sur": "salon", "este": None, "oeste": None},
    }
    
    posicion_actual = "entrada"
    print("¡Bienvenido al laberinto! Tienes que encontrar la salida.")

    while True:
        direccion = input(f"Estás en {posicion_actual}. Puedes ir hacia: {list(laberinto[posicion_actual].keys())}. ¿Hacia dónde vas? ").lower()

        if direccion in laberinto[posicion_actual] and laberinto[posicion_actual][direccion]:
            posicion_actual = laberinto[posicion_actual][direccion]
            if posicion_actual == "salida":
                print("¡Felicidades, encontraste la salida!")
                break
        else:
            print("No puedes ir en esa dirección, intenta de nuevo.")

laberinto()
