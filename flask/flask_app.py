__author__ = 'sergii'
import os
import flask


app = flask.Flask(__name__)


@app.route('/')
def index():
    pass


@app.route('/upload/', methods=['POST'])
def upload():
    """send by:
    dd if=/dev/zero of=file.txt count=1024 bs=1024
    curl -X POST  --data-binary @file.txt 10.0.2.15:80/upload/
    """
    print 'data len: ', len(flask.request.data)
    print 'request file:', len(flask.request.files)
    try:
        with open(flask.request.headers['X-File']) as fd:
            fd.seek(0, os.SEEK_END)
            print 'file size', fd.tell()
    except KeyError:
        print 'No X-File detected'
    resp = flask.make_response()
    return resp


app.run('0.0.0.0', 8080, debug=True)
