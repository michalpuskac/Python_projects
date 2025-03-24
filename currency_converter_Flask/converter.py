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

            self.rates = {}
            for line in data[2:]:
                try:
                    parts = line.split("|")
                    currency = parts[3]
                    rate = float(parts[4].replace(",", "."))
                    self.rates[currency] = rate
                except (IndexError, ValueError):
                    print(f"Skipping invalid line: {line}")
            self.rates["CZK"] = 1.0

        except requests.RequestException as e:
            raise ConnectionError(f"Failed to retrieve exchange rates: {str(e)}")


    def convert(self, amount, from_currency, to_currency):
        """Converts an amount from one currency to another based on fetched rates."""
        if not self.rates:
            self.fetch_exchange_rates()
        if from_currency not in self.rates or to_currency not in self.rates:
            raise ValueError(f"Currency not supported: {from_currency} or {to_currency}")

        try:
            return amount * self.rates[from_currency] / self.rates[to_currency]
        except Exception as e:
            raise RuntimeError(f"Conversion error: {str(e)}")