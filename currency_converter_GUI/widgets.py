import tkinter as tk
from tkinter import StringVar

# CurrencyDropdown class (as provided in your code)
class CurrencyDropdown:
    def __init__(self, root, currency_var, options, default):
        self.currency_var = StringVar(root)
        self.currency_var.set(default)
        self.dropdown = tk.OptionMenu(root, self.currency_var, *options)
        self.dropdown.config(width=18)
    
    def grid(self, row, column, padx=0, pady=0):
        self.dropdown.grid(row=row, column=column, padx=padx, pady=pady)