####This is basis API program where web page form is available where user operation can be recorded in MYSQL database
#### Also, each and every action will be logged using logger function

import logging as lg
lg.basicConfig(filename='Flasktest.log', level = lg.INFO, format  = '%(asctime)s %(message)s')
lg.info(" This is logger of my application and below is the server on which application is running")

from flask import Flask, render_template, request, jsonify
import mysql.connector as connection
#mydb = connection.connect(host="localhost", database='student', user="root", passwd="", use_pure=True)

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST']) # To render Homepage
def home_page():
    return render_template('index.html')

@app.route('/update', methods=['POST'])  # This will be called from UI
def math_operation():
    if (request.method=='POST'):
        operation=request.form['operation']
        name = str(request.form['name'])
        empid = str(request.form['empid'])
        if(operation=='Query'):
            print('inside query')
            mydb = connection.connect(host="localhost", database='Student', user="root", passwd="", use_pure=True)
            query = "select * from empdetails where empid = %s "
            cursor = mydb.cursor()  # create a cursor to execute queries
            cursor.execute(query,(empid,))
            record = cursor.fetchall()

            for row in record:
                a = row[0]
                b = row[1]
            if a.isspace():
                result = 'Record not found:'
            else:
                result = 'Record found:' + a
            # mydb.commit()
            mydb.close()
            result = 'Record' + str(name) + ' and ' + str(empid) + ' are found'
        if (operation == 'Insert'):
            print('inside insert')
            mydb = connection.connect(host="localhost", database='Student', user="root", passwd="", use_pure=True)
            query = """INSERT INTO empdetails(name,empid) VALUES (%s,%s)"""
            record = (name,empid)
            cursor = mydb.cursor()  # create a cursor to execute queries
            cursor.execute(query,record)
            mydb.commit()
            mydb.close()
            result= 'Record  ' + str(name) +' and '+str(empid) +' are inserted successfully'
            lg.info(result)
        return render_template('results.html',result=result)

if __name__ == '__main__':
    app.run()




