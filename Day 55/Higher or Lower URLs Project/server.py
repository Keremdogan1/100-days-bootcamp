from flask import Flask
from random import randint

random = randint(0,9)
app = Flask(__name__)

@app.route('/')
def start():
    return '<h1>Guess a Number between 0 and 9</h1> '\
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'

@app.route('/<int:number>')
def guess(number):
    if number == random:
        return '<h1 style="color:green">You Found Me!</h1>' \
               '<img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExbmhzd3AxcWp4YnFzZzhjaHhqNDc3MGRteHplZjVxOHRtd2Npd3hnMCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/t9igJ3odrXBixqXtgf/giphy.gif">'
    elif number > random:
        return '<h1 style="color:purple">Too high, try again!</h1>' \
               '<img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNjdmdXhwYTA2ZmJ4eDF6MDZsdzI5djU4NTZ3bXJ6MTBiNjl6bzZlMCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/9w9Z2ZOxcbs1a/giphy.gif">'
    elif number < random:
        return '<h1 style="color:red">Too low, try again!</h1>' \
               '<img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNjdmdXhwYTA2ZmJ4eDF6MDZsdzI5djU4NTZ3bXJ6MTBiNjl6bzZlMCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/RYOsjgBkb40E/giphy.gif">'

if __name__ == "__server__":
    app.run(debug=True)