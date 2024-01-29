from app import app
from flask import render_template, flash, redirect
from app.forms import RegisterForm, AddProductForm


@app.route('/')
@app.route('/index')
def index():
    """Index URL"""
    return render_template('index.html', title='Index Page')


@app.route('/about-me')
def about_me():
    """About me URL"""
    return render_template('about_me.html', title='about me page')


@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
    """Product URL"""
    form = AddProductForm()
    if form.validate_on_submit():
        flash(f'Your product has been saved {form.product_name.data}')
        return redirect('/index')
    return render_template('add_product.html', title='Add Product', form=form)


@app.route('/register', methods=['GET', 'POST'])
def re4():
    """Register URL"""
    form = RegisterForm()
    if form.validate_on_submit():
        flash(f'You are requesting to login in {form.username.data}')
        return redirect('/index')
    return render_template('register.html', title='Register', form=form)