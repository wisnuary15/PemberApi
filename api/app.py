from flask import Flask, request, jsonify, render_template
from flask_restful import Api, Resource
import uuid
from .data import products  # Perhatikan perubahan di sini

app = Flask(__name__)
api = Api(app)

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
            "nama_produk": data["nama_produk"],
            "deskripsi": data["deskripsi"],
            "harga": data["harga"],
            "gambar": data["gambar"]
        }
        products.append(new_product)
        return {
            "error": False,
            "message": "Product added successfully",
            "product": new_product
        }, 201

class ProductDetail(Resource):
    def get(self, product_id):
        product = next((p for p in products if p["id"] == product_id), None)
        if product:
            return {
                "error": False,
                "message": "success",
                "product": product
            }
        return {"error": True, "message": "Product not found"}, 404

    def put(self, product_id):
        data = request.get_json()
        product = next((p for p in products if p["id"] == product_id), None)
        if product:
            product.update(data)
            return {
                "error": False,
                "message": "Product updated successfully",
                "product": product
            }
        return {"error": True, "message": "Product not found"}, 404

    def delete(self, product_id):
        global products
        products = [p for p in products if p["id"] != product_id]
        return {
            "error": False,
            "message": "Product deleted successfully"
        }

@app.route('/')
def home():
    return render_template('index.html')

api.add_resource(ProductList, '/products')
api.add_resource(ProductDetail, '/products/<string:product_id>')

if __name__ == '__main__':
    app.run(debug=True)
