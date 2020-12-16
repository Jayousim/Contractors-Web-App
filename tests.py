from db_api import employee_api, projects_api


constractor = {"id": "1", "name":"Mahmood Qawasmi"}

employees = [{"id" : "12345", "name": "Mohamma Abid", "phone": "0500000000", "job" : "graphic designer"}, {"id" : "12346", "name": "Mohamma Jayousi", "phone": "0544444444", "job" : "backend"}, {"id" : "123", "name": "fathy alnasab", "phone": "0533333333", "job" : "nasab"}]

#employee_api.create_constractor(constractor["id"],constractor["name"])
# for employee in employees:
    # employee_api.add_new_employee(employee["id"],employee["name"],employee["phone"],employee["job"])

print(employee_api.get_constractor())
print("\n")
print(employee_api.get_all_employees())
print("\n")
#print(employee_api.get_employee_by_id(12345)) if it doesnot excist
print("\n")
#employee_api.delete_employee(12345)
#print(employee_api.get_all_employees())
print("\n")
employee_api.free_employee_status(123)
print(employee_api.get_all_employees())

projects_api.add_new_project("microsoft building","Jerusalem",1,"build a new high tech building for microsoft","15/10/2020", "5/5/2022")

print(projects_api.get_all_projects())
print("\n")
print(projects_api.get_project_by_id(1))
employee_api.set_employee_status(123,1)
print(employee_api.get_all_employees())

print(employee_api.get_all_employees_works_in_project(1))
