#!/usr/bin/env python3
import os, json
import secret

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



print("Content-type:text/html\r\n\r\n")
print("<Title>Test CGI</Title>")
print(login_page())
#print(os.environ)
#print(os.environ["QUERY_STRING"])
#print(os.environ["HTTP_USER_AGENT"])



