import tkinter as tk
from converter import CurrencyConverter
from widgets import CurrencyDropdown

class CurrencyConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Currency Converter")
        self.root.geometry("630x250+750+300")
        self.root.resizable(False, False)
        self.root.config(bg="#313131")
        self.root.attributes("-alpha",0.98)
        
        self.converter = CurrencyConverter()  # Instance of converter logic
        
        # GUI setup
        self.create_widgets()

    def create_widgets(self):
        # Input amount entry
        self.input_amount = tk.Entry(self.root, bg="#989899", width=10, font="Helvetica, 15", justify="center")
        self.input_amount.grid(row=0, column=0, padx=50, pady=20)
        self.input_amount.insert(0, "0")

        # Dropdowns
        currency_options = ["CZK - Czech koruna", "USD - United States dollar", "EUR - Euro"]
        self.drop_down_from = CurrencyDropdown(self.root, "CZK - Czech koruna", currency_options, "CZK - Czech koruna")
        self.drop_down_from.grid(row=0, column=1)

        self.drop_down_to = CurrencyDropdown(self.root, "EUR - Euro", currency_options, "EUR - Euro")
        self.drop_down_to.grid(row=1, column=1, pady=15)

        # Button for conversion
        self.change_button = tk.Button(
        self.root, text="Count", font=("Helvetica", 15), command=self.count_exchange, bg="#ecebf2")
        self.change_button.grid(row=0, column=3, padx=20, ipadx=15)

        # Result and notification labels
        self.result_label = tk.Label(self.root, text="0", bg="#989899", width = 10, font=("Helvetica", 15))
        self.result_label.grid(row=1, column=0, padx=50, pady=20)

        self.notification_label = tk.Label(self.root, bg="#313131", fg="red", font=("Helvetica", 13))
        self.notification_label.grid(row=2, column=0,)

    def count_exchange(self):
        try:
            amount = float(self.input_amount.get())
            from_currency = self.drop_down_from.currency_var.get().split(" - ")[0]
            to_currency = self.drop_down_to.currency_var.get().split(" - ")[0]
            result = self.converter.convert(amount, from_currency, to_currency)
            self.result_label.config(text=f"{result:.2f} {to_currency}")
            self.notification_label.config(text="")
        except ValueError as e:
            self.notification_label.config(text=str(e))
        except ConnectionError:
            self.notification_label.config(text="Failed to retrieve exchange rates.")

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = CurrencyConverterApp(root)
    root.mainloop()