# 🧠 Liver Disease Detection Using Machine Learning

A machine learning–based web application that predicts the likelihood of liver disease using patient medical parameters. The system integrates a trained ML model with a Flask backend and a simple web interface.

---

## 📌 Project Overview

Liver disease is a serious health condition that often remains undiagnosed until later stages. This project aims to assist in early detection by leveraging machine learning techniques on clinical data.

Users can input patient details such as age, bilirubin levels, enzyme values, and protein ratios to receive an instant prediction.

---

## 🚀 Features

- Machine learning–based prediction system  
- Simple HTML form for user input  
- Flask backend for model inference  
- Trained and serialized ML model (`.pkl`)  
- Lightweight and fast execution  
- Easy to extend and deploy  

---

## 🛠️ Technologies Used

### Backend & Programming
- Python
- Flask

### Machine Learning
- Scikit-learn
- Pandas
- NumPy

### Frontend
- HTML
- CSS

### Tools
- Jupyter Notebook
- Pickle

---

## 🧪 Machine Learning Models Used

The following models were trained and evaluated:

- Logistic Regression  
- Decision Tree Classifier  
- Random Forest Classifier  
- Support Vector Machine (SVM)  

The best-performing model was selected and saved as:


liver_disease_model.pkl


---

## 📊 Dataset

- Indian Liver Patient Dataset (ILPD)

### Attributes:
- Age  
- Gender  
- Total Bilirubin  
- Direct Bilirubin  
- Alkaline Phosphotase  
- Alamine Aminotransferase (SGPT)  
- Aspartate Aminotransferase (SGOT)  
- Total Proteins  
- Albumin  
- Albumin and Globulin Ratio  

---

## ⚙️ Project Structure

Liver-Disease-Detection/
│
├── app.py
├── liver_disease_model.pkl
├── model_training.ipynb
├── requirements.txt
├── templates/
│ └── index.html
├── static/
│ └── style.css
└── README.md


---

## ▶️ How to Run the Project Locally

### 1. Clone the Repository
git clone https://github.com/your-username/liver-disease-detection.git
cd liver-disease-detection

### 2. Install Dependencies
pip install -r requirements.txt

### 3. Run the Application
python app.py

### 4. Open in Browser
http://127.0.0.1:5000/


---

## 🧠 Prediction Workflow

1. User enters medical details via the web form  
2. Flask backend receives input  
3. Input data is processed and passed to the ML model  
4. Model predicts liver disease presence  
5. Prediction result is displayed to the user  

---

## 📈 Future Enhancements

- Add deep learning models
- Improve UI using Bootstrap or React
- Add database support for storing patient records
- Deploy the application on cloud platforms
- Expose prediction as a REST API

---

## 👤 Author

**Sumanth P**  
Machine Learning & Web Development Enthusiast

---

## 📜 License

This project is licensed under the MIT License.


