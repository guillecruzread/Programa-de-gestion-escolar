alumnos={"Alumnos": []} #diccionario

def agregar_alumno(datos):
    nuevo_alumno ={"Nombre": input("Nombre: "),
                   "Apellido": input("Apellido: "),
                   "DNI": int(input("DNI: ")),
                   "Fecha de nacimiento": input("Fecha de nacimiento -> dia/mes/año: "),
                   "Tutor": input("Nombre del Tutor: "),
                   "Notas": input("Ingrese las notas separadas por coma (ej: 8,7,10): "), 
                   "Faltas": int(input("Faltas: ")),
                   "amonestaciones": int(input("Amonestaciones:"))}
    
    datos["Alumnos"].append(nuevo_alumno) #no puedo poner alumnos.append pq no esuna lista, si no un diccionario.
    print("Alumno guardado ")

agregar_alumno(alumnos) #esto hace que ahora el diccionario principal pase de ser alumnos a datos, y Alumnos es una lista
print(alumnos) #hice una fucion q contenga un diccionario de un alumno y sus datos
               #con append agrego ese diccionario al anterior a la lista "Alumnos"->imprimo la lista "alumnos" con el nuevo alumno y sus datos
            
def mostrar_alumno(datos):
    for alumno in datos["Alumnos"]: #datos["Alumnos"] es la lista
        print(f"Alumno: {alumno['Nombre']} {alumno['Apellido']}, DNI: {alumno['DNI']}")
        print(f"Notas: {alumno['Notas']} | Faltas: {alumno['Faltas']}")
        print("-" * 20)