from flask import Flask, request
import pyodbc

app = Flask(__name__)

cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=DESKTOP-P7M0F99;DATABASE=FLASK;UID=sa;PWD=info')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        details = request.json
        print(request)
        #firstName = details['fname']
        #lastName = details['lname']
        cur = cnxn.cursor()
        cur.execute("INSERT INTO MyUsers(firstName, lastName) VALUES ('{}', '{}')".format(details['fname'], details['lname']))
        #cur.execute("SELECT * FROM FLASK")
        cnxn.commit()
        cur.close()
        return 'success'
    return "NON"

if __name__ == '__main__':
    app.run()
