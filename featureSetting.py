# All Necessary Library Imports
#from Database import Connector
import threading
from joblib import load
import pandas as pd
import numpy as np
from CustomLogger.logger import Logger

logging = Logger('logFiles/test.log')

class ThreadWithResult(threading.Thread):
    def __init__(self, group=None, target=None, name=None, args=(), kwargs={}, *, daemon=None):
        def function():
            self.result = target(*args, **kwargs)
        super().__init__(group=group, target=function, name=name, daemon=daemon)

def backend(result):
    

    logging.info('INFO', 'Data for Database: {}'.format(result))
    result['Journey_month'] = int(result['Journey_month'])
    result['Journey_day'] = int(result['Journey_day'])
    result['Total_Duration'] = int(result['Total_Duration'])

    
def featureCorrection(result):
   

    logging.info('INFO', 'Data is received  : {}'.format(result))
    result['Journey_month'] = result['Departure_Date'].split('-')[1]
    result['Journey_day'] = result['Departure_Date'].split('-')[2]
    result.pop('submit')
    result.pop('Departure_Date')
    logging.info('INFO', 'Data Cleaned : {}'.format(result))

    frame = pd.read_csv("Removedoutlierfile.csv")
    frame = frame.drop('Price', axis=1)
    frame = frame.append(result, ignore_index=True)
    logging.info('INFO', 'Frame created and data appended')

    frame[['Journey_day', 'Journey_month']] = frame[['Journey_day', 'Journey_month']].astype('int64')
    frame['Total_Duration'] = frame['Total_Duration'].astype('float64')

    frame = pd.get_dummies(frame, drop_first=True)
    logging.info('INFO', 'Dummy variables created from received data')
    scaler = load("Scaling.pkl")
    result = frame.iloc[-1].values
    result = scaler.transform(np.reshape(result, (1, -1)))
    logging.info('INFO', 'Data scaled and sent for prediction')

    return result

def getResult(result):
    
    logging.info('INFO', 'Threading Called !')
    in1 = result
    in2 = result
    thread1 = ThreadWithResult(target=featureCorrection, args=(in1,))
    thread2 = ThreadWithResult(target=backend, args=(in2,))
    logging.info('INFO', 'Threading Created !')
    thread1.start()
    thread2.start()
    logging.info('INFO', 'Threading Started !')
    thread1.join()
    thread2.join()
    logging.info('INFO', 'Threading join !')
    return thread1.result



