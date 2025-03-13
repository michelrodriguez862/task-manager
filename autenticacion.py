import requests
import sys

tareas = []

def autenticar_usuario(username, password):
    url = f"https://httpbin.org/basic-auth/{username}/{password}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return True
    return False


def obtener_credenciales():
    intentos = 0
    while intentos < 3:
        username = input("Ingrese su nombre de usuario: ")
        password = input("Ingrese su contraseña: ")
        
        if autenticar_usuario(username, password):
            print("Autenticación exitosa.")
            return True
        else:
            print("Credenciales incorrectas. Intente nuevamente.")
            intentos += 1
    
    print("Número máximo de intentos alcanzado. Acceso denegado.")
    return False


def agregar_tarea():
    titulo = input("Ingrese el título de la tarea: ")
    tarea = {"titulo": titulo, "estado": "pendiente"}
    tareas.append(tarea)
    print(f"Tarea '{titulo}' agregada.")


def listar_tareas():
    if tareas:
        for index, tarea in enumerate(tareas, start=1):
            print(f"{index}. {tarea['titulo']} [{tarea['estado']}]")
    else:
        print("No hay tareas registradas.")


def eliminar_tarea():
    titulo = input("Ingrese el título de la tarea a eliminar: ")
    tarea_encontrada = False
    for tarea in tareas:
        if tarea['titulo'] == titulo:
            tareas.remove(tarea)
            print(f"Tarea '{titulo}' eliminada.")
            tarea_encontrada = True
            break
    if not tarea_encontrada:
        print(f"No se encontró ninguna tarea con el título '{titulo}'.")


def mostrar_menu():
    while True:
        print("\n--- Menú de Gestión de Tareas ---")
        print("1. Agregar tarea")
        print("2. Listar tareas")
        print("3. Eliminar tarea")
        print("4. Salir")
        
        opcion = input("Elija una opción (1-4): ")
        
        if opcion == "1":
            agregar_tarea()
        elif opcion == "2":
            listar_tareas()
        elif opcion == "3":
            eliminar_tarea()
        elif opcion == "4":
            print("Saliendo del programa.")
            sys.exit(0)
        else:
            print("Opción no válida. Por favor, elija una opción del 1 al 4.")


def main():
    
    if obtener_credenciales():
        mostrar_menu()

if __name__ == "__main__":
    main()
