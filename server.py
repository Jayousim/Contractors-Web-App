from flask import Flask, render_template, request, Response
import requests
import json


RESPONSE_OK = 200
RESPONSE_CREATED = 201
RESPONSE_DELETED = 204
RESPONSE_SERVER_ERROR = 500

mock_projects = [{"name":"building1" , "employees" : ["employee1", "employee2"], "progress" : 14}, 
                 {"name":"hitech park","employees" : ["employee15", "employee22"], "progress" : 3}, 
                    {"name":"school", "employees" : ["employee5", "employee4"], "progress" : 34},
                    {"name":"school", "employees" : ["employee5", "employee4"],"progress" : 50}  ]

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
def render_add_employees():
    return render_template('add_employee.html')

@app.route('/employees/set', methods = ['GET'])
def render_set_employees():
    return render_template('scheduling.html')

@app.route('/projects', methods = ['GET'])
def render_my_projects():
    return render_template('my_projects.html', projects = mock_projects)

@app.route('/schedule/<project_name>', methods = ['GET'])
def schedule_employee_to_project(project_name):
    return render_template('schedule.html', project = project_name)

if __name__ == "__main__":
    app.run( port = 3000 )

