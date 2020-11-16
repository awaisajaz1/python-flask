from datetime import datetime
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from myConfigs import Configs

# import models

##App
app = Flask(__name__)
app.config.from_object(Configs)
db = SQLAlchemy(app)


class students(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    studentname = db.Column(db.String(), nullable=True)
    dateCreated = db.Column(db.DateTime, default=datetime.utcnow())

    def __repr__(self):
        return '<Task %r>' % self.id


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        task_data = request.form
        sid = task_data['id']
        name = task_data['name']
        push_task = students(id=sid, studentname=name)

        try:
            db.session.add(push_task)
            db.session.commit()
            return redirect('/')
        except:
            return 'There could be an issue with your Code, Please checl ;<'

    else:
        tasks = students.query.order_by(students.dateCreated).all()
        return render_template('index.html', tasks=tasks)


@app.route('/delete/<int:ids>')
def delete(ids):
    drop_student = students.query.get(ids)
    try:
        db.session.delete(drop_student)
        db.session.commit()
        return redirect('/')
    except:
        return "Delete Code has some issue, Learn well before doing this stuff ;)"


@app.route('/update/<int:ids>', methods=['POST', 'GET'])
def update(ids):
    taskUpdate = students.query.get_or_404(ids)
    if request.method == 'POST':
        taskUpdate.id = request.form['id']
        taskUpdate.studentname = request.form['name']
        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'Issue in deletion procedure'

    else:
        return render_template('/update.html', task=taskUpdate)


if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1', port=2333, debug=True)
