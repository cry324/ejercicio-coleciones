"""
Tarea práctica - Semana 15
Colecciones de datos: Agenda de contactos usando un diccionario

Problema de la vida real: guardar contactos (nombre y número telefónico),
mostrarlos, agregar nuevos y poder buscar uno por nombre.
"""


def agregar_contacto(agenda: dict, nombre: str, telefono: str) -> None:
    """Agrega un contacto nuevo a la agenda."""
    agenda[nombre] = telefono
    print(f"Contacto agregado: {nombre} - {telefono}")


def mostrar_contactos(agenda: dict) -> None:
    """Muestra todos los contactos guardados en la agenda."""
    if not agenda:
        print("La agenda está vacía.")
        return

    print("\n--- Lista de contactos ---")
    for nombre, telefono in agenda.items():
        print(f"{nombre}: {telefono}")
    print("---------------------------\n")


def buscar_contacto(agenda: dict, nombre: str) -> None:
    """Busca un contacto por su nombre y muestra el resultado."""
    if nombre in agenda:
        print(f"{nombre} encontrado, número: {agenda[nombre]}")
    else:
        print(f"No se encontró ningún contacto llamado {nombre}.")


def eliminar_contacto(agenda: dict, nombre: str) -> None:
    """Elimina un contacto de la agenda si existe."""
    if nombre in agenda:
        del agenda[nombre]
        print(f"Contacto {nombre} eliminado.")
    else:
        print(f"No se encontró {nombre} para eliminar.")


def main() -> None:
    agenda: dict = {}

    # Agregamos algunos contactos de ejemplo
    agregar_contacto(agenda, "Ana Torres", "0991234567")
    agregar_contacto(agenda, "Luis Pérez", "0987654321")
    agregar_contacto(agenda, "María Gómez", "0965432189")

    # Mostramos toda la agenda
    mostrar_contactos(agenda)

    # Buscamos un contacto
    buscar_contacto(agenda, "Luis Pérez")
    buscar_contacto(agenda, "Carlos Ruiz")

    # Eliminamos un contacto y volvemos a mostrar la agenda
    eliminar_contacto(agenda, "Ana Torres")
    mostrar_contactos(agenda)


if __name__ == "__main__":
    main()
