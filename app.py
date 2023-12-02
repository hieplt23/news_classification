from flask import Flask, render_template, request, session
import pickle
from underthesea import word_tokenize
import string
import re

# load vietnamese stopwords
with open('./vietnamese-stopwords.txt', encoding='utf8') as f:
    stopwords = f.readlines()
stopwords = [x.strip().replace(' ', '_') for x in stopwords]

# function for clean content input
def data_clean(data):
    data = data.lower()
    data = word_tokenize(data, format="text")
    data = ''.join(char for char in data if char not in (string.punctuation.replace('_', '')))
    data = re.sub(r'\s+', ' ', data).strip()
    data = ' '.join(word for word in data.split() if word not in stopwords)
    
    return data
# function preprocessing app data and return prediction label
def preprocess_data(data):
    with open('data_preprocess_method.pkl', 'rb') as f:
        data_preprocess = pickle.load(f)
        
    clean_data = data_clean(data['news'])
    print(f'Clean content: {clean_data}')
    X_test = data_preprocess.transform([clean_data])
    
    # Load svm model
    with open("./model/svm_model.pkl", 'rb') as f:
        svm_model = pickle.load(f)
    result = svm_model.predict(X_test)
    labels = ['Bat dong san', 'Du lich', 'Giai tri', 'Giao duc', 'Goc nhin','Khoa hoc', 
              'Kinh doanh', 'Phap luat', 'So hoa', 'Suc khoe', 'The gioi', 'The thao', 'Thoi su', 'Xe']
    return f'Prediction label: {labels[result[0]]}'

app = Flask(__name__)
app.config['SECRET_KEY'] = '@lethanhhiep'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/result', methods = ['POST'])
def result():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        print("___________________")
        print(to_predict_list)
        print("___________________")
        result =preprocess_data(to_predict_list)
        session['result_data'] = result
        return render_template("index.html", prediction=result)
    
if __name__ == "__main__":
    app.run(debug=True)  