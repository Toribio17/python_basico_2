from flask import Flask
from flask import request
import json
from utils import Utils as utils
 
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_every_one():
    return "Hello Student! "

@app.route('/add_value/<name>', methods=['GET'])
def add_data(name):
    list_names = ['Jose', 'Joel', 'Manuel', 'Elias', 'Mateo']
    list_names.append(name)
    
    return list_names


@app.route('/add_value_post', methods=['POST'])
def add_data_post():
    list_names = ['Jose', 'Joel', 'Manuel', 'Elias', 'Mateo']
    name = request.get_json().get('user_name')
    list_names.append(name)
    
    return list_names

@app.route('/show_values_json', methods=['POST'])
def show_json():
    json_values = '{ "name":"John", "age":30, "city":"New York"}'
    # the result is a Python dictionary:
    json_file = json.loads(json_values)
    
    return json_file

@app.route('/show_values_json_v2', methods=['POST'])
def show_json_v2():
    # a Python object (dict):
    dictionary = {
    "name": "John",
    "age": 30,
    "city": "New York"
    }

    # convert into JSON:
    json_file = json.dumps(dictionary)
    
    # the result is a JSON string:
    return json_file

@app.route('/compare_two_numbers', methods=['POST'])
def compare_numbers():
    obj = utils("dummy value")
    get_result = obj.statements_one()
    
    return get_result


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8088, debug=True)