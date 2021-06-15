from flask import Flask, render_template, request
import pickle
from preprocess import preprocess_text
from config import Config
from form import ClassifyForm

app = Flask(__name__)
app.config.from_object(Config)

cv = pickle.load(open('NLP_models/vectorizer.pkl','rb'))
model_NB = pickle.load(open('NLP_models/NB.pkl','rb'))
model_SVM = pickle.load(open('NLP_models/SVM.pkl','rb'))

# ROUTES
@app.route('/', methods=['GET', 'POST'])
def index():
  form = ClassifyForm(request.form)
  if request.method == 'POST' and form.validate():
    # get text data from POST request
    data = form.textarea
  
    # preprocess text
    text = preprocess_text(str(data))
    
    # vectorize text
    text_in_array = []
    text_in_array.append(preprocess_text(text))
    vectorized_text = cv.transform(text_in_array)
    
    # make prediction
    prediction_NB = model_NB.predict(vectorized_text)
    prediction_SVM = model_SVM.predict(vectorized_text)
  
    # return model outputs
    results = {
      "NB": prediction_NB[0],
      "SVM": prediction_SVM[0]
    }

    return render_template('predictions.html', results=results)
    
  return render_template('index.html', form=form)

# APP START
if __name__ == '__main__':
  app.run()