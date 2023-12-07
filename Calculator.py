import tkinter as tk
from tkinter import ttk
from math import *

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.geometry("300x400")
        self.configure(bg="#F0F0F0")

        self.create_widgets()

    def create_widgets(self):
        style = ttk.Style()
        style.configure("TButton", font=("Helvetica", 12))

        # Entry widget to display input and results
        self.entry = tk.Entry(self, font=("Helvetica", 18), bd=5, relief=tk.GROOVE, justify=tk.RIGHT)
        self.entry.grid(row=0, column=0, columnspan=4, sticky="nsew", pady=10)

        # Create buttons and add them to the grid
        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("C", 4, 2), ("+", 4, 3),
            ("=", 5, 0, 4),
        ]

        for button_info in buttons:
            self.create_button(*button_info)

        # Configure row and column weights
        for i in range(1, 6):
            self.grid_rowconfigure(i, weight=1)
            self.grid_columnconfigure(i, weight=1)

        # Make the entry widget expand when the window is resized
        self.grid_rowconfigure(0, weight=1)
        for i in range(4):
            self.grid_columnconfigure(i, weight=1)

    def create_button(self, text, row, col, col_span=None):
        button = ttk.Button(self, text=text, width=6, style="TButton", command=lambda t=text: self.on_button_click(t))
        button.grid(row=row, column=col, columnspan=col_span, sticky="nsew", pady=5, padx=5)

    def on_button_click(self, button_text):
        current_text = self.entry.get()

        if button_text == "=":
            try:
                result = eval(current_text)
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        elif button_text == "C":
            self.entry.delete(0, tk.END)
        else:
            self.entry.insert(tk.END, button_text)

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
