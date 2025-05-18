from collections import deque
from model.transactions import Transaction
from view.view import View

list_transactions = deque()
cont = 1
class Control:
    def __init__(self):
        self.view = View()

        self.ejecutar()

    def ejecutar(self):
        while True:
            self.view.show("\n--- Menú ---")
            self.view.show("1. Agregar transacción")
            self.view.show("2. Atender transacción")
            self.view.show("3. Aplazar transacción")
            self.view.show("4. Salir")
            option = self.view.write("Seleccione una opción: ")

            match option:
                case 1:
                    self.add_transaction()
                case 2:
                    self.attend_transaction()
                case 3:
                    self.postpone_transaction()
                case 4:
                    self.view.show("Saliendo del sistema...")
                    break
                case _:
                    self.view.show("Opción no válida, intente de nuevo.")

    def add_transaction(self):
        global cont
        num_trans = 0
        while True:
            if num_trans > 5 or num_trans < 1:
                num_trans = self.view.write("Ingrese el número de transacciones, máximo 5:\t")
                break
            else:
                self.view.show('Número de transacciones no valido, debe ser entre 1 y 5')
                continue
        transaction = Transaction(f'Turno{cont}',num_trans)
        list_transactions.append(transaction)
        cont += 1
        self.view.show(f'Transacción agregada: {transaction.turn} con {transaction.num_transactions} transacciones')
        self.show_transactions()

    def attend_transaction(self):
        if len(list_transactions) > 0:
            list_transactions.popleft()
            self.view.show("Transacción atendida")
            self.show_transactions()
        else:
            self.view.show("No hay transacciones para atender")

    def postpone_transaction(self):
        if len(list_transactions) > 0:
            list_transactions.rotate(-1)
            self.view.show("Transacción aplazada")
            self.show_transactions()
        else:
            self.view.show("No hay transacciones para aplazar")

    def show_transactions(self):
        if len(list_transactions) > 0:
            for transaction in list_transactions:
                self.view.show(f'Turno: {transaction.turn} - Transacciones: {transaction.num_transactions}')