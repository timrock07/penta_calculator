import tkinter as tk
from tkinter import messagebox
import math

class CalculatorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("電卓")

        self.result_var = tk.StringVar()
        self.result_var.set("")

        self.result_entry = tk.Entry(
            self, textvariable=self.result_var, font=('Meiryo UI', 18), bd=10, insertwidth=4, width=14, justify='right')
        
        self.result_entry.grid(row=0, column=0, columnspan=4)

        buttons = [

            ('√', 1, 0), ('(', 1, 1), (')', 1, 2), ('C', 1, 3),('z', 1, 4),
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('÷', 2, 3), ('t', 2, 4), 
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('×', 3, 3), ('χ', 3, 4),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('-', 4, 3), ('F', 4, 4),
            ('0', 5, 0), ('.', 5, 1), ('=', 5, 2), ('+', 5, 3), ('AC', 5, 4)

        ]

        for (text, row, column) in buttons:
            if text == 'AC':
                tk.Button(
                    self, 
                    text=text, 
                    font=('Meiryo UI', 14), 
                    height=2, 
                    width=5, 
                    command=self.clear_entry).grid(row=row, column=column)
            elif text == '√':
                tk.Button(
                    self, 
                    text=text, 
                    font=('Meiryo UI', 14), 
                    height=2, 
                    width=5, 
                    command=self.calculate_square_root).grid(row=row, column=column)
            elif text in {'z', 't', 'χ', 'F'}:
                tk.Button(
                    self, 
                    text=text, 
                    font=('Meiryo UI', 14), 
                    height=2, 
                    width=5, 
                    command=lambda t=text: self.open_mode(t)).grid(row=row, column=column)
            elif text == 'C':
                tk.Button(
                    self, 
                    text=text, 
                    font=('Meiryo UI', 14), 
                    height=2, 
                    width=5, 
                    command=self.clear_last_entry).grid(row=row, column=column)
            else:
                tk.Button(
                    self, 
                    text=text, 
                    font=('Meiryo UI', 14), 
                    height=2, 
                    width=5, 
                    command=lambda t=text: self.button_click(t)).grid(row=row, column=column)

        self.bind('<Return>', lambda event=None: self.button_click('='))

    def button_click(self, button):
        current_expression = self.result_var.get()

        if button == '=':
            try:
                current_expression = current_expression.replace('×', '*')
                current_expression = current_expression.replace('÷', '/')
                result = eval(current_expression)
                self.result_var.set(str(result))
            except Exception as e:
                messagebox.showerror("エラー", f"計算エラー: {e}")
        else:
            self.result_var.set(current_expression + button)
    
    def clear_entry(self):
        self.result_var.set("")
    
    def clear_last_entry(self):
        current_expression = self.result_var.get()
        if current_expression:
            self.result_var.set(current_expression[:-1])
    
    def calculate_square_root(self):
        current_expression = self.result_var.get()
        try:
            result = math.sqrt(float(current_expression))
            self.result_var.set(str(result))
        except ValueError:
            messagebox.showerror("エラー", "有効な数値を入力してください")
    
    def open_mode(self, mode):
        print(f"Open mode: {mode}") 
        if mode == 'z':
            import z
            z.main()
        elif mode == 't':
            import t
            t.main()
        elif mode == 'χ':
            import chi
            chi.main()
        elif mode == 'F':
            import f
            f.main()

if __name__ == "__main__":
    app = CalculatorApp()
    app.mainloop()