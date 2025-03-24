from flask import Flask, jsonify, render_template, request
from converter import CurrencyConverter

app = Flask(__name__)
converter = CurrencyConverter()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/convert", methods=["POST"])
def convert_currency():
    try:
        data = request.get_json()
        print(f"DEBUG: Received data: {data}")
        if not data:
            return jsonify({"error": "Invalid input"}), 400
        
        amount = float(data["amount"])
        from_currency = data["from_currency"]
        to_currency = data["to_currency"]

        result = converter.convert(amount, from_currency, to_currency)
        
        json_response = {"result": f"{result:.2f} {to_currency}"}
        return jsonify(json_response)

    except Exception as e:
        print(f"DEBUG: Error: {e}")
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)