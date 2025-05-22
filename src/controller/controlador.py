from collections import deque
from model.transactions import Transaction
from view.view import View

list_transactions = deque()
cont = 1
class Control:
    def __init__(self):
        self.view = View()
        self.view.set_add_command(self.add_transaction)
        self.view.set_attend_command(self.attend_transaction)
        self.view.set_attend_all_command(self.attend_all_transactions)
        self.view.set_postpone_command(self.postpone_transaction)
        self.view.set_exit_command(self.exit_program)
        self.update_view()
        self.view.mainloop()

    def update_view(self):
        self.view.update_transactions(list_transactions)

    def add_transaction(self):
        global cont
        num_trans = self.view.ask_num_transactions()
        if num_trans is None:
            self.view.show("Operación cancelada.")
            return
        transaction = Transaction(f'Turno{cont}', num_trans)
        list_transactions.append(transaction)
        cont += 1
        self.view.show(f'Transacción agregada: {transaction.turn} con {transaction.num_transactions} transacciones')
        self.update_view()

    def attend_transaction(self):
        if len(list_transactions) == 0:
            self.view.show("No hay transacciones para atender")
            return
        transaction = list_transactions[0]
        if transaction.num_transactions > 5:
            transaction.num_transactions -= 5
            self.view.show(f"Se atendieron 5 transacciones de {transaction.turn}. Restan {transaction.num_transactions}.")
            self.postpone_transaction()
        else:
            list_transactions.popleft()
            self.view.show(f"Transacción {transaction.turn} atendida completamente.")
        self.update_view()

    def postpone_transaction(self):
        if len(list_transactions) > 0:
            list_transactions.rotate(-1)
            self.view.show("Transacción aplazada")
            self.update_view()
        else:
            self.view.show("No hay transacciones para aplazar")

    def exit_program(self):
        self.view.root.destroy()

    def attend_all_transactions(self):
        if len(list_transactions) == 0:
            self.view.show("No hay transacciones para atender")
            return
        self._attend_all_step()

    def _attend_all_step(self):
        if len(list_transactions) == 0:
            self.view.show("Todas las transacciones han sido atendidas")
            return
        self.attend_transaction()
        self.view.root.after(3000, self._attend_all_step)