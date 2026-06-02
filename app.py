from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
# Secret key is required to use sessions (keeping users logged in)
app.secret_key = "super_secret_matrimony_key"

# Dummy database simulating registered users
# Pre-populated with a few profiles for immediate testing
USER_PROFILES = [
    {
        "username": "rahim",
        "name": "Rahim Uddin",
        "gender": "Male",
        "age": "27",
        "profession": "Software Engineer",
        "bio": "Looking for someone who loves music and traveling."
    },
    {
        "username": "nusrat",
        "name": "Nusrat Jahan",
        "gender": "Female",
        "age": "25",
        "profession": "Doctor",
        "bio": "Family-oriented, passionate about reading and helping others."
    },
    {
        "username": "arif",
        "name": "Arif Ahmed",
        "gender": "Male",
        "age": "29",
        "profession": "Banker",
        "bio": "Simple guy looking for a life partner."
    },
    {
        "username": "sadia",
        "name": "Sadia Islam",
        "gender": "Female",
        "age": "24",
        "profession": "Lecturer",
        "bio": "Enjoys teaching, photography, and exploring nature."
    }
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Grab data from the HTML form
        username = request.form.get('username')
        name = request.form.get('name')
        gender = request.form.get('gender')
        age = request.form.get('age')
        profession = request.form.get('profession')
        bio = request.form.get('bio')
        
        # Create a new profile dictionary
        new_profile = {
            "username": username,
            "name": name,
            "gender": gender,
            "age": age,
            "profession": profession,
            "bio": bio
        }
        
        # Add to our fake database
        USER_PROFILES.append(new_profile)
        
        # Log the user into the session automatically
        session['logged_in_user'] = username
        session['user_gender'] = gender
        
        return redirect(url_for('dashboard'))
        
    return render_template('register.html')

@app.route('/dashboard')
def dashboard():
    # If a user tries to access dashboard without registering/logging in, send them home
    if 'logged_in_user' not in session:
        return redirect(url_for('index'))
    
    current_username = session['logged_in_user']
    current_gender = session['user_gender']
    
    # Find the current user's full details
    user_info = None
    for profile in USER_PROFILES:
        if profile['username'] == current_username:
            user_info = profile
            break

    # Find matches (Opposite gender)
    matches = []
    for profile in USER_PROFILES:
        if profile['gender'] != current_gender:
            matches.append(profile)
            
    return render_template('dashboard.html', user=user_info, matches=matches)

@app.route('/logout')
def logout():
    # Clear the session data
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)