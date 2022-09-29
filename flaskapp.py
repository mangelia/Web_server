from flask import Flask
from flask import request
from flask import jsonify
from bson import ObjectId
from pprint import pprint

app = Flask(__name__)

dogs = {
    str(ObjectId()): {
        "breed": "pug",
        "size": 15,
        "color": "black"
    },
    str(ObjectId()): {
        "breed": "yorkshire",
        "size": 20,
        "color": "cafe perro"
    },
    str(ObjectId()): {
        "breed": "chihuahua",
        "size": 10,
        "color": "brown"
    }}
# pprint(dogs)
# exit()


def create_dog(breed, size, color):
    new_dog = {
        "breed": breed,
        "size": size,
        "color": color
    }
    return new_dog


@app.route("/",methods=["GET"])
def hello_world():
    # if request.method == "POST":
    #     print("si llegaste yeiii!")
    #     print(request.data)
    #     if len(request.form)>0:
    #         form_dict = request.form.to_dict()
    #         # print(form_dict)
    #         new_dog = create_dog(form_dict["breed"],form_dict["size"],form_dict["color"])
    #         dogs[str(ObjectId())]= new_dog
            # return "Created doggy", 201
    return """<h1>hello world form</h1>
<form method="POST" action="/DOGS" enctype="mutipart/form-data">
    <label for="breed">Breed</label>
    <input type="text" name="breed"/>

    <label for="color">Color</label>
    <input type="text" name="color"/>

    <label for="size">Size</label>
    <input type="number" name="size"/>
    <p></p>
    <input type="submit"/>

</form>"""


@app.route("/TAC")
def hello_tac():
    return "<h1>Hola TAC</h1>"


@app.route("/DOGS", methods=["GET", "POST", "DELETE", "PUT"])
def recurso_dogs():
    if request.method == "POST":
        print(request.data)
        print(request.form)
        if len(request.form)>0:
            form_dict = request.form.to_dict()
            # print(form_dict)
            new_dog = create_dog(form_dict["breed"],int(form_dict["size"]),form_dict["color"])
            dogs[str(ObjectId())]= new_dog
            return "Created doggy", 201
            # return "it works"
        print(request.json,type(request.json))
        new_dog = create_dog(request.json["breed"],request.json["size"],request.json["color"])
        dogs[str(ObjectId())]= new_dog
        return "Created doggy", 201
    elif request.method == "PUT":
        dog_id = request.args["id"]
        dogs[dog_id]=request.json
        return "Updated doggy", 204
    elif request.method == "DELETE":
        dog_id = request.args["id"]
        del dogs[dog_id]
        return "Deleted doggy", 204
    else:
        print(request.headers)
        if len(request.args) > 0:
            dog = dogs[request.args["id"]]
            if "filter" in request.args:
                return jsonify(dog[request.args["filter"]])
            return jsonify(dog)
        print(request.args)
        return jsonify(dogs)
