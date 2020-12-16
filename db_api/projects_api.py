from config import connection

def add_new_project(project_name,project_address,constractor_id,project_notes, start_date, end_date):
    with connection.cursor() as cursor:
        query=""" INSERT INTO project (name,address,constructor_id,notes) VALUES(%s,%s,%s,%s)"""
        cursor.execute(query,(project_name, project_address,constractor_id,project_notes ))
        connection.commit()

        query = """ select last_insert_id(); """
        cursor.execute(query, ())
        connection.commit()
        last_id = cursor.fetchone()['last_insert_id()']

        query=""" INSERT INTO time_line (project_id,start_date,end_date) VALUES(%s,%s,%s)"""
        cursor.execute(query,(last_id, start_date,end_date ))
        connection.commit()

        
    

def get_project_by_id(project_id):
    with connection.cursor() as cursor:
        query = """ SELECT * FROM project WHERE id=%s """
        cursor.execute(query, (project_id))
        connection.commit()
        result = cursor.fetchone()
    return result

def get_all_projects():
    with connection.cursor() as cursor:
        query = """ SELECT * FROM project"""
        cursor.execute(query, ())
        connection.commit()
        result = cursor.fetchall()
    return result