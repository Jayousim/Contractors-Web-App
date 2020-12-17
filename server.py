from flask import Flask, render_template, request, Response, redirect
from db_api import employee_api, projects_api
from datetime import date, datetime, timedelta
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
    e_id = request.form['employee_id']
    name = request.form['employee_name']
    phone = request.form['employee_phone']
    position = request.form['employee_position']
    try:
        employee_api.add_new_employee(e_id, name, phone, position)
        payload = {"text": f"{name} added"}
        response = redirect('/employees')
    except:
        response = Response(json.dumps({"error": "employee add failed --##add details##--"}), RESPONSE_SERVER_ERROR)
    return response

@app.route('/projects', methods = ['POST'])
def add_project_form():
    name = request.form['project_name']
    params = request.form.to_dict()
    try:
        projects_api.add_new_project(*params.values())
        payload = {"text": f"{name} project added"}
        response = redirect("/projects")
    except Exception as ex:
        print(ex)
        response = Response(json.dumps({"error": "employee add failed --##add details##--"}), RESPONSE_SERVER_ERROR)
    return response
        
    
@app.route('/projects/add', methods = ['GET'])
def add_projects():
    return render_template('new_project.html')

@app.route('/employees/add', methods = ['GET'])
def render_add_employees():
    return render_template('add_employee.html')


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
    projects = projects_api.get_all_projects()
    all_employees = {}
    for project in projects:
        pid = project.get('id')  
        project_employees = employee_api.get_all_employees_works_in_project(pid) 
        all_employees[pid] = [employee.get('name') for employee in project_employees]
    return render_template('my_projects.html', projects = projects, employees = all_employees)


@app.route('/delete_project/<project_id>', methods = ['GET'])
def delete_projects(project_id):
    employees = employee_api.get_all_employees_works_in_project(project_id)
    for employee in employees:
        employee_api.free_employee_status(employee['id'])
    
    projects_api.delete_project(project_id)
    return redirect('/projects')

@app.route('/schedule', methods = ['GET'])
def schedule_employee_to_project():
    project_id = request.args.get('project_id')
    employee_id = request.args.get('employee_id')
    employee_api.set_employee_status(employee_id, project_id)
    available = employee_api.get_all_available()
    return render_template('schedule.html', project = project_id, available_employees = available)


@app.route('/schedule/<project_id>', methods = ['GET'])
def schedule_employees_project(project_id):
    available = employee_api.get_all_available()
    return render_template('schedule.html', project = project_id, available_employees = available)


@app.route('/schedule/remove', methods = ['GET'])
def schedule_remove_employee_project():
    project_id = request.args.get('project_id')
    employee_id = request.args.get('employee_id')
    employee_api.free_employee_status(employee_id)
    project_employees = employee_api.get_all_employees_works_in_project(project_id)
    return render_template('schedule_remove.html', project = project_id, available_employees = project_employees)


@app.route('/schedule/remove/<project_id>', methods = ['GET'])
def schedule_free_employees_project(project_id):
    project_employees = employee_api.get_all_employees_works_in_project(project_id)
    return render_template('schedule_remove.html', project = project_id, available_employees = project_employees)

@app.route('/time_line', methods = ['GET'])
def time_lines():
    time_lines = projects_api.get_all_history_time_line()
    
    for project_time_line in time_lines:
        start_date = datetime.strptime(project_time_line['start_date'], '%Y-%m-%d')
        end_date =  datetime.strptime(project_time_line['end_date'], '%Y-%m-%d')
        progress = int((datetime.now() - start_date).days)
        if progress < 0:
            progress = 0
        ends_in = (end_date - start_date).days
        project_time_line.pop('start_date')
        project_time_line.pop('end_date')
        if progress == 0:
            project_time_line['progress'] = 0
        elif progress == int(ends_in):
            project_time_line['progress'] = 100
        else:
            project_time_line['progress'] = int(((progress / int(ends_in)) * 100)+1)

    return render_template('time_lines.html', time_lines=time_lines)


if __name__ == "__main__":
    app.run( port = 3000 )
