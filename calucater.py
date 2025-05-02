from flask import Flask, request, jsonify

app = Flask(__name__)

class Calculator:
    def sum(self, *args):
        return sum(args)
    
    def multiply(self, *args):
        result = 1
        for i in args:
            result *= i
        return result

calc = Calculator()

@app.route('/sum', methods=['POST'])
def calculate_sum():
    data = request.json
    numbers = data.get('numbers', [])
    result = calc.sum(*numbers)
    return jsonify({'sum': result})

@app.route('/multiply', methods=['POST'])
def calculate_multiply():
    data = request.json
    numbers = data.get('numbers', [])
    result = calc.multiply(*numbers)
    return jsonify({'product': result})

if __name__ == '__main__':
    app.run(debug=True)
