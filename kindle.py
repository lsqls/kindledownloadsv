#!/usr/bin/python
#coding:utf-8
import sqlite3
from flask import Flask
from flask import request
from flask import render_template
from flask import  send_from_directory
app = Flask(__name__)
app.config.update(
    debug=True,
    host='0.0.0.0',
    port=80,
    dbfilepath = r'.\books.db'
)
@app.route('/',methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return  render_template('index.html')
    else:
        keyword= request.form['keyword']
        books=dbsearch(keyword)
        return render_template('search.html', keyword=keyword,books=books)
@app.route('/download/<path:filename>')
def download_file(filename):
    return send_from_directory('.',filename, as_attachment=True)
@app.errorhandler(404)
def handle_bad_request(e):
    return '请返回主页', 400
# or, without the decorator
app.register_error_handler(400, handle_bad_request)
def dbsearch(keyword):
    dbfilepath =app.config['dbfilepath']
    conn = sqlite3.connect(dbfilepath)
    c = conn.cursor()
    cursor = c.execute('SELECT id, name, path  from PathInfo where name like "%{0}%"'
                       .format(keyword))
    result = []
    for row in cursor:
        result.append({"id" :row[0],"name" :row[1],"path" :row[2]})
    conn.close()
    return result
if __name__ == '__main__':
   app.run(debug=app.config['debug'],
           host=app.config['host'],
           port=app.config['port'])