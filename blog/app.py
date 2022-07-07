from flask import Flask, render_template, request, redirect
from news import News

app = Flask(__name__)
news = News()

@app.route('/')
@app.route('/home/')
def home():
    return render_template('home.html', title='Posts page', header='Welcome to my blog')

@app.route('/posts/<date>')
def postsbydate(date):
    return render_template('posts.html', title='Posts page', header='Posts ' + date)

@app.route('/post/<sku>.html')
def post(sku):
    return render_template('post.html', title='Post page', header=sku)

@app.route('/news')
def news_list():
    return render_template('news.html', title="News", header="Our news", news=news.getList())

@app.route('/news', methods=['POST'])
def news_add():
    news.addNews(request.form.get('title', ''), request.form.get('date', ''), request.form.get('body', ''))
    return redirect('/news')