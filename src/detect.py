from fastapi import FastAPI
from pydantic import BaseModel
from keras.models import load_model
from tensorflow.keras.losses import CategoricalCrossentropy
from tensorflow.keras.models import load_model
from keras.utils import pad_sequences

import numpy as np
import pickle

# Loading Tokeninzer
with open('tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)
    
max_length = 5

# Loading Model
custom_objects = {'CategoricalCrossentropy': CategoricalCrossentropy}
model = load_model('language_classification.h5' ,custom_objects=custom_objects)

predicted = None

app = FastAPI()
# Define the input schema for the API
class data(BaseModel):
    text:str
     
    
# Define the API 
@app.post("/text")
async def main(data:data):
    sequences = tokenizer.texts_to_sequences([str(data.text)])
    test_data = pad_sequences(sequences, maxlen=max_length) 
    # Make predictions on the new data using the loaded model
    predictions = model.predict(test_data)
    if np.argmax(predictions) == 0:
        predicted = "Arabic"
    elif np.argmax(predictions) == 1:
        predicted = "English"

    return str(predicted)
