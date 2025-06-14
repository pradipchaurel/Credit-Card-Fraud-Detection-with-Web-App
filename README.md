# 🛡️ Credit Card Fraud Detection with Web App

A machine learning-based project to detect fraudulent credit card transactions, integrated with a responsive Flask web interface for real-time CSV upload and fraud prediction.

---

## 📂 Dataset

- **Source**: https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud
- The dataset contains transactions made by European cardholders in September 2013.
- **Classes**:  
  - `0` → Legitimate transaction  
  - `1` → Fraudulent transaction

> ⚠️ Download the dataset manually from Kaggle and place `creditcard.csv` inside the `dataset/` folder.

---

## 🚀 Features

- ✅ Fraud detection using trained ML model
- ✅ CSV file upload for batch prediction
- ✅ Displays summary and previews
- ✅ Responsive frontend using HTML + CSS
- ✅ Robust error handling for invalid files or inputs

---

## 🛠️ Tech Stack

- **Backend**: Python, Flask
- **ML**: Pandas, Scikit-learn, Jupyter Notebook
- **Frontend**: HTML5, CSS3


---

## 📁 Project Structure

Credit-Card-Fraud-Detection-with-Web-App/
├── app.py # Flask app
├── model.pkl # Trained model (pickle file)
├── dataset/
│ └── creditcard.csv # Dataset (download from Kaggle)
├── templates/
│ └── index_csv.html # HTML frontend
└── README.md

## Want to try?
- create folder - Credit-Card-Fraud-Detection-with-Web-App
- Inside this folder place app.py, model.pkl, templates/index_csv.html.
- Inside project folder open command prompt - run app.py
- command to run - python app.py
- open link provided in the console 

## 📁 Machine Learning Model Structure

Credit-Card-Fraud-Detection/
├── model.ipynb 
├── dataset/
│ └── creditcard.csv # Dataset (download from Kaggle)
