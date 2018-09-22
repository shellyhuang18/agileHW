from app import app
from flask import render_template, request, redirect, jsonify


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'GET':
        return render_template('add.html')
    elif request.method == 'POST':
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        op = request.form.get("operation")

        result = ""

        if op == "add":
            result = str(num1 + num2)
        elif op == "sub":
            result = str(num1 - num2)
        elif op == "div":
            if num2 == 0:
                result = "no divide by 0"
            else:
                result = str(num1 / num2)
        else:
            result = str(num1 * num2)
        
        #send response back to ajax
        return jsonify(result)      

    