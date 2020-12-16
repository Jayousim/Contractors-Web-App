from flask import Flask, render_template, request, Response, redirect
from db_api import employee_api, projects_api
import requests
import json


RESPONSE_OK = 200
RESPONSE_CREATED = 201
RESPONSE_DELETED = 204
RESPONSE_SERVER_ERROR = 500

app = Flask(__name__, static_url_path='', 
              static_folder='static', 
              template_folder='templates'
           )


@app.route('/')
def home():
    table = [['one','two','three'],['four','five','six'],['seven','eight','nine']]
    return render_template('index.html', item = table )


@app.route('/employees', methods = ['POST'])
def add_employees_form():
    details = request.get_json()
    try:
        #db_api.add_employee(details)
        payload = {"text": f"{details.get('employee_name')} added"}
        response = Response(json.dumps(payload))
    except:
        respone = Response(json.dumps({"error": "employee add failed --##add details##--"}), RESPONSE_SERVER_ERROR)
    return respone


@app.route('/employees', methods = ['GET'])
def render_employees():
    employees = employee_api.get_all_employees()
    for elem in employees:
        if "constructor_id" in elem.keys():
            del elem['constructor_id']
        if "project_id" in elem.keys():
            del elem['project_id']
    return render_template('my_employees.html', employees=employees)

@app.route('/employees/set', methods = ['GET'])
def render_set_employees():
    return render_template('scheduling.html')

@app.route('/remove_employee/<employee_id>', methods = ['GET'])
def delete_employees(employee_id):
    employee_api.delete_employee(employee_id)
    return redirect("http://localhost:3000/employees", code=302)

@app.route('/projects', methods = ['GET'])
def render_my_projects():

    return render_template('my_projects.html')



if __name__ == "__main__":
    app.run( port = 3000 )

