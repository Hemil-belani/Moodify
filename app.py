from flask import Flask, render_template, request, jsonify
# from inference import model
from keras.models import load_model




app = Flask(__name__)

# Load your machine learning model

# model = load_model("model.h5")

# Dummy user database (replace with actual database)
users = {
    'user1@example.com': 'password1',
    'user2@example.com': 'password2'
}

# Route for serving the registration page
@app.route('/', methods=['GET'])
def register_page():
    print("asdfsdf")
    return render_template('register.html')

# Route for handling user registration
@app.route('/register', methods=['POST'])
def register():
    email = request.form['email']
    password = request.form['password']

    # Check if user already exists
    if email in users:
        return jsonify({'error': 'User already exists'})

    # Add new user to database (in this case, just a dictionary)
    users[email] = password

    # Perform ML operations if needed
    # prediction = model.predict(email, password)

    return jsonify({'success': 'User registered successfully'})



# Route for serving the login page
@app.route('/login', methods=['GET'])
def login_page():
    return render_template('login.html')

# Route for handling user login
@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    # Check if user exists and password is correct
    if email in users and users[email] == password:
        # Perform ML operations if needed
        # prediction = model.predict(email, password)

        return jsonify({'success': 'Login successful'})
    else:
        return jsonify({'error': 'Invalid email or password'})

if __name__ == '__main__':
    app.run(debug=True)
