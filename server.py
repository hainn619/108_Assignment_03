import json
from operator import truediv
from flask import Flask
from aboutme import me
from mock_data import catalog  # import data
app = Flask('organika')


@app.route("/", methods=['GET'])
def home():
    return "This is home page!!"


# Creat an about endpoint to return your name


@app.route("/about", methods=['GET'])
def about():
    return me["first"] + " " + me["last"]


@app.route("/myaddress")
def address():
    return f'{me["address"]["number"]}{me["address"]["street"]}'


#####################################################
#################### API End Point ##################
#####################################################

@app.route("/api/catalog", methods=["GET"])
def get_catalog():
    return json.dumps(catalog)


@app.route("/api/catalog/count", methods=["GET"])
def get_count():
    # Here... Count how many products are in list catalog
    counts = len(catalog)
    return json.dumps(counts)  # return the value


@app.route("/api/product/<id>", methods=["GET"])
def get_product(id):
    return json.dumps(id)

app.run(debug=True)
