from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
@app.route('/home/')
def home():
    # TODO: missed title?
    return render_template('home.html', title='Posts page', header='Welcome to my blog')

@app.route('/posts/<date>')
def postsbydate(date):
    return render_template('posts.html', title='Posts page', header='Posts ' + date)

@app.route('/post/<sku>.html')
def post(sku):
    return render_template('post.html', title='Post page', header=sku)