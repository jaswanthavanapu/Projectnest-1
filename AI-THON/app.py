from flask import Flask, render_template,request,redirect,url_for
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['store']
collection = db['users']

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/aboutus')
def about_us():
    return render_template('aboutus.html')

@app.route('/accesories')
def accesories():
    return render_template('accesories.html')

@app.route('/clothing')
def clothing():
    return render_template('clothing.html')

@app.route('/electronics')
def electronics():
    return render_template('electronics.html')

@app.route('/footer')
def footer():
    return render_template('footer.html')

@app.route('/forgetpass')
def forgetpass():
    return render_template('forgetpass.html')

@app.route('/grocery')
def grocery():
    return render_template('grocery.html')
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Handle the login logic here
        username = request.form.get('username')
        password = request.form.get('password')
        # Perform authentication or other necessary actions
        # For now, let's just redirect to the home page
        return redirect(url_for('home'))

    # If it's a GET request, simply render the login page
    return render_template('login.html')


@app.route('/order')
def order():
    return render_template('order.html')

@app.route('/products')
def products():
    return render_template('products.html')

@app.route('/signup', methods=[ 'POST'])
def signup():
    if request.method == 'POST':
        # Extracting user data from the form
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # Creating a dictionary to represent user data
        user_data = {'username': username, 'email': email, 'password': password}

        # Inserting the user data into the 'users' collection
        collection.insert_one(user_data)

        # Redirecting to the login page after successful signup
        return redirect(url_for('login'))

    # Rendering the signup template for GET req

@app.route('/wishlist')
def wishlist():
    return render_template('wishlist.html')

if __name__ == '__main__':
    app.run(debug=True)