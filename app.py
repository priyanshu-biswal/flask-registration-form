from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def register_form():
    return render_template('register.html')

@app.route('/submit', methods=['POST'])
def handle_submission():
    name = request.form.get('name')
    city = request.form.get('city')
    phone = request.form.get('phone')

    return render_template('confirmation.html', name=name, city=city, phone=phone)

if __name__ == '__main__':
    app.run(debug=True)