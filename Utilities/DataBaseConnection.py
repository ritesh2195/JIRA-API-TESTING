import mysql.connector

from Utilities.ConfigReader import configReader

sql_config = {'user': configReader.getDBUser(),
              'password': configReader.getDBPassword(),
              'host': configReader.getDBHost(),
              'database': configReader.getDBName()
              }


def sqlData(query):

    conn = mysql.connector.connect(**sql_config)

    cursor = conn.cursor()

    cursor.execute(query)

    row = cursor.fetchone()

    conn.close()

    return row
