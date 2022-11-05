from flask import Flask, jsonify, request, render_template, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')

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
        uploaded_file.save('kallekula.csv')#uploaded_file.filename)
        #print(redirect(url_for('index')))
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)