from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({"Message":"Welcome"})

data = [{"id": "0", "name": "Sally", "age": "25"},
    {"id": "1", "name": "Bob", "age": "30"},
    {"id": "2", "name": "Sue", "age": "35"},
    {"id": "3", "name": "Joe", "age": "40"},
    {"id": "4", "name": "Bob", "age": "32"}]

@app.route("/users")
def users():
    return jsonify({"Users":data})

@app.route("/users/<int:id>", methods = ['GET'])
def get_user_by_id(id):
    return jsonify({"User":data[id]})


@app.route("/users/<string:name>", methods = ['GET'])
def get_user_by_name(name):
    for user in data:
        if user['name'] == name:
            return jsonify({"User": user})
    return jsonify({"User":None})

# insert data
# Command curl -i -H "Content-Type: Application/json" -X POST http://localhost:5000/users
@app.route("/users", methods = ['POST'])
def insert_data():
    new_user = {"id": "5", "name": "Joel", "age": "45"}
    data.append(new_user)
    return jsonify({"User Added": new_user})

# PUT methode to update values
# Command curl -i -H "Content-Type: Application/json" -X PUT http://localhost:5000/users/5 (5 as id to update value for)
@app.route("/users/<int:id>", methods = ['PUT'])
def update_user(id):
    data[id]["age"] = "99"
    return jsonify({"Users": data[id]})

# DELETE data
# Command curl -i -H "Content-Type: Application/json" -X DELETE http://localhost:5000/users/5
@app.route('/users/<int:id>', methods = ['DELETE'])
def delete_user(id):
    data.remove(data[id])
    return jsonify({"Result": True})


if __name__ == '__main__':
    app.run(debug = True)
