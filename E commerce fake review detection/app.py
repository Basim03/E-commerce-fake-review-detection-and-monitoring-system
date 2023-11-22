from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# %matplotlib inline
import warnings, string
warnings.filterwarnings('ignore')
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import nltk
# import nltk/
nltk.download('stopwords')
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from flask import url_for

app = Flask(__name__)



def text_process(review):
    nopunc = [char for char in review if char not in string.punctuation]
    nopunc = ''.join(nopunc)
    return [word for word in nopunc.split() if word.lower() not in stopwords.words('english')]
# Load your trained fake review detection model
model=pickle.load(open('C:/Users/asmee/Documents/GitHub/E-commerce-fake-review-detection-and-monitoring-system/E commerce fake review detection/model/pipeline.pkl','rb'))



@app.route('/')
def home():
       return render_template('login.html', css=url_for('static', filename='login.css'))


@app.route('/route_to_index')
def route_to_index():
       return render_template('index.html', css=url_for('static', filename='style.css'))



# Define a route to handle review submission and analysis
# Your Python code
from flask import render_template

@app.route('/analyze_review', methods=['POST'])
def analyze_review():
    if request.method == 'POST':
        review = request.form['review_text']
        # Preprocess the review text (cleaning, tokenization, etc.)
        # Use your trained model to make predictions
        prediction = model.predict([review])

        if prediction == 'CG':
            result = "This review is likely fake."
        else:
            result = "This review appears to be genuine."

        return result


if __name__ == '__main__':
    app.run(debug=True)
