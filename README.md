<p align="center">
 <h1 align="center">Vietnamese News Genre Classifier 📰🇻🇳</h1>
</p>

## 📋 Table of Contents
- [🌟 Introduction](#-introduction)
- [📊 Dataset](#-dataset)
- [🏷️ Categories](#️-categories)
- [🔬 Methodology](#-methodology)
- [📈 Results](#-results)
- [💻 Web Application](#-web-application)
- [🛠️ Requirements](#️-requirements)
- [🚀 Getting Started](#-getting-started)
- [📊 Performance Metrics](#-performance-metrics)
- [🔮 Future Improvements](#-future-improvements)
- [🤝 Contributing](#-contributing)

## 🌟 Introduction

This project harnesses the power of machine learning to predict article genres from *vnexpress.net*, a leading Vietnamese news portal. Our approach encompasses:

- Data extraction and preprocessing
- Feature engineering
- Model optimization across 9 algorithms
- Hyperparameter tuning for optimal performance

The project culminates in a web application that visualizes predictions, demonstrating the practical application of NLP techniques in content categorization for Vietnamese text.

## 📊 Dataset

Our dataset comprises articles from various fields, structured with 6 key attributes:

1. Title
2. Abstract
3. Content
4. Author
5. Date
6. Label

**Location**: `./data/vnexpress_data.csv`

## 🏷️ Categories

| News & Current Affairs | Business & Technology | Lifestyle & Entertainment | Education & Thought |
|------------------------|----------------------|---------------------------|---------------------|
| World                  | Business             | Travel                    | Education           |
| Current Affairs        | Real Estate          | Health                    | Science             |
| Law                    | Digitalization       | Sports                    | Perspective         |
|                        | Vehicles             | Entertainment             |                     |

## 🔬 Methodology

### Trained Models

We employed nine machine learning models, each chosen for its unique strengths in text classification:

1. LogisticRegression
2. MultinomialNB
3. BaggingClassifier
4. DecisionTreeClassifier
5. LinearSVC
6. SGDClassifier
7. KNeighborsClassifier
8. RandomForestClassifier
9. GradientBoostingClassifier

### Training Process

- Data split: 80% training, 20% testing
- Feature extraction: TF-IDF (Term Frequency-Inverse Document Frequency)
- Cross-validation: 5-fold

## 📈 Results

### Initial Model Performance

<p align="center">
  <img src="demo/output1.png" width="900">
</p>

### Optimized Model Performance

After rigorous hyperparameter optimization, our top-performing models achieved the following results:

<p align="center">
  <img src="demo/output2.png" width="900">
</p>

## 💻 Web Application

We developed a Flask-based web application to showcase our model's predictions in real-time.

<p align="center">
  <img src="demo/app.png" width="900" alt="Web Application Interface">
</p>

**Experience it yourself:**
- Run `flask_app.py` locally
- Or visit our live demo: [lethanhhiep.pythonanywhere.com](https://lethanhhiep.pythonanywhere.com)

## 🛠️ Requirements

- Python 3.10
- scikit-learn
- pandas
- underthesea
- Flask 3.0

## 🚀 Getting Started

1. Clone the repository:
`git clone https://github.com/hieplt23/news_classification.git`
2. Run the Flask application:
`python flask_app.py`
3. Open your web browser and navigate to `http://localhost:5000` to use the application.

## 📊 Performance Metrics

We evaluate our models using the following metrics:
- Accuracy
- Precision
- Recall
- F1-score

For detailed performance analysis, refer to the `analysis_model.ipynb` notebook.

## 🔮 Future Improvements

- Implement deep learning models (e.g., LSTM, BERT) for potentially higher accuracy
- Expand the dataset to include more recent articles and diverse sources
- Develop a browser extension for real-time news classification
- Implement multi-language support for classification of news in other languages

## 🤝 Contributing

We welcome contributions! Please feel free to submit a Pull Request.
