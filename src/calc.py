# БПМ-22-1
# Практическая работа №1
# Команда: Кадомцев Андрей, Данила Федуков, Антон Лопаткин

import tkinter as tk
import re
import operator

class NumberBaseCalculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Калькулятор")
        self.current_base = 'DEC'

        self.entry = tk.Entry(master, width=30)
        self.entry.grid(row=0, column=0, columnspan=5)

        self.base_buttons = ['BIN', 'OCT', 'HEX', 'DEC']
        self.operation_buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'B', 'A', '0', '+',
            'E', 'D', 'C', 'Cc',
            '', '', 'F', '=',
        ]

        self.create_buttons()

    def create_buttons(self):
        row = 1
        col = 0

        # Создание кнопок
        self.buttons = {}  # Кнопки для смены сс
        for base_button in self.base_buttons:
            button = tk.Button(self.master, text=base_button, width=5, command=lambda text=base_button: self.change_base(text))
            button.grid(row=row, column=col)

            if base_button == 'DEC':
                button.config(fg='#FF0000')

            self.buttons[base_button] = button 

            col += 1

        row += 1
        col = 0

        for operation_button in self.operation_buttons:
            button = tk.Button(self.master, text=operation_button, width=5, command=lambda text=operation_button: self.on_button_click(text))
            button.grid(row=row, column=col)
            col += 1

            if col > 3:
                col = 0
                row += 1


    def on_button_click(self, text):
        operations = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv,
        }

        if text == '=':
            for base, base_int in [('DEC', 10), ('OCT', 8), ('BIN', 2), ('HEX', 16)]:
                if self.current_base == base:
                    try:
                        first_number, operation, second_number = re.split('(\+|-|\*|/)', self.entry.get().strip())
                        first_number = int(first_number, base_int)
                        second_number = int(second_number, base_int)
                        result = operations[operation](first_number, second_number)
                        if base != 'DEC':
                            if result < 0:
                                result = '-' + {'OCT': oct, 'BIN': bin, 'HEX': hex}[base](abs(result))[2:]
                            else:
                                result = {'OCT': oct, 'BIN': bin, 'HEX': hex}[base](result)[2:]
                        self.entry.delete(0, tk.END)
                        self.entry.insert(tk.END, str(result))
                    except:
                        self.entry.delete(0, tk.END)
                        self.entry.insert(tk.END, "Error")
                    break
        elif text == 'Cc':
            self.entry.delete(0, tk.END)
        else:
            self.entry.insert(tk.END, text)


    def change_base(self, base):
        for button in self.buttons.values():
            button.config(fg='black')

        if base in self.buttons:
            self.buttons[base].config(fg='red')

        self.current_base = base
        self.entry.delete(0, tk.END)


def main():
    root = tk.Tk()
    app = NumberBaseCalculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()