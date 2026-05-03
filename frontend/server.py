from flask import Flask, render_template, redirect, url_for

## Server Configuration
srvhost = "0.0.0.0"
srvport = 80

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    return redirect(url_for('index'))

# =============================================================== #

if __name__ == '__main__':
    app.run(host=srvhost, port=srvport, debug=True)