from flask import Flask, url_for, render_template, request

app = Flask(__name__)
@app.route('/')
def index():
    return	'Hello,	World!'

@app.route('/user')
@app.route('/profile')
@app.route('/user/<username>')
@app.route('/profile/<username>', redirect_to="user/<username>")
def user(username=None):
	return (username or "Guest") + " profile!"

@app.route('/catalog/<category_name>/product/<int:product_id>.html')
@app.route('/catalog/<category_name>/product/<int:product_id>')
@app.route('/catalog/', defaults={'category_name': 'new_products', 'product_id': 0})
def product_page(category_name, product_id):
	return "Product from category: " + category_name + ", product ID: " + str(product_id) + "<br/>" + "<a href='" + url_for('index')+ "'>Home</a>"

@app.route('/home/')
def home():
	return render_template('home.html', title='Home page', header='Welcome!', text='Page content')

@app.route('/report/html')
def report_html():
    return render_template('report.html', orders='4', total='100')

@app.route('/report/json')
def report_json():
    return {'orders': 4, 'total': 100}

@app.route('/not_found')
def not_found():
    return "Ooops!", 404

@app.errorhandler(404)
def page_404(error):
    return "404 Not found"

@app.errorhandler(500)
def page_500(error):
    return "Internal Error"

#@app.route('/order/', methods=['GET'])
#def order_get():
#	id = request.args.get('id', 0)
#	return 'Order requested with ID:' + str(id)

@app.route('/order/', methods=['POST'])
def order_post():
    order = {
        'name': request.form.get('name', ''),
        'price': request.form.get('price', 0)
        }
    return "Order created with name " + order.name + " and price " + str(order.price)

