Videojuegos = {
    "mario":"Fontanero que salva a la princesa",
    "sonic":"Erizo que es demasiado rapido",
    "megaman":"Robot que debera salvar al mundo"
}

palabra = input("Digite el nombre del personaje de videojuego: ")
palabra = palabra.lower()

if palabra in Videojuegos.keys():
    # pasa algo
    print(Videojuegos[palabra])
else:
    # pasa algo
    print("Videojuego no encontrado")
