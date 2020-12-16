from config import connection

def get_constractor():

    with connection.cursor() as cursor:
        query = """ SELECT * FROM constractor """
        cursor.execute(query, ())
        connection.commit()
        result = cursor.fetchone()
    return result

def create_constractor(constractor_id,name):
    with connection.cursor() as cursor:
        query=""" INSERT INTO constractor (id,name) VALUES(%s,%s)"""
        cursor.execute(query,(constractor_id, name ))
        connection.commit()

def get_employee_by_id(employee_id):
    with connection.cursor() as cursor:
        query = """ SELECT * FROM employee WHERE id = %s """
        cursor.execute(query, (employee_id,))
        connection.commit()
        result = cursor.fetchone()
    if result == None:
        raise Exception("Error, this employee does not exist")
    return result

def get_all_employees():
    with connection.cursor() as cursor:
        query = """ SELECT * FROM employee """
        cursor.execute(query, ())
        connection.commit()
        result = cursor.fetchall()
    return result


def get_all_available():
    with connection.cursor() as cursor:
        query = """ SELECT * FROM employee WHERE STATUS = 1 """
        cursor.execute(query, ())
        connection.commit()
        result = cursor.fetchall()
    return result

def add_new_employee(employee_id, employee_name, employee_phone_number, employee_job):
    constractor_id = get_constractor()['id']
    with connection.cursor() as cursor:
        query=""" INSERT INTO employee (id,name,phone_number,job,constructor_id) VALUES(%s,%s,%s,%s,%s)"""
        cursor.execute(query,(employee_id,employee_name,employee_phone_number,employee_job,constractor_id ))
        connection.commit()


def delete_employee(employee_id):
    with connection.cursor() as cursor:
        query = """ DELETE FROM employee WHERE id = %s """
        cursor.execute(query, (employee_id, ))
        connection.commit()

def free_employee_status(employee_id):
    with connection.cursor() as cursor:
        query=""" UPDATE employee set status=%s , project_id=%s WHERE id=%s """
        cursor.execute(query,('true',None,employee_id, ))
        connection.commit()

def set_employee_status(employee_id, project_id):
    with connection.cursor() as cursor:
        query=""" UPDATE employee set status=%s , project_id=%s WHERE id=%s """
        cursor.execute(query,('false',project_id,employee_id, ))
        connection.commit()

def get_all_employees_works_in_project(project_id):
    with connection.cursor() as cursor:
        query = """ SELECT * FROM employee WHERE project_id=%s """
        cursor.execute(query, (project_id))
        connection.commit()
        result = cursor.fetchall()
    return result