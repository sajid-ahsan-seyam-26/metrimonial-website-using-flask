from flask import Flask, render_template, request,redirect,url_for,session
app=Flask(__name__)
app.secret_key="super_secret_matrimony_key"
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
app.route('/')
def index():
    return render_template('index.html')
@app.route('/')
def register():
    if register.method=='POST':
        username=request.form.get('username')
        name=request.form.get('name')
        gender=request.form.get('gender')
        age=request.form.get('age')
        profession=request.get('profession')
        bio=request.get('bio')

        new_profile={
            "username":username,
            "name":name,
            "gender":gender,
            "age":age,
            "profession":profession,
            "bio":bio


        }
        USER_PROFILES.append(new_profile)
        session["logged_in_user"]=username
        session["user_gender"]=gender
        return redirect(url_for('dashboard'))
    return render_template('register.html')
        