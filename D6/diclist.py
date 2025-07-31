agenda = {
    "Pablo": ["666 666 66", "36 78 948 9"],
    "Paco" : ["555 7883 89", "89 0393 939"],
    "Amanda" : ["696969696969696969","888" ]
}

print(f"tlfs:{agenda["Amanda"]}, {agenda["Pablo"]}, {agenda['Paco']}")


users = [
    {"nombre" : "Pablo", "edad": 24, "ciudad": "Galapagar"},
    {"nombre": "Paco", "edad": 33, "ciudad" : "Torrelodones"},
    {"nombre": "Almudena", "edad": 42, "ciudad":"Colmenarejo"}
]
for user in users:
    if user["edad"] > 27:
        print(user["nombre"])