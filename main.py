from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods = ["GET", "POST"])
def contact():
    #if request.method == "POST":
    #    userEmail = request.form.get('userEmail')
    #    print(userEmail)
    #    topic = request.form.get('topic')
    #    print(topic)
    #    sendEmail(userEmail, topic)
    #else:
    #    print(str(request.method))
    return render_template('contact.html')

@app.route("/sponsors")
def sponsors():
    return render_template('sponsors.html')

@app.errorhandler(404)
def pageNotFound(e):
    # note that we set the 404 status explicitly
    return render_template('Error Codes/404NotFound.html'), 404    

if __name__ == '__main__':
    app.run(debug=True)
