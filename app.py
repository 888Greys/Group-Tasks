from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory data store for student details
students = []

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        # Get form data
        first_name = request.form['first_name']
        second_name = request.form['second_name']
        email = request.form['email']
        phone = request.form['phone']

        # Add to students list
        students.append({
            'First Name': first_name,
            'Second Name': second_name,
            'Email': email,
            'Phone': phone
        })

        return redirect(url_for('table'))
    return render_template('form.html')

@app.route('/table')
def table():
    return render_template('table.html', students=students)

if __name__ == '__main__':
    app.run(debug=True)
