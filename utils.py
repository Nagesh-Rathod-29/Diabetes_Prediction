import numpy as np
import pandas as pd
import config
import pickle
import json


class Model:
    def __init__(self):
        self.model = pickle.load(open(config.MODEL_FILE_PATH,'rb'))
        self.scaler = pickle.load(open(config.SCALER_fILE_PATH,'rb'))
        self.model_data = json.load(open(config.MODEL_DATA_FILE,'r'))

    def prediction(self,age,bmi,HbA1c_level,blood_glucose_level):
        test_array = np.array([age,bmi,HbA1c_level,blood_glucose_level],ndmin=2)
        #reshape_array = test_array.reshape(1,-1)

        scaled_array = self.scaler.transform(test_array)

        pred = self.model.predict(scaled_array)
        print("Predicted class:",pred)
        if pred[0] == 0:
            print("Person is not suffering from diabetes".upper())
        else:
            print("Person is suffering from diabetes".upper())

        return pred[0]
    
#if __name__ == "__main__":
#    test = Model()
#    test.prediction(50,27.32,5.7,247.5)