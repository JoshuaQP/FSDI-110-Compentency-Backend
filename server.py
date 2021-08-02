from flask import Flask , abort , request
from data import data
import json
from flask_cors import CORS
from config import db,parse_json


app = Flask(__name__)
CORS(app)

#dictionary
me = {
        "name" : "joshua",
        "last": "Palmier",
        "email": "Joshua@Gmail.com",
}

#List
products = data



@app.route("/")
@app.route("/home")
def index():
    return "hello from flask"


@app.route("/about")
def about():
    return render_template("abbout.html")

@app.route("/about/name")
def name():
    return me["name"]

@app.route("/about/fullname")
def full_name():
    return me["name"] + " " + me ["last"]




@app.route("/api/catalog")
def get_catalog():
    cursor= db.products.find({})
    catalog = [item for item in cursor]
    return parse_json(catalog)
     

    # Get a product by its id
@app.route("/api/catalog", methods=['POST'])

def save_product():
    prod = request.get_json()
    db.products.insert(prod)
    return parse_json(prod)

@app.route("/api/order", methods=['POST'])
def save_order():
    order = request.get_json()
    
     
    # calculate the total
    for prod in order["products"]:
        qnty = prod["quantity"]
        price = prod["price"]
        total +=(qnty * price)

    
    # verify if there is a couponCode on the order, if so
    code = order["couponCode"]
    if(len(code) > 0):
        cursor = db.couponsCodes.find({"code": code})
        for coupon in cursor:
            discount= total * (coupon["discount"] / 100)
            total = total - discount

    order["total"] = total
    # verify the coupon and get discount%

    # apply the discount to the order


    db.orders.insert(order)
    return parse_json(order)

@app.route("/api/catalog/id/<id>")
def get_product_by_id(id):
    for prod in products:
        if(prod["_id"].lower() == id):
            return json.dumps(prod)

    abort(404)


# get the cheapes product
# /api/catalog/cheapest

@app.route("/api/catalog/cheapest")
def get_cheapest():
    cheapest = products[0]
    for prod in products:
        if(prod["prince"]  < cheapest["price"]):
            cheapest = prod

    return json.dumps(cheapest)




@app.route("/api/catalog/<category>")
def get_product_by_category(category):
    data = db.products.find({"category": category})
    results = [item for item in data]
    return parse_json(results)


@app.route("/api/discountCode/<code>")
def get_discount(code):
    data = db.couponCodes.find({"code": code})
    for code in data:
        return parse_json(code)

    return parse_json ({"error": True, "reason": "invalid Code"})



    
#find the products with such category



@app.route("/api/categories")
def get_categories():
    data = db.products.find({})
    unique_categories =[]
    for prod in data:
        cat =prod["category"]
        
        if cat not in unique_Categories:
            unique_Categories.append(cat)
            print(cat)

    return parse_json(unique_categories) 



@app.route("/api/test")
def test_data_manipulation():
    test_data = db.test.find({})
    print(test_data)

    return parse_json(test_data[0])




@app.route("/test/populatecodes")
def test_populate_codes():
    db.couponsCodes.insert({"code": "sdsdd" , "discount": 10 })
    db.couponsCodes.insert({"code": "hfghj" , "discount": 18 })
    db.couponsCodes.insert({"code": "gfhfgdh" , "discount": 5 })
    db.couponsCodes.insert({"code": "jjhj" , "discount": 10 })
    db.couponsCodes.insert({"code": "pfghdf" , "discount": 30 })

    return " Codes registered "



   

  



