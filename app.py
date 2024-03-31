from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from datetime import datetime
app = Flask(__name__)

conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'P@ssw0rd',
    database = 'flaskapp'
)

@app.route('/')
def home():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM flaskapp_reviews order by date desc limit 15")
    users = cursor.fetchall()
    return render_template('home.html',users = users)

@app.route('/review', methods = ['GET', 'POST'])
def review():
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT Make FROM flaskapp_cars")
    makes = cursor.fetchall()  
    cursor.execute("SELECT DISTINCT Model FROM flaskapp_cars")
    models = cursor.fetchall()
    cursor.execute("SELECT DISTINCT Year FROM flaskapp_cars")
    years = cursor.fetchall()
    if request.method == 'POST':
        user = request.form['user']
        if user == "":
            user = "Anonymous"
        car_tuple = request.form['make'], request.form['model'], request.form['year']
        car = ""
        for cars in car_tuple:
            if cars == car_tuple[-1]:
                car = car + str(cars) + "."
            else:
                car = car + str(cars) + ", "
        date = datetime.now()
        rating = request.form['rating']
        review = request.form['review']
        cursor = conn.cursor()
        cursor.execute('INSERT INTO flaskapp_reviews (User, Car, Date, Rating, Review) values(%s, %s, %s, %s, %s)', (user, car, date, rating, review)) 
        conn.commit()
        return redirect(url_for('home', message = "Review Added Successfully!"))
    return render_template('add_review.html', makes = makes, models = models, years = years)

@app.route('/car', methods = ['GET', 'POST'])
def car():
    if request.method == 'POST':
        make = request.form['make']
        model = request.form['model']
        year = request.form['year']
        cursor = conn.cursor()
        cursor.execute('INSERT INTO flaskapp_cars (Make, Model, Year) values(%s,%s,%s)', (make, model, year))
        conn.commit()
        if 'photo' in request.files:
            photo = request.files['photo']
            photo.save('static/pictures/' + make +', '+ model + ', ' + year + '.jpg')
        return redirect(url_for("home", message = "Car added"))
    return render_template("add_car.html")
        
@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/view')
def view_cars():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM flaskapp_cars")
    cars = cursor.fetchall()
    return render_template('view_cars.html', cars = cars)

@app.route('/pictures/<int:id>', methods = ['GET', 'POST'])
def information(id):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM flaskapp_cars WHERE id = %s", (id,))
    car = cursor.fetchone()
    if request.method == 'POST':
        user = request.form['user']
        if user == "":
            user = "Anonymous"
        car = request.form['car']
        date = datetime.now()
        rating = request.form['rating']
        review = request.form['review']
        cursor = conn.cursor()
        cursor.execute('INSERT INTO flaskapp_reviews (User, Car, Date, Rating, Review) values(%s, %s, %s, %s, %s)', (user, car, date, rating, review)) 
        conn.commit()
        return redirect(url_for('home', message = "Review Submitted"))
    return render_template('car_info.html', car = car)

if __name__ == "__main__":
    app.run(debug = True)