def escribir_el_nombre(*args, **kwargs):
    print("     inicio")
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(key, value)


def buscar_datos(*args, **database):
    for key, person_data in database.items():
        if all(nombre_apellido in person_data.values() for nombre_apellido in args):
            return key
    return None


escribir_el_nombre("Ludmila", primer_nombre="Luciano",
                   segundo_nombre="Cristian",
                   primer_apellido="Toneatti",
                   segundo_apellido="Gandolfo")

escribir_el_nombre(primer_nombre="Nehuen",
                   primer_apellido="Donozo",
                   segundo_apellido="Marquez")

escribir_el_nombre("Francisco", "Facundo", "Emiliano", primer_nombre="Celina",
                   segundo_nombre="Anahi",
                   primer_apellido="Guerra Diaz")

escribir_el_nombre("Raul", "Uva", "Antonio", "Pepe", "Yolanda", "Negra", primer_nombre="Eusebio",
                   primer_apellido="Quinteros")


database = {

            1:{

                "nombre1":"Pablo",

                "nombre2":"Diego",

                "apellido1":"Ruiz",

                "apellido2":"Picasso"

            },

            2:{

                "nombre1":"Elio",

                "apellido1":"Anci"

            },

            3:{

                "nombre1":"Elias",

                "nombre2":"Marcos",

                "nombre3":"Luciano",

                "apellido1":"Marcelo",

                "apellido2":"Gonzalez"

            }

}

id_persona = buscar_datos("Pablo", "Diego", "Ruiz", "Picasso", **database)
print(id_persona)