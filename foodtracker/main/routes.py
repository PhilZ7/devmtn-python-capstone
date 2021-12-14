from flask import Blueprint, render_template, request, redirect, url_for

from foodtracker.models import Food
from foodtracker.extensions import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')
    # return 'blueprint test'

@main.route('/create_log', methods=['POST'])
def create_log():
    request.form.get('')
    return redirect(url_for('views'))

@main.route('/add')
def add():
    foods = Food.query.all()

    return render_template('add.html', foods=foods, food=None)

@main.route('/add', methods=['POST'])
def add_post():
    food_name = request.form.get('food-name')
    proteins = request.form.get('protein')
    carbs = request.form.get('carbohydrates')
    fats = request.form.get('fat')

    food_id = request.form.get('food-id')

    if food_id:
        food = Food.query.get(food_id)
        food.name = food_name
        food.proteins = proteins
        food.carbs = carbs
        food.fats = fats

    else:
        new_food = Food(
            name=food_name,
            proteins=proteins,
            carbs=carbs,
            fats=fats)

        db.session.add(new_food)

    db.session.commit()

    return redirect(url_for('main.add'))

@main.route('/delete_food/<int:food_id>')
def delete_food(food_id):
    food = Food.query.get(food_id)
    db.session.delete(food)
    db.session.commit()

    return redirect(url_for('main.add'))

@main.route('/edit_food/<int:food_id>')
def edit_food(food_id):
    food = Food.query.get(food_id)
    foods = Food.query.all()
     
    return render_template('add.html', food=food, foods=foods)

@main.route('/view')
def view():
    foods = Food.query.all()

    return render_template('view.html', foods=foods)