from flask import Flask, render_template, request, redirect, url_for
import shutil
import mysql.connector
from datetime import datetime

app = Flask(__name__)

conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'P@ssw0rd',
    database = 'flaskapp'
)

@app.route('/', methods = ['GET', 'POST'])
def home():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM flaskapp_reviews order by date desc limit 15")
    users = cursor.fetchall()
    cursor.execute("SELECT Distinct Make FROM flaskapp_cars;")
    makes = cursor.fetchall()
    cursor.execute("SELECT Distinct Model FROM flaskapp_cars;")
    models = cursor.fetchall()
    if request.method == 'POST':
        make = request.form['make']
        model = request.form['model']
        cursor = conn.cursor()
        cursor.execute("SELECT *, CONCAT(Make,', ', Model, ', ',Year, '.') AS MMY FROM flaskapp_cars where make = %s OR model = %s", (make, model))
        results = cursor.fetchall()
        return render_template("recommendation.html", results=results)
    return render_template('home.html',users = users, makes = makes, models = models)
       
           
@app.route('/review', methods = ['GET', 'POST'])
def review():
    cursor = conn.cursor()
    #no space after comma, otherwise tuncate when variable return from html
    cursor.execute("SELECT Concat(Make,',',Model,',',Year,'.') as makes FROM flaskapp_cars;") 
    makes = cursor.fetchall()  
    if request.method == 'POST':
        user = request.form['user']
        if user == "":
            user = "Anonymous"
        car = request.form['make']
        mmy = ", ".join(car.split(',')) # compiled with our format.
        date = datetime.now()
        rating = request.form['rating']
        review = request.form['review']
        cursor = conn.cursor()
        cursor.execute('INSERT INTO flaskapp_reviews (User, Car, Date, Rating, Review) values(%s, %s, %s, %s, %s)', (user, mmy, date, rating, review)) 
        conn.commit()
        return redirect(url_for('home', message = "Review Added Successfully!"))
    return render_template('add_review.html', makes = makes)

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
            if photo.filename != '':
                photo.save('static/pictures/' + make +', '+ model + ', ' + year + '.jpg')
            else:
                shutil.copy('static/pictures/template.jpg', 'static/pictures/' + make +', '+ model + ', ' + year + '.jpg')
        return redirect(url_for("home", message = "Car added"))
    return render_template("add_car.html")
        
@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/view', methods = ['GET', 'POST'])
def view_cars():
    cursor = conn.cursor()
    cursor.execute("SELECT *, CONCAT(Make,', ', Model, ', ',Year, '.') AS MMY FROM flaskapp_cars")
    cars = cursor.fetchall()
    cursor.execute("SELECT Distinct Make FROM flaskapp_cars;")
    makes = cursor.fetchall()
    cursor.execute("SELECT Distinct Model FROM flaskapp_cars;")
    models = cursor.fetchall()
    cursor.execute("SELECT Distinct Year FROM flaskapp_cars;")
    years = cursor.fetchall()
    if request.method == "POST":
        make = request.form['make']
        model = request.form['model']
        year = request.form['year']
        cursor = conn.cursor()
        cursor.execute("SELECT *, CONCAT(Make,', ', Model, ', ',Year, '.') AS MMY FROM flaskapp_cars where make = %s OR model = %s OR year = %s", (make, model, year))
        results = cursor.fetchall()
        return render_template("search_results.html", results=results)
    return render_template('view_cars.html', cars = cars, makes = makes, models = models, years = years)

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

@app.route('/useful/<int:id>/<int:likenumber>', methods = ['GET'])
def thumbup(id,likenumber):
    likenumber +=1
    #if request.method == 'POST':
    cursor = conn.cursor()
    cursor.execute('UPDATE flaskapp_reviews set likecount = %s where id = %s', (likenumber, id,)) 
    conn.commit()
    #    return redirect(url_for('home', message = "Review Submitted"))
    return redirect(url_for('home', message = "Like counted"))

@app.route('/useful_one/<int:id>/<int:likenumber>/<MMY>', methods = ['GET'])
def thumbup_one(id,likenumber,MMY):
    likenumber +=1
    cursor = conn.cursor()
    cursor.execute('UPDATE flaskapp_reviews set likecount = %s where id = %s', (likenumber, id,)) 
    conn.commit()
    return redirect(url_for('review_one', MMY=MMY))


@app.route('/review_all/<MMY>', methods = ['GET'])
def review_one(MMY):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM flaskapp_reviews WHERE car = %s", (MMY,))
    reviews = cursor.fetchall()
    return render_template('review_one.html', reviews = reviews, MMY = MMY)


if __name__ == "__main__":
    app.run(debug = True)