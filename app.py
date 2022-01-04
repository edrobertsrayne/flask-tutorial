from flask import Flask, render_template
app = Flask(__name__)


posts = [
    {
        'author': 'Ed',
        'tite': 'Post 1',
        'content': 'First post',
        'date_posted': 'January 4th, 2022'
    },
    {
        'author': 'Pearl',
        'tite': 'Post 2',
        'content': '2nd post',
        'date_posted': 'July 3rd, 2021'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run(debug=True)