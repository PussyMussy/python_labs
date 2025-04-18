from collections import defaultdict
from datetime import datetime
from flask import Flask, jsonify

app = Flask(__name__)

app.storage = defaultdict(lambda: defaultdict(int))

@app.route('/add/<date>/<int:number>', methods=["POST"])
def add_expense(date, number):
    if number < 0:
        return jsonify({"error": "Expense must be a non-negative integer."}), 400

    try:
        year = int(date[:4])
        month = int(date[4:6])
        day = int(date[6:8])
        datetime(year, month, day)
    except ValueError:
        return jsonify({"error": "Invalid date format. Use YYYYMMDD."}), 400

    app.storage[year][month] += number
    return jsonify({"message": "Expense added successfully"}), 201

@app.route('/calculate/<int:year>', methods=['GET'])
def calculate_year(year):
    if year in app.storage:
        total_expense = sum(app.storage[year].values())
        return jsonify({"year": year, "total_expense": total_expense}), 200
    return jsonify({"year": year, "total_expense": 0}), 200

@app.route('/calculate/<int:year>/<int:month>')
def calculate_month(year, month):
    if year in app.storage:
        total_expense = app.storage[year].get(month, 0)
        return jsonify({"year": year, "month": month, "total_expense": total_expense}), 200
    return jsonify({"year": year, "month": month, "total_expense": 0}), 200

if __name__ == "__main__":
    app.run(debug=True)
