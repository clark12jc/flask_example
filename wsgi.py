from flask import Flask, render_template

app = Flask(__name__,
            template_folder='templates',
            static_folder='static')
agency = 'U.S. Department of Labor'


@app.route('/')
def home():
    """Landing page."""
    return render_template('home.html',
                           title=agency,
                           description="Smarter page templates \
                                with Flask & Jinja.")


@app.route('/demo')
def demo():
    """Demo page."""
    return render_template('demo.html',
                           title=agency,
                           h1='Page Title',
                           description="Smarter page templates \
                                with Flask & Jinja.")


@app.route('/sidenav')
def demo_sidenav():
    """Sidenav page."""
    return render_template('demo_sidenav.html',
                           title=agency,
                           h1='Page Title',
                           description="Smarter page templates \
                                with Flask & Jinja.")


@app.route('/login')
def login():
    """Sidenav page."""
    return render_template('login.html',
                           title=agency
                           )


if __name__ == '__main__':
    app.run(debug=True)
