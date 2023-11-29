#quiz1

from flask import Flask, jsonify

app = Flask(__name__)

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

@app.route('/prime_number/<int:number>', methods=['GET'])
def check_prime(number):
    result = {"Number": number, "isPrime": is_prime(number)}
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)

#quiz2

from flask import Flask, jsonify

app = Flask(__name__)


airport_database = {
    "EFHK": {"Name": "Helsinki-Vantaa Airport", "Location": "Helsinki"},
    "EGLL": {"Name": "Heathrow Airport", "Location": "London"},
    # Add more airports as needed
}

@app.route('/airport/<icao>', methods=['GET'])
def get_airport_info(icao):
    airport_info = airport_database.get(icao.upper())

    if airport_info:
        result = {"ICAO": icao.upper(), "Name": airport_info["Name"], "Location": airport_info["Location"]}
        return jsonify(result)
    else:
        return jsonify({"error": "Airport not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)

