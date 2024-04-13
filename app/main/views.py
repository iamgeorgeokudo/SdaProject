from flask import render_template, redirect, request, url_for, flash
from . import main


@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('main/index.html')

@main.route('/about')
def about():
    return render_template('main/about.html')
