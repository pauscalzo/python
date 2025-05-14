from clientes.cliente import Cliente
from clientes.sistema import login

def ejecutar():
    if login():
        usuario = input("Reingresá tu nombre para crear el cliente: ")  
        apellido = input("Ingresá tu apellido: ")
        email = input("Ingresá tu email: ")
        try:
            saldo_inicial = float(input("Saldo inicial: "))
        except ValueError:
            print("Saldo inválido, se usará 0 por defecto.")
            saldo_inicial = 0

        cliente = Cliente(usuario, apellido, email, saldo_inicial)
        print(f"\nCliente cargado: {cliente}")


        while True:
            print("\n--- Menú del Cliente ---")
            print("1. Ver saldo")
            print("2. Agregar crédito")
            print("3. Realizar compra")
            print("4. Salir")

            opcion = input("Elegí una opción: ")

            if opcion == "1":
                print(f"Saldo actual: ${cliente.saldo}")
            elif opcion == "2":
                try:
                    monto = float(input("¿Cuánto querés agregar?: "))
                    cliente.agregar_credito(monto)
                except ValueError:
                    print("Por favor, ingresá un número válido.")
            elif opcion == "3":
                try:
                    monto = float(input("¿Cuánto cuesta la compra?: "))
                    cliente.realizar_compra(monto)
                except ValueError:
                    print("Por favor, ingresá un número válido.")
            elif opcion == "4":
                print("¡Gracias por usar el sistema!")
                break
            else:
                print("Opción inválida.")

if __name__ == "__main__":
    ejecutar()


