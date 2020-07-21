import mysql.connector
import io
import sys

def fetch_model_data(model_name):
    mydb = mysql.connector.connect( user = 'root', 
                                    password = 'qwerty', 
                                    host = '127.0.0.1', 
                                    port = '3306', 
                                    database = 'mlmodels')

    cursor = mydb.cursor()

    query = ("SELECT id, name, model_data FROM models where name = '" + model_name + "'")

    cursor.execute(query)

    data = "" 

    for (model_data) in cursor:
        data = model_data[2]
        print(sys.getsizeof(data))

    cursor.close()
    mydb.close()
    
    return data

def write_model_data(model_name, model_data):
    mydb = mysql.connector.connect( user = 'root', 
                                    password = 'qwerty', 
                                    host = '127.0.0.1', 
                                    port = '3306', 
                                    database = 'mlmodels')

    cursor = mydb.cursor()

    query = ("""UPDATE models SET model_data = %s WHERE name = %s """)

    data = model_data.read()

    args = (data, model_name)

    result = cursor.execute(query, args)
    
    mydb.commit()

    if (mydb.is_connected()):
        cursor.close()
        mydb.close()
    
    return result

