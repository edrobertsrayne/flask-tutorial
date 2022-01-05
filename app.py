from flask import Flask, render_template, url_for
app = Flask(__name__)

app.config['SECRET_KEY'] = 'b9e6d0c2ab9a6a440b0044a0d5121c53'

posts = [
    {
        'author': 'Ed',
        'title': 'Post 1',
        'content': 'First post',
        'date_posted': 'January 4th, 2022'
    },
    {
        'author': 'Pearl',
        'title': 'Post 2',
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
    return render_template('about.html', title='About')


if __name__ == "__main__":
    app.run(debug=True)
