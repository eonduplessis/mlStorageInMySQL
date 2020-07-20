import mysql.connector

config = {
    'user' : 'eon',
    'password' : 'qwerty',
    'host' : '127.0.0.1',
    'database' : 'mlmodels'
}

def fetch_model_data(model_name):

    mydb = mysql.connector.connect(**config)
    cursor = mydb.cursor()

    query = ("SELECT id, name, model_data FROM models where name = ?", model_name)

    cursor.execute(query)

    for (id, name, model_data) in cursor:
        print(id,name)

    cursor.close()
    mydb.close()