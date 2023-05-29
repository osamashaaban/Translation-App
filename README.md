# Language Detection and Translation App
- This project is designed to showcase the implementation of a Natural Language Processing (NLP) models for classify the Arabic and English text and translate it from Arabic to English and vice versa.
## ***Project Overview***
### The project consists of three main components:
#### a. Language Detection Model - CNN model
#### b. Language Translation Model - Transformer model
#### c. Two APIs and a User Interface for input and output displaying
## ***Technologies Used***
- Numpy, Pandas
- Tensorflow, Keras, sklearn
- pyarabic
- CNN , Transformer
- FastAPI, Streamlit

## ***Evaluation***
- I used the F1 score for the detecttion model as it is the harmonic mean of precision and recall, and provides a single value that balances both metrics.
- Translation models were pre-trained transformer models 

## ***Run The App***
##### After installing all dependencies from the ```"requirements.txt"``` file, you can use this command
```
$ pip install -r requirements.txt
```
- Open ```cmd``` from ```src``` from the project directory
- Write this command to run the detection model from detect.py
```
$ uvicorn detect:app --reload --port=8050
```
- Write this command to run the translation model from translate.py
```
$ uvicorn translate:app --reload --port=9000
```
- To run the App
```
$ streamlit run app.py      
```

Once the web applications are running, you can visitthe Streamlit app in your web browser at http://localhost:8501 or http://localhost:8502 to interact with the NLP model.




## ***Valid Test Cases***
- Enter an English word or sentence and click on ```"Detect Language"``` button
- Enter an Arabic word or sentence and click on ```"Detect Language"``` button
- Click on ```"Translate your blog"``` button to print the sentence and the translation from Arabic to English or English to Arabic based on the language of the inputted sentence
- Check the Response time printed in seconds 

## ***Invalid - Not Supported Test Cases***
- Translate the sentence before detecting its the language
- Enter a sentence of english and arabic together
    - Example:
```
The book is good -  الكتاب جيد
```
- Enter a sentence in anther language than Arabic and English
    - Examples:
```
Chinise: 这是一种不受支持的语言
Greek: Αυτή είναι μια μη υποστηριζόμενη γλώσσα
Russian: Это не поддерживаемый язык
```
- Enter just numbers or non-alphanumeric or both
    - Examples:
```
Sentence: “42” 
Sentence: “?!!!!!!?"
Sentence: "42?!!!!!?"
```
## ***Examples***
- Valid
<img src="valid.png" alt="Alt text">
- Invalid
<img src="invalid.png" alt="Alt text">

## ***Future Problems***
- I tried to train the model on some other languages you provided and I found that if the language has some English characters it will classify it wrongly as English and the model F1-Score was 0.34 (Max), and if the language is non-Latin it will classify it as Arabic. That is why I thought I need to use a transformer or just the embedding layer of a pre-trained model but it will make the classification task very hard and will not be accurate too in addition it will take more than 0.5 sec and the model will not be light weighted. so that I concentrated on how to make the classification task simple and fast with a light weight model.


