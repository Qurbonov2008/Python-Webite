from flask import Flask , render_template , url_for


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/service')
def service():
    return render_template('service.html')


@app.route('/feature')
def feature():
    return render_template('future.html')



@app.route('/team')
def team():
    return render_template('team.html')


@app.route('/appointment')
def appointment():
    return render_template('appointment.html')


@app.route('/testimonial')
def testimonial():
    return render_template('testimonial.html')


@app.route('/not_found')
def not_found():
    return render_template('not_found.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True , port=8000)

