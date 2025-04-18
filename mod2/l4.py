from flask import Flask
from datetime import datetime

app = Flask(__name__)

weeks = {
    0: ('понедельника', 'его'),
    1: ('вторника', 'его'),
    2: ('среды', 'ей'),
    3: ('четверга', 'его'),
    4: ('пятницы', 'ей'),
    5: ('субботы', 'ей'),
    6: ('воскресенья', 'его')
}

@app.route('/hello_world/<name>')
def hello_world(name):
    week = datetime.today().weekday()
    day, good_form = weeks[week]
    greeting = f"Привет, {name}. Хорош{good_form} {day}!"
    return greeting


if __name__ == '__main__':
    app.run(debug=True)