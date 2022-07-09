from flask import Flask
from about import me
from data import mock_data
import json


print("hello from server")
app = Flask("server")

@app.get('/')
def home():
    return "Hello from flask server"

@app.get("/test")
def test():
    return "This is just a test"

    # GET /about
    #show your name
@app.get("/about")
def about():
    return "Kacy Clark"





#######################################################
##########  API ENDPOINTS = PRODUCTS  #################
#######################################################



@app.get("/api/version")
def version():
    return "1.0"


#get /api/about
#return first lastname
@app.get("/api/about")
def about_json():
    return json.dumps(me)   # parse the dict into a json string


    # get /api/products
    # return mock_data as a json string
    @app.get("/api/products")
    def get_products():
        return json.dumps(mock_data)


@app.get("api/products/<id>")
def get_product_by_id(id): 
    for prod in mock_data:
       if prod["id"] == id:
          return json.dumps(prod)
          return "Not Found"


    # travel mock_data list
    # compare product id with the id
    # if they match, return the product as json                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   

app.run(debug=True)
