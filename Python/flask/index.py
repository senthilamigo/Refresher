#!/usr/bin/python3

from flask import Flask, jsonify, request

app = Flask(__name__)
app.config["DEBUG"] = True

incomes = [
        { 'description': 'Salary',
            'amount': 5000
            }
        ]

############################################
@app.route("/json_example", methods=['POST'])
def json_route():
    req_data = request.get_json()

    language = req_data['language']
    framework = req_data['framework']
    return ''' The Language is ' + language 
               The framework is ' + framework '''

############################################
@app.route('/param_example')
def param_route():
    args = request.args
    print(args)
    transId = args.get('transId')
    transDate = args.get('transDate')
    status = '1'
    print(transId)
    print(transDate)
    result = [ { "transId":transId, "transDate":transDate, "Status":status } ]
    #result = "Transid " + transId + " transDate " + transDate
    return jsonify(result)

############################################
@app.route("/query_example")
def query_example():
    Language = request.args.get('Language')
    return 'The Language is ' + Language

############################################
@app.route('/int_example/<int:mynum>')
def int_route(mynum):
    return 'The number is :' + str(mynum)

############################################
@app.route("/incomes")
def get_incomes():
    return jsonify(incomes)

############################################
@app.route("/incomes", methods=['POST'])
def add_income():
    incomes.append(request.get_json())
    return '', 204

############################################
@app.route("/")
def hello_world():
    return "Hello World"

app.run(host="0.0.0.0")
