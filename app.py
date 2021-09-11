# All Necessary Library Imports
from CustomLogger.logger import Logger
import numpy as np
from flask import Flask, request, render_template
from forms import SignUpForm
from joblib import load
from featureSetting import getResult

# Flask App and Secret Key
app = Flask(__name__)
app.config['SECRET_KEY'] = 'ABC235G5K8'

logging = Logger('logFiles/test.log')


@app.route("/", methods = ['GET','POST'])
def home():
    
    form = SignUpForm()
    if request.method == 'POST':
        logging.info('INFO', 'POST Method is requested')
        if form.is_submitted():
            model = load('Model.pkl')
            logging.info('INFO', 'Model which is in Pickle format is loaded')
            result = request.form.to_dict()
            try:
                logging.info('INFO', 'Data is Converted ')
                result['Total_Duration'] = int(result['Total_Duration'])
                if result['Source'] == result['Destination']:
                    return render_template('index.html', form=form, value1=0, value2=0,Rs='Rs')
                else:
                    if result['Total_Duration'] < 10:
                        result = getResult(result)
                        output = model.predict(result)
                        logging.info('INFO', 'Prediction is done successfully!')
                        minfare = np.round(output) - 1000
                        maxfare = np.round(output) + 1000
                        logging.info('INFO', 'Output displayed!')
                        return render_template('index.html', form=form, value1=int(minfare), value2=int(maxfare),Rs='Rs')
                    else:
                        return render_template('index.html', form=form, value1='Please enter Duration less than 10 Hour')
            except:
                logging.info('ERROR', "Excepted integer got String")
                return render_template('index.html', form=form,value1='PLease Give Duration In numbers Only')


    return render_template('index.html',form=form,value1=None,value2=None)



# Main File Run Debug Mode
if __name__ == "__main__":
    app.run(port=8000)