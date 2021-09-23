#!/usr/bin/env python3
import os, cgi, cgitb
import secret
from http.cookies import SimpleCookie

# Python 3.7 versus Python 3.8
try:
    from cgi import escape #v3.7
except:
    from html import escape #v3.8

def secret_page(username=None, password=None):
    """
    Returns the HTML for the page visited after the user has logged-in.
    """
    if username is None or password is None:
        raise ValueError("You need to pass both username and password!")

    return _wrapper("""
    <h1> Welcome, {username}! </h1>

    <p> <small> Pst! I know your password is
        <span class="spoilers"> {password}</span>.
        </small>
    </p>
    """.format(username=escape(username.capitalize()),
               password=escape(password)))


def after_login_incorrect():
    """
    Returns the HTML for the page when the login credentials were typed
    incorrectly.
    """
    return _wrapper(r"""
    <h1> Login incorrect :c </h1>

    <p> Incorrect username or password (hint: <span class="spoilers"> Check
        <code>secret.py</code>!</span>)
    <p> <a href="login.py"> Try again. </a>
    """)

def login_page():
    """
    Returns the HTML for the login page.
    """

    return _wrapper(r"""
    <h1> Welcome! </h1>

    <form method="POST" action="login.py">
        <label> <span>Username:</span> <input autofocus type="text" name="username"></label> <br>
        <label> <span>Password:</span> <input type="password" name="password"></label>

        <button type="submit"> Login! </button>
    </form>
    """)

def _wrapper(page):
    """
    Wraps some text in common HTML.
    """
    return ("""
    <!DOCTYPE HTML>
    <html>
    <head>
        <meta charset="utf-8">
        <style>
            body {
                font-family: -apple-system, BlinkMacSystemFont, sans-serif;
                max-width: 24em;
                margin: auto;
                color: #333;
                background-color: #fdfdfd
            }

            .spoilers {
                color: rgba(0,0,0,0); border-bottom: 1px dashed #ccc
            }
            .spoilers:hover {
                transition: color 250ms;
                color: rgba(36, 36, 36, 1)
            }

            label {
                display: flex;
                flex-direction: row;
            }

            label > span {
                flex: 0;
            }

            label> input {
                flex: 1;
            }

            button {
                font-size: larger;
                float: right;
                margin-top: 6px;
            }
        </style>
    </head>
    <body>
    """ + page + """
    </body>
    </html>
    """)

form = cgi.FieldStorage()

username = form.getvalue('username')
password = form.getvalue('password')

c = SimpleCookie(os.environ["HTTP_COOKIE"]) #this line was inspired by Zoe Riell however can be found also in  class http.cookies.SimpleCookie([input]) in
#https://docs.python.org/3/library/http.cookies.html

if c.get("username"):
    cookies_username = c.get("username").value


if c.get("password"):
    cookies_password = c.get("password").value

got_pass_from_cookie = False
try:
    if (cookies_password == secret.password and cookies_username == secret.username):
        print(secret_page(cookies_username,cookies_password))
        got_pass_from_cookie = True
except:
    i = 1


if (username == secret.username and password == secret.password):
    print("Set-Cookie:username = "+username+";/r/n")
    print("Set-Cookie:password = "+password+";/r/n")
    print(secret_page(username,password))
else:
    if (got_pass_from_cookie == False):
        print(login_page())   


        



"""
print("Content-type:text/html\r\n\r\n")

print("<html>")
print("<head>")
print("<Title>Test CGI</Title>")
print("</head>")

print("<body>")

if (username):
    if (username == secret.username):
        print("Set-Cookie:User_id = "+username+";/r/n")

if (password):
    if (password == secret.password):
        print("Set-Cookie:User_id = "+username+";/r/n")


print(username)
print(password)
print("<p>test</p>")
print("</body>")

print("</html>")
"""