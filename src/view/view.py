import tkinter as tk
from tkinter import simpledialog, messagebox

class View:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Transacciones Bancarias")
        self.root.geometry("800x600")

        # Panel de botones
        self.frame_buttons = tk.Frame(self.root)
        self.frame_buttons.pack(pady=10)

        self.btn_add = tk.Button(self.frame_buttons, text="Agregar transacción", width=20)
        self.btn_add.grid(row=0, column=0, padx=5, pady=5)

        self.btn_attend = tk.Button(self.frame_buttons, text="Atender transacción", width=20)
        self.btn_attend.grid(row=1, column=0, padx=5, pady=5)

        self.btn_attend_all = tk.Button(self.frame_buttons, text="Atender todas", width=20)
        self.btn_attend_all.grid(row=2, column=0, padx=5, pady=5)

        self.btn_postpone = tk.Button(self.frame_buttons, text="Aplazar transacción", width=20)
        self.btn_postpone.grid(row=3, column=0, padx=5, pady=5)

        self.btn_exit = tk.Button(self.frame_buttons, text="Salir", width=20)
        self.btn_exit.grid(row=4, column=0, padx=5, pady=5)

        # Lista de transacciones
        self.label_list = tk.Label(self.root, text="Transacciones:")
        self.label_list.pack()
        self.listbox = tk.Listbox(self.root, width=50)
        self.listbox.pack(pady=10, fill=tk.BOTH, expand=True)

        # Mensaje inferior
        self.status = tk.Label(self.root, text="", fg="blue")
        self.status.pack(pady=5)

    def mainloop(self):
        self.root.mainloop()

    def set_add_command(self, cmd):
        self.btn_add.config(command=cmd)

    def set_attend_command(self, cmd):
        self.btn_attend.config(command=cmd)

    def set_attend_all_command(self, cmd):
        self.btn_attend_all.config(command=cmd)

    def set_postpone_command(self, cmd):
        self.btn_postpone.config(command=cmd)

    def set_exit_command(self, cmd):
        self.btn_exit.config(command=cmd)

    def show(self, text: str):
        self.status.config(text=text)
        self.root.update_idletasks()

    def ask_num_transactions(self):
        while True:
            value = simpledialog.askstring("Agregar transacción", "Ingrese el número de transacciones (1-5):", parent=self.root)
            if value is None:
                return None
            try:
                num = int(value)
                if num >= 1:
                    return num
                else:
                    messagebox.showerror("Error", "Debe ser un número entre mayor a 1.")
            except ValueError:
                messagebox.showerror("Error", "Por favor, ingrese un número válido.")

    def update_transactions(self, transactions):
        self.listbox.delete(0, tk.END)
        for t in transactions:
            self.listbox.insert(tk.END, f"Turno: {t.turn} - Transacciones: {t.num_transactions}")
        self.root.update_idletasks()
