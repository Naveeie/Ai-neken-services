import mysql.connector
import json

with open('config.json', 'r') as configFile:
    config = json.load(configFile)

mydb = mysql.connector.connect(host=config['host'], user=config['user'], passwd=config['passwd'], database=config['database'])

mycursor = mydb.cursor()
mycursor2 = mydb.cursor(buffered=True)
