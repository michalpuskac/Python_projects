import requests

class CurrencyConverter:
    API_URL = "https://www.cnb.cz/en/financial-markets/foreign-exchange-market/central-bank-exchange-rate-fixing/central-bank-exchange-rate-fixing/daily.txt"

    def __init__(self):
        self.rates = {}

    def fetch_exchange_rates(self):
        """Fetches exchange rates from the CNB API and updates the rates dictionary."""
        try:
            response = requests.get(self.API_URL)
            response.raise_for_status()
            data = response.text.splitlines()
            
            self.rates = {
                line.split("|")[3]: float(line.split("|")[4].replace(",", "."))
                for line in data[2:]
            }
            self.rates["CZK"] = 1.0

        except requests.RequestException:
            raise ConnectionError("Failed to retrieve exchange rates.")

    def convert(self, amount, from_currency, to_currency):
        """Converts an amount from one currency to another based on fetched rates."""
        if not self.rates:
            self.fetch_exchange_rates()
        
        if from_currency in self.rates and to_currency in self.rates:
            return amount * self.rates[from_currency] / self.rates[to_currency]
        else:
            raise ValueError("Currency not supported")
