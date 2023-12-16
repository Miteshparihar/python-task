# >>>>>>>>>>>>>>>>>>>>>>>>>>Advance Assesment
import mysql.connector
#>>>>>>>>>>>>>>>>>>>>>>>>>>>database connectivity
def connection():

    return mysql.connector.connect(
        user="root",
        host="localhost",
        password="",
        database="pharmacy")
