__author__ = 'sergii'
import flask
import logging
import os
import sys

logger = logging.getLogger('flask_app')


app = flask.Flask(__name__)


form = ('''
<!doctype html>
<title>Upload new File</title>
<h1>Upload new File</h1>
<form action="" method=post enctype=multipart/form-data>
  <p><input type=file name=file>
     <input type=submit value=Upload>
</form>
''')


@app.route('/')
def index():
    pass


@app.route('/upload/', methods=['POST', 'GET'])
def upload():
    """send by:
    dd if=/dev/zero of=file.txt count=1024 bs=1024
    curl -X POST  --data-binary @file.txt 10.0.2.15:80/upload/
    """
    if flask.request.method == 'GET':
        return form
    logger.debug('data len: %d', len(flask.request.data))
    logger.debug('request file: %d', len(flask.request.files))
    #import pdb; pdb.set_trace()
    try:
        with open(flask.request.headers['X-File']) as fd:
            fd.seek(0, os.SEEK_END)
            logger.debug('file size %d', fd.tell())
    except KeyError:
        logger.debug('No X-File detected')
    resp = flask.make_response()
    return resp


@app.route('/hello', methods=['GET'])
def hello():
    name = flask.request.args.get('name')
    return hello_api(name)


def hello_api(name):
    return "hello %s" % name


if __name__ == '__main__':
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler(sys.stdout))
    app.run('0.0.0.0', 8080, debug=True)
