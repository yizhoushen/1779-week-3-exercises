import datetime
from flask import Flask
from flask import render_template, request

app = Flask(__name__)


@app.route('/collatz', methods=['GET'])
def collatz():
    """
    Create a web page with the number of steps it takes to reach 1, by applying 
    the two steps of the Collatz conjecture beginning from n.

    """

    # your code starts here
    if 'n' not in request.args:
        return "Missing argument!"
    input_n = request.args.get('n')
    if not input_n.isdigit():
        return "Argument is not integer!"
    original = int(input_n)
    n = original
    # end of your code

    steps = []

    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
        steps.append(n)

    series = str(original)

    for i in steps:
        series = series + "->" + str(i)

    html = """
        <!DOCTYPE html >
            <body>
                <p>Collatz series for {0} </p>
                <p>{1}</p>
                <p>Number of steps = {2}</p>
            </body>
        </html>
    """

    return html.format(original, series, len(steps))


app.run(host='0.0.0.0')
