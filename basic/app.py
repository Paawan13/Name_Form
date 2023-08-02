from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def form_submission():
    if request.method == 'POST':
        name = request.form['name']
        print(f"Received name: {name}")  # Print the received name
        return redirect(url_for('show', name=name))
    return render_template('form.html')

@app.route('/show/<name>')
def show(name):
    print(f"Your name is: {name}")  # Print the name parameter in the show function
    return render_template('display_data.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)
