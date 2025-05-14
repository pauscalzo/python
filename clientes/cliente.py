class Cliente:
    def __init__(self, nombre, apellido, email, saldo=0):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.saldo = saldo

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.email})"

    def agregar_credito(self, monto):
        self.saldo += monto
        print(f"{self.nombre} ahora tiene un saldo de ${self.saldo}")

    def realizar_compra(self, monto):
        if self.saldo >= monto:
            self.saldo -= monto
            print(f"{self.nombre} realizó una compra de ${monto}. Saldo restante: ${self.saldo}")
        else:
            print(f"Fondos insuficientes para realizar la compra.")
