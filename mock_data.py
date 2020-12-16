from db_api import employee_api, projects_api


constractor = {"id": "1", "name":"Mahmood Qawasmi"}

employees = [
    {"id" : "12345",
    "name": "Mohamma Abid",
    "phone": "0500000000",
    "job" : "graphic designer"},
    {"id" : "12346",
    "name": "Mohamma Jayousi",
    "phone": "0544444444",
    "job" : "backend"},
    {"id" : "123",
    "name": "fathy alnasab",
    "phone": "0533333333",
    "job" : "nasab"},
    {"id" : "1235",
    "name": "Salem salem",
    "phone": "0555555555",
    "job" : "front end"},
    {"id" : "1233",
    "name": "Sami",
    "phone": "0512344567",
    "job" : "full stack"},
    {"id" : "1232",
    "name": "Wissam",
    "phone": "0522334455",
    "job" : "security"}
    ]

projects = [
    {
        "name": "microsoft building",
        "address": "Jerusalem",
        "constractor" : 1,
        "notes" : "build a new high tech building for microsoft",
        "start_date" : "10/12/2020",
        "end_date" : "15/01/2022"
    },
    {
        "name": "7 floor building",
        "address": "Jerusalem, tal-puit, 5",
        "constractor" : 1,
        "notes" : "7 floors building for offices",
        "start_date" : "25/12/2020",
        "end_date" : "15/08/2021"
    }
]

employee_api.create_constractor(constractor["id"],constractor["name"])
for employee in employees:
    employee_api.add_new_employee(employee["id"],employee["name"],employee["phone"],employee["job"])

for project in projects:
    projects_api.add_new_project(project['name'],project['address'], 1, project['notes'], project["start_date"],project["end_date"])

employee_api.set_employee_status(12345,1)
employee_api.set_employee_status(12346,1)
employee_api.set_employee_status(123,1)

employee_api.set_employee_status(1235,2)
employee_api.set_employee_status(1233,2)
employee_api.set_employee_status(1232,2)









