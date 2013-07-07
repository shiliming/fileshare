import os
from bottle import route,template,run,static_file


@route('/')
def index():
    filenames=os.listdir('file')
    return template('index.html',filenames=filenames)

@route('/file/<filename>')
def server_static(filename):
    return static_file(filename,root='file',download=filename)

run(port=80,host='0.0.0.0')
