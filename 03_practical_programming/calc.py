import tkinter as tk

# This was added as an extra example intended to give you more reference 
# code for your project
# 
# This example demonstrates the following concepts:
#   - Object-oriented Programming (OOP)
#   - Graphical User Interfaces with tkinter

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Calculator')
        self.resizable(True, True)
        self._expr = ''
        self._build()

    def _build(self):
        self.display = tk.Entry(
            self,
            font=('Monospace', 22),
            justify='right',
            state='readonly',
            readonlybackground='white'
        )
        self.display.grid(row=0, column=0, columnspan=4, sticky='nsew', padx=4, pady=4)

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('+', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('/', 4, 3),
        ]

        for text, row, col in buttons:
            tk.Button(
                self,
                text=text,
                font=('Monospace', 18),
                command=lambda t = text: self._press(t),
            ).grid(row=row, column=col, sticky='nsew', padx=2, pady=2)

        for i in range(6):
            self.grid_rowconfigure(i, weight=1)
        
        for j in range(4):
            self.grid_columnconfigure(j, weight=1)
        
    def _set_display(self, text):
        self.display.config(state='normal')
        self.display.delete(0, tk.END)
        self.display.insert(0, text)
        self.display.config(state='readonly')
    
    def _press(self, token):
        if token == '=':
            try:
                self._expr = str(eval(self._expr))
            except ZeroDivisionError:
                self._expr = 'Error'
            except Exception:
                self._expr = 'Error'
        else:
            if self._expr == 'Error':
                self._expr = ''
            self._expr += token 
        self._set_display(self._expr)
    
    def _clear(self):
        self._expr = ''
        self._set_display('')

if __name__ == '__main__':
    Calculator().mainloop()