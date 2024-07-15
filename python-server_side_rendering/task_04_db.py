from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/products')
def show_products():
    source = request.args.get('source')
    products_list = []

    if source == 'sql':
        try:
            conn = sqlite3.connect('products.db')
            cursor = conn.cursor()
            cursor.execute('SELECT id, name, category, price FROM Products')
            products = cursor.fetchall()
            conn.close()

            # Convert tuple data to dictionary for easier access in the template
            for product in products:
                products_list.append({
                    'id': product[0],
                    'name': product[1],
                    'category': product[2],
                    'price': product[3]
                })
        except sqlite3.Error as e:
            # Log the error and return a generic error message or render an error template
            print(f"Database error: {e}")
            return render_template('error.html', message="An error occurred accessing the database.")
    else:
        # If source is not 'sql' or another expected value, return "Wrong source" error message
        return render_template('error.html', message="Wrong source")

    return render_template('product_display.html', products=products_list)

if __name__ == '__main__':
    app.run(debug=True)