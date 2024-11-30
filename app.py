from flask import Flask, render_template, redirect, url_for, flash, request, abort
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from forms import RegistrationForm, LoginForm, SearchForm, BookForm
from models import db, User, Book, Cart
from functools import wraps
from werkzeug.utils import secure_filename
import os
from sqlalchemy.orm import Session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['UPLOAD_FOLDER'] = 'static/uploads'

db.init_app(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or not current_user.is_admin:
            abort(403)
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
def index():
    books = Book.query.all()
    return render_template('index.html', books=books)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        new_user = User(username=form.username.data, email=form.email.data)
        new_user.set_password(form.password.data)
        db.session.add(new_user)
        print(new_user)
        db.session.commit()
        flash('Successfully registered user', 'success')
        return redirect(url_for('index'))  
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter(
            (User.username == form.username.data) | (User.email == form.username.data)
        ).first()

        if user and user.check_password(form.password.data):
            login_user(user)
            flash('Successful login', 'success')

            next_page = request.args.get('next')
            print(f"Redirecting to: {next_page}")  
            return redirect(next_page) if next_page else redirect(url_for('index'))
        else:
            flash('Incorrect username, email or password', 'danger')

    return render_template('login.html', form=form)

@login_manager.user_loader
def load_user(user_id):
    with Session(db.engine) as session:  
        return session.get(User, int(user_id))  

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have logged out!', 'success')
    return redirect(url_for('index'))

@app.route('/search', methods=['GET', 'POST'])
def search():
    form = SearchForm()
    books = []
    if form.validate_on_submit():
        query = form.search.data
        books = Book.query.filter(Book.title.contains(query)).all()
    return render_template('search.html', form=form, books=books)

@app.route('/add_book', methods=['GET', 'POST'])
@login_required
@admin_required
def add_book():
    form = BookForm()
    if form.validate_on_submit():
        if form.image.data:
            image_file = secure_filename(form.image.data.filename)
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], image_file)
            form.image.data.save(image_path)
        else:
            image_file = 'default.jpg'  

        new_book = Book(
            title=form.title.data,
            author=form.author.data,
            price=form.price.data,
            image_file=image_file  
        )
        db.session.add(new_book)
        db.session.commit()
        flash('Product added successfully!', 'success')
        return redirect(url_for('index'))
    return render_template('add_book.html', form=form)

@app.route('/add_to_cart/<int:book_id>', methods=['POST'])
@login_required
def add_to_cart(book_id):
    book = Book.query.get(book_id)
    if book:
        cart_item = Cart.query.filter_by(user_id=current_user.id, book_id=book_id).first()
        if cart_item:
            cart_item.quantity += 1
        else:
            new_item = Cart(user_id=current_user.id, book_id=book_id, quantity=1)
            db.session.add(new_item)
        db.session.commit()
        flash('Added to cart!', 'success')
    return redirect(url_for('index'))

@app.route('/cart', methods=['GET', 'POST'])
@login_required
def cart():
    items = Cart.query.filter_by(user_id=current_user.id).all()
    total = sum(item.book.price * item.quantity for item in items)
    return render_template('cart.html', items=items, total=total)

@app.route('/remove_from_cart/<int:cart_id>', methods=['POST'])
@login_required
def remove_from_cart(cart_id):
    item = Cart.query.get(cart_id)
    if item and item.user_id == current_user.id:
        db.session.delete(item)
        db.session.commit()
        flash('Removed from cart!', 'success')
    return redirect(url_for('cart'))

@app.context_processor
def inject_search_form():
    return {'search_form': SearchForm()}

@app.errorhandler(403)
def forbidden(error):
    return render_template('403.html', error=error), 403

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)