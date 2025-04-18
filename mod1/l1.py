from flask import Flask, render_template
from random import choice
from datetime import datetime
from datetime import timedelta

import re
import os

app = Flask(__name__)

class Counter:
    def __init__(self):
        self.visits = 0

cars = ['Chevrolet', 'Renault', 'Ford', 'Lada']
cats = ['корниш-рекс', 'русская голубая', 'шотландская вислоухая', 'мейн-кун', 'манчкин']
counter = Counter()

with open(os.path.abspath('war_and_peace.txt'), 'r', encoding='utf-8') as file:
    text = file.read()
words = re.findall(r'\b\w+\b', text)

@app.route('/hello_world')
def hello_world():
    return render_template('HelloWorld.html')


@app.route('/cars')
def cars():
    return render_template('Cars.html', cars = cars)

@app.route('/cats')
def cats():
    cat = choice(cats)
    return render_template('Cats.html', cat = cat)


@app.route('/get_time/now')
def get_time_now():
    now = datetime.now()
    time_now = get_time(now.hour, now.minute, now.second)
    return render_template('DateTimeNow.html', current_time = time_now)


@app.route('/get_time/future')
def get_time_future():
    now = datetime.now()
    delta = now + timedelta(hours=1)
    time_future = get_time(delta.hour, delta.minute, delta.second)
    return render_template('DateTimeFuture.html', current_time_after_hour = time_future)


@app.route('/get_random_word')
def get_random_word():
    word = choice(words)
    return render_template('RandomWord.html', random_word = word)


@app.route('/counter')
def counter():
    counter.visits += 1
    return render_template('Counter.html', counter = counter.visits)


def get_time(hours, minutes, seconds):
    return str(hours) + ':' + str(minutes) + ':' + str(seconds)

if __name__ == '__main__':
    app.run(debug = True)