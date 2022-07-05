from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
@app.route('/home/')
def home():
    return render_template('base.html', header='Welcome to my blog', 
    content_header='About my blog')

@app.route('/posts')
def allposts():
    return render_template('base.html', title='Posts page', header='Posts', 
    content_header='All posts')

@app.route('/posts/<date>')
def postsbydate(date):
    return render_template('base.html', title='Posts page', header='Posts {}'.format(date), 
    content_header=date)

@app.route('/post/<sku>.html')
def mypost(sku):
    return render_template('base.html', title='Post page', header='My Post', 
    content_header='My firt post')