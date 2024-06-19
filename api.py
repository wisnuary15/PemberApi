from flask import Flask, request, jsonify
from flask_restful import Api, Resource
import uuid

app = Flask(__name__)
api = Api(app)

# Sample product data
products = [
    {
        "id": str(uuid.uuid4()),
        "nama_produk": "Biji Jagung Hibrida",
        "deskripsi": "Biji jagung hibrida unggulan yang dirancang untuk memberikan hasil panen maksimal dengan kualitas biji yang superior. Cocok untuk berbagai kondisi tanah dan iklim, produk ini merupakan solusi terbaik bagi para petani yang menginginkan produktivitas tinggi dan ketahanan terhadap berbagai penyakit tanaman.",
        "harga": 30000,
        "gambar": "https://benihcitraasia.co.id/assets/images/kemasan/aeeb038754fc3e6d3df0acfd70ccbc61.webp"
    },
    # Additional products...
]

class ProductList(Resource):
    def get(self):
        return {
            "error": False,
            "message": "success",
            "count": len(products),
            "products": products
        }

    def post(self):
        data = request.get_json()
        new_product = {
            "id": str(uuid.uuid4()),
            "nama_produk": data.get("nama_produk"),
            "deskripsi": data.get("deskripsi"),
            "harga": data.get("harga"),
            "gambar": data.get("gambar")
        }
        products.append(new_product)
        return {"error": False, "message": "Product added successfully", "product": new_product}, 201

class ProductDetail(Resource):
    def get(self, product_id):
        product = next((p for p in products if p['id'] == product_id), None)
        if product:
            return {"error": False, "message": "success", "product": product}
        return {"error": True, "message": "Product not found"}, 404

    def put(self, product_id):
        data = request.get_json()
        product = next((p for p in products if p['id'] == product_id), None)
        if product:
            product['nama_produk'] = data.get('nama_produk', product['nama_produk'])
            product['deskripsi'] = data.get('deskripsi', product['deskripsi'])
            product['harga'] = data.get('harga', product['harga'])
            product['gambar'] = data.get('gambar', product['gambar'])
            return {"error": False, "message": "Product updated successfully", "product": product}
        return {"error": True, "message": "Product not found"}, 404

    def delete(self, product_id):
        global products
        products = [p for p in products if p['id'] != product_id]
        return {"error": False, "message": "Product deleted successfully"}

# Define the routes
api.add_resource(ProductList, '/products')
api.add_resource(ProductDetail, '/products/<string:product_id>')

if __name__ == '__main__':
    app.run(debug=True)
