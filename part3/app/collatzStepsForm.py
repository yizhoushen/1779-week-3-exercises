"""
    3rd Tutorial Session
"""

from flask import render_template, request
from app import webapp


@webapp.route('/collatz_form',methods=['GET'])
def collatz_form():

    html = """
        <!DOCTYPE html>
        <head>
            <title>Collatz series</title>
        </head>
        <body>
            <form method='get' action='/collatz'>
            
            <!-- your code starts here -->
            <label>Input</label>
                    <input type='text' name='n'>
            <!-- end of your code -->


            </form>
        <body>
    </html>
    """
    return html

