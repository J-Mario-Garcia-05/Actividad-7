def mostrar_datos(estudiantes):
    for carnet, estudiante in estudiantes.items():
        print(f"Carnet: {carnet}")
        print(f"Nombre: {estudiante['nombre']}, Edad: {estudiante['edad']}, carrera: {estudiante['carrera']}")
        print(f"Cursos que recibe {estudiante['nombre']}:")
        for curso, notas in estudiante["cursos"].items():
            print(f"\tCódigo del curso: {curso}")
            print(f"\tNombre del curso: {notas['nombre_curso']}")
            print(f"\tNotas en Tareas: {notas['nota_tarea']}")
            print(f"\tNotas en parciales: {notas['nota_parcial']}")
            print(f"\tNota final: {notas['nota_final']}")
            print(f"\tPromedio: {notas['promedio']}")

estudiantes = {}
opcion = "0"
while opcion != "4":
     print("===MENÚ PRINCIPAL===")
     print("1.Registrar estudiante")
     print("2.Mostrar todos los estudiantes y sus cursos")
     print("3.Buscar estudiante por su carné")
     print("4.Salir")
     opcion = input("\nSeleccione una opción: ")
     match opcion:
         case "1":
             while True:
                 print("Ingrese el dato del estudiante:")
                 carnet = input("Ingrese su carnet: ")
                 if carnet in estudiantes:
                     print("El carné ya se le ha asignado a otro estudiante, intente uno diferente")
                     continue
                 try:
                     nombre = input("Nombre: ")
                     edad = int(input("Edad: "))
                     if 0 > edad or 25 < edad:
                         print("Edad ingresado no válida, repita el ingreso")
                         continue
                     carrera = input("Carrera: ")
                     estudiantes[carnet] = {
                         "nombre": nombre,
                         "edad": edad,
                         "carrera": carrera,
                         "cursos": {}
                     }
                     cantidad_cursos = int(input("Cantidad de cursos que recibe, puede recibir un maximo de 10 cursos: "))
                     if cantidad_cursos > 10 or cantidad_cursos < 1:
                         print("Cantidad de cursos ingresado no valido, repita nuevamente el ingreso.")
                         continue
                     i = 1
                     while i <= cantidad_cursos:
                         codigo_curso = input("\nCódigo del curso: ")
                         nombre_curso = input(f"Nombre del curso {i}: ")
                         nota_tarea = float(input("Nota Tarea: "))
                         if nota_tarea > 100 or nota_tarea < 0:
                             print("Nota fuera de rango")
                             continue
                         nota_parcial = float(input("Nota Parcial: "))
                         if nota_parcial > 100 or nota_parcial < 0:
                             print("Nota fuera de rango")
                             continue
                         nota_final = float(input("Nota Final: "))
                         if nota_final > 100 or nota_final < 0:
                             print("Nota fuera de rango")
                             continue
                         promedio = (nota_tarea + nota_final + nota_parcial) / 3
                         estudiantes[carnet]["cursos"][codigo_curso] = {
                             "nombre_curso": nombre_curso,
                             "nota_tarea": nota_tarea,
                             "nota_parcial": nota_parcial,
                             "nota_final": nota_final,
                             "promedio": promedio,
                         }
                         i += 1
                     print("Se ha registrado con éxito al estudiante")
                 except Exception as e:
                     print("Ha ocurrido un error inesperado: " + str(e))
                 break
         case "2":
             if estudiantes:
                 print("Esrtudiantes registrados:")
                 mostrar_datos(estudiantes)
             else:
                 print("No hay estudiantes registrados.")
         case "3":
             if estudiantes:
                 buscar = input("Ingrese el carné del estudiante que desea buscar: ")
                 if buscar not in estudiantes:
                    print(f"No se encontró algún estudiante que tenga el carné {buscar}")
                    continue
                 print("Datos del estudiante:")
                 print(f"Carnet: {buscar}")
                 print(f"Nombre: {estudiantes[buscar]['nombre']}, Edad: {estudiantes[buscar]['edad']}, carrera: {estudiantes[buscar]['carrera']}")
                 print(f"Cursos que recibe {estudiantes[buscar]['nombre']}:")
                 for curso, notas in estudiantes["cursos"].items():
                     print(f"Código del curso: {curso}")
                     print(f"Nombre del curso: {notas['nombre_curso']}")
                     print(f"\tNotas en Tareas: {notas['nota_tarea']}")
                     print(f"\tNotas en parciales: {notas['nota_parcial']}")
                     print(f"\tNota final: {notas['nota_final']}")
                     print(f"\tPromedio: {notas['promedio']}")
             else:
                 print("No hay estudiantes registrados.")
         case "4":
             print("Saliendo")
         case __:
             print("Opción no válida")