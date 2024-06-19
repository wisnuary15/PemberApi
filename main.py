from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nama_produk = db.Column(db.String(100), nullable=False)
    deskripsi = db.Column(db.String(500), nullable=False)
    harga = db.Column(db.Float, nullable=False)
    gambar = db.Column(db.String(200), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'nama_produk': self.nama_produk,
            'deskripsi': self.deskripsi,
            'harga': self.harga,
            'gambar': self.gambar
        }

@app.route('/products', methods=['POST'])
def create_product():
    data = request.get_json()
    new_product = Product(
        nama_produk=data['nama_produk'],
        deskripsi=data['deskripsi'],
        harga=data['harga'],
        gambar=data['gambar']
    )
    db.session.add(new_product)
    db.session.commit()
    return jsonify(new_product.to_dict()), 201

@app.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify([product.to_dict() for product in products]), 200

@app.route('/products/<int:id>', methods=['GET'])
def get_product(id):
    product = Product.query.get_or_404(id)
    return jsonify(product.to_dict()), 200

@app.route('/products/<int:id>', methods=['PUT'])
def update_product(id):
    data = request.get_json()
    product = Product.query.get_or_404(id)
    product.nama_produk = data['nama_produk']
    product.deskripsi = data['deskripsi']
    product.harga = data['harga']
    product.gambar = data['gambar']
    db.session.commit()
    return jsonify(product.to_dict()), 200

@app.route('/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    return '', 204

if __name__ == '__main__':
    if not os.path.exists('db.sqlite3'):
        db.create_all()
    app.run(debug=True)
