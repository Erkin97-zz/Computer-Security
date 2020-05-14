#!/usr/bin/env python
import flask
app  = flask.Flask(__name__)


'''
The attacker's server for lab2.
'''
main_page = '''
<!doctype html><html>Working!</html>
'''
empty_page = '''
<!doctype html>
<html lang="en">
Message received!
</html>
'''

@app.route("/",methods=['GET'])
def resp_main_page():
    print(flask.request.data)
    print(main_page)
    resp = flask.Response(main_page)
    print(resp)
    return resp

@app.route("/benign",methods=['POST'])
def benign():
    print(flask.request.data)
    resp = flask.Response(empty_page)
    return resp

@app.route('/<path:dummy>')
def fallback(dummy):
    print(flask.request.data)
    print(dummy)
    return 'This one catches everything else'


if __name__ == '__main__':
    app.run(host='example.org', port=4444)
