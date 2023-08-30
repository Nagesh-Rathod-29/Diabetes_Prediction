from flask import Flask,render_template,request,jsonify
import utils
import config
import traceback

model = utils.Model()


app = Flask(__name__)
@app.route('/')
def home():
#    return jsonify({"Result":"This is Home Page"})
    return render_template('index.html')

@app.route('/predict',methods=['GET','POST'])
def result():
    try:
        if request.method == "GET":
            data = request.args.get

            print("Data :::",data)

            age = data(('Age'))
            print("age:",age)
            bmi = data(('Bmi')) 
            HbA1c_level = data(('HbA1c_Level'))
            blood_glucose_level = data(('Blood_glucose_level'))

            pred =  model.prediction(age,bmi,HbA1c_level,blood_glucose_level)
            output = ""
            if pred == 0:
                output = "Person is not suffering from diabetes".upper()
            else:
                output = "Person is suffering from diabetes".upper()
            
            return render_template('index.html',prediction=output)
    
        else:
            data = request.form.get

            print("Data :::",data)

            age = data(('Age'))
            bmi = data(('Bmi')) 
            HbA1c_level = data(('HbA1c_Level'))
            blood_glucose_level = data(('Blood_glucose_level'))

            pred =  model.prediction(age,bmi,HbA1c_level,blood_glucose_level)
            output = ""
            if pred == 0:
                output = "Person is not suffering from diabetes".upper()
            else:
                output = "Person is suffering from diabetes".upper()
            
            return render_template('index.html',prediction=output)
    
    except:
        print("Error occured")
        print("Error is :",traceback.print_exc())
        
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=config.PORT,debug=True)
