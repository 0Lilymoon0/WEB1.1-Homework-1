
# TODO: Follow the assignment instructions to complete the required routes!
# (And make sure to delete this TODO message when you're done!)

from flask import Flask

app = Flask(__name__)

@app.route('/')
def homepage():
    """Shows a greeting to the user."""
    return 'Are you there, world? It\'s me, Ducky!'

@app.route('/penguins')
def penguins():
    return 'Penguins are cute!'

@app.route('/mfa')
def mfa():
    return 'My favorite animal is a wolf!'

@app.route('/animal/<users_animal>')
def favorite_animal(users_animal):
    """Display a message to the user that changes based on their favorite animal."""
    return f'Wow, {users_animal} is my favorite animal, too!'

@app.route('/dessert/<users_dessert>')
def favorite_dessert(users_dessert):
    return f'How did you know I liked {users_dessert}?'

@app.route('/madlibs/<adjective>/<noun>')
def lost_the_cupcake(adjective, noun):
    return f'The {adjective} {noun} claimed they lost their cupcake. (Though it was probably actually lost in their belly)'

@app.route('/multiply/<number1>/<number2>')
def multiply(number1, number2):
    if number1.isdigit() == True and number2.isdigit() == True:
        return f'{number1} times {number2} is {int(number1) * int(number2)}'
    if number1.isdigit() == False or number2.isdigit() == False:
        return f'Invalid inputs. Please try again by entering two numbers!'

if __name__ == '__main__':
    app.run(debug=True)
