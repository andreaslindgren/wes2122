from my_server import app
from flask import render_template, request

@app.route('/')
def start():
    return render_template('index.html')

# Add user
@app.route('/user/add', methods=['GET', 'PUT'])
def add_user():
    if request.method == 'GET':
        return render_template('add_user.html')
    
    name = request.form['name']
    email = request.form['email']

    new_user = User(name, email)
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('list_users'))


@app.route('/user/list')
def list_users():
    pass

# # Get all products
# @app.route('/product', methods=['GET'])
# def get_products():
#     all_products = Product.query.all()
#     result = products_schema.dump(all_products)
#     return jsonify(result)


# # Get single products
# @app.route('/product/<id>', methods=['GET'])
# def get_product(id):
#     product = Product.query.get(id)
#     return product_schema.jsonify(product)


# # Update product
# @app.route('/product/<id>', methods=['PUT'])
# def update_product(id):
#     product = Product.query.get(id)

#     name = request.json['name']
#     description = request.json['description']
#     price = request.json['price']
#     qty = request.json['qty']

#     product.name = name
#     product.description = description
#     product.price = price
#     product.qty = qty

#     db.session.commit()

#     return product_schema.jsonify(product)

# # Delete product
# @app.route('/product/<id>', methods=['DELETE'])
# def delete_product(id):
#     product = Product.query.get(id)
#     db.session.delete(product)
#     db.session.commit()
    
#     return product_schema.jsonify(product)
