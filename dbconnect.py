import mysql.connector
import io

config = {  'user' : 'root', 
            'password' : 'password', 
            'host' : '127.0.0.1', 
            'port' : '3306', 
            'database' : 'mlmodels'}

def fetch_model_data(model_name):
    """
    Expects a model name in target MySQL database and returns the content of the model_data column
    """
    try:

        mydb = mysql.connector.connect( **config )

        cursor = mydb.cursor()

        query = (""" SELECT id, name, model_data FROM models where name = %s """)

        cursor.execute(query, (model_name,))

        data = "" 

        for (model_data) in cursor:
            data = model_data[2]

        return data

    except mysql.connector.Error as error:
        print("Database fetch query failed {}".format(error))
    finally:
        if (mydb.is_connected()):
            cursor.close()
            mydb.close()
    
    

def write_model_data(model_name, model_data):
    """
    Writes model data to an existing item in target MySQL database, matching model_name value
    """
    try:

        mydb = mysql.connector.connect( **config)

        cursor = mydb.cursor()

        query = ("""UPDATE models SET model_data = %s WHERE name = %s """)

        data = model_data.read()

        args = (data, model_name)

        result = cursor.execute(query, args)
        
        mydb.commit()
        
        return result

    except mysql.connector.Error as error:
        print("Database update query failed {}".format(error))

    finally:
        if (mydb.is_connected()):
            cursor.close()
            mydb.close()
    
