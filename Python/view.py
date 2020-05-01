from flask import Flask

class Result():
    def show(self):
        app.run(port = 5555)


# Initiate a Flask instance.
app = Flask(__name__)

# Configure the root route.
@app.route('/')
def show_result():
    fil = '/home/hh/Documents/Python/result'

    # Open the result file and get the lab result.
    with open(fil) as f:
        res = f.read()

    # Check if the result of the lab is good enough and shows passed or failed.
    if float(res) > 80:
        return f'Congratulations, you passed: {res}%'
    else:
        return f'Unfortunately, you failed: {res}%'

# This is executed, if this file is run directly.
if __name__ == '__main__':
    app.run(debug = True, port = 5555)