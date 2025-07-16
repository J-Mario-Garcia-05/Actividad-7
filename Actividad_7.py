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
             nombre = input("Nombre: ")
             edad = int(input("Edad: "))
             if 0 > edad or 25 > edad:
                 print("Edad ingresado no válida, repita el ingreso")
                 continue
             carrera = input("Carrera: ")
             cantidad_cursos = int(input("Cantidad de cursos que recibe: "))
             for i in range(cantidad_cursos):
                 curso = input(f"Curso {i + 1}: ")