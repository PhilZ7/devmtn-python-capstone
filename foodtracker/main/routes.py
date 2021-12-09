from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('/templates/index.html')

@main.route('/add')
def add():
    return render_template('/templates/add.html')

@main.route('/view')
def view():
    return render_template('/templates/view.html')