from flask import Flask,render_template,request
import mysql.connector

my_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="integration"
)
my_cursor = my_connection.cursor()
app = Flask(__name__)

@app.route('/', methods=['GET'])
def homepage():
    return render_template('index.html', context="You are in home page")
@app.route('/admission', methods=['GET'])
def admission():
    return render_template('admission.html')
@app.route('/register', methods=['GET'])
def register():
    return render_template('register.html')
@app.route('/update', methods=['GET'])
def update():
    return render_template('update.html')
# ---------------------------------------------------
@app.route('/register_form', methods=['POST'])
def register_form():
    _id = request.form['id']
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    percentage = request.form['percentage']
    rank = request.form['rank']
    course = request.form['course']
    address = request.form['address']
    query = f'''
      insert into student
      values(%s,%s,%s,%s,%s,%s,%s,%s);
    '''
    values = (_id, name, email, phone, percentage, rank, course, address)

    my_cursor.execute(query, values)

    my_connection.commit()
    return 'DATA is inserted'
@app.route('/view', methods=['GET'])
def view():
    query = '''
      select * from student;
    '''
    my_cursor.execute(query)
    data = my_cursor.fetchall()
    return render_template('view.html', detailes=data)

@app.route('/update_form', methods=['POST'])
def update_form():
    _id = request.form['id']
    field = request.form['field']
    new_value = request.form['new_value']
    query = f'''
        update student
        set {field} = '{new_value}'
        where id = {_id}
    '''
    my_cursor.execute(query)
    my_connection.commit()
    return 'Updated'
@app.route('/delete', methods=['GET'])
def delete():
    return render_template('delete.html')
@app.route('/delete_form', methods=['POST'])
def delete_form():
    _id = request.form['id']
    q = 'delete from student where id = %s'
    values = (_id,)
    my_cursor.execute(q, values)
    my_connection.commit()
    return 'DELETED'
@app.route('/query_form', methods=['POST'])
def query():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    field = request.form['field']
    query = '''
      insert into query(name, email, phone, course)
      values(%s,%s,%s,%s);
    '''
    values = (name, email, phone, field)
    my_cursor.execute(query, values)
    my_connection.commit()
    return render_template('index.html')
app.run(debug=True)
#comitted
#eddited
#shareef changed the code
#neeraj changed the code