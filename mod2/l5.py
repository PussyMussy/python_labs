from flask import Flask, jsonify
from werkzeug.exceptions import BadRequest


app = Flask(__name__)


@app.route('/max_number/<path:numbers>')
def max_number(numbers):
    numbers_list = numbers.split('/')
    try:
        int_numbers = [int(num) for num in numbers_list]
    except ValueError:
        raise BadRequest("Все перечисленные значения должны быть числами")
    
    max_num = max(int_numbers)

    response = f"Максимальное число: <i>{max_num}</i>"
    return response


if __name__ == '__main__':
    app.run(debug=True)