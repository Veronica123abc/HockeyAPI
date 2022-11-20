from flask import Flask, jsonify, request, render_template, redirect, url_for
import pandas as pd


app = Flask(__name__)


@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')

def print_csv(filename):
    df = pd.read_csv(filename)
    print(df)


#@app.route('/hello', methods=['GET'])
#def helloworld():
#    if (request.method == 'GET'):
#        data = {"data": "Hello World"}
#        return jsonify(data)

@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    print('apa')
    uploaded_file = request.files['file']

    if uploaded_file.filename != '':
        print(uploaded_file.filename)
        uploaded_file.save('tmp.csv')#uploaded_file.filename)
        print_csv('tmp.csv')
        #print(redirect(url_for('index')))
        df = pd.read_csv('tmp.csv')
        text = df.columns.values[0]
    return render_template('test.html', name=text)
    #return redirect(url_for('test'))




if __name__ == '__main__':
    app.run(debug=True)