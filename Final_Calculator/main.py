from flask import Flask, request, render_template


app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def hello():
    result = ""
    if request.method =='POST':
        Value = str(request.form.get('answer'))
        result = eval(Value)
        
    return render_template('calc.html',result=result)

if __name__ =='__main__':
    app.run(debug=True)


