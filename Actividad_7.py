estuiantes = {}
opcion = "0"
while opcion != "4":
     print("===MENÚ PRINCIPAL===")
     print("1.Registrar estudiante")
     print("2.Mostrar todos los estudiantes y sus cursos")
     print("3.Buscar estudiante por su carné")
     print("4.Salir")
     opcion = input("Seleccione una opción: ")
     match opcion:
         case "1":
             print("Ingrese el dato del estudiante:")
             carnet = input("Ingrese su carnet: ")
             if carnet in estuiantes:
                 print("El carné ya se le ha asignado a otro estudiante, intente uno diferente")
                 continue
             nombre = input("Nombre: ")
             edad = int(input("Edad: "))
             if 0 > edad or 25 > edad:
                 print("Edad ingresado no válida, repita el ingreso")
                 continue
             carrera = input("Carrera: ")
             estuiantes[carnet] = {
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
                 nombre_curso = input(f"Curso {i + 1}: ")
                 nota_tarea = float(input("Nota Tarea: "))
                 nota_parcial = float(input("Nota Parcial: "))
                 nota_final = float(input("Nota Final: "))
                 estuiantes[carnet]["cursos"][nombre_curso] = {
                     "nota_tarea": nota_tarea,
                     "nota_parcial": nota_parcial,
                     "nota_final": nota_final,
                 }
                 i += 1
             print("Se ha registrado con éxito al estudiante")
