# Fake Job Post Detection using Machine Learning

## 📌 Project Overview

Fake job postings are a growing problem on online job portals. Many fraudulent recruiters post misleading job advertisements to scam job seekers.

This project uses **Machine Learning and Natural Language Processing (NLP)** to analyze job descriptions and predict whether a job posting is **Fake or Real**.

A **Flask web application** is built to allow users to input a job description and instantly get a prediction.

---

## 🚀 Features

* Detects **Fake Job Posts**
* Identifies **Legitimate Job Posts**
* Uses **TF-IDF for text processing**
* Machine Learning classification model
* Simple **Flask web interface**
* Real-time job post prediction

---

## 🛠️ Technologies Used

* Python
* Flask
* Scikit-learn
* TF-IDF Vectorization
* Logistic Regression
* HTML / CSS
* Git & GitHub

---

## 📂 Project Structure

```
fake-job-detection/
│
├── app.py
├── train_model.py
├── model.pkl
├── requirements.txt
├── README.md
│
├── data/
│   └── jobs_sample.csv
│
├── templates/
│   └── index.html
│
└── images/
    ├── fake job model.png
    ├── real job prediction.png
    └── fake job prediction.png
```

---

## ⚙️ How to Run the Project

### 1️⃣ Clone the repository

```
git clone https://github.com/Niharika_coder_art/fake-job-post-detection-ml.git
```

### 2️⃣ Install dependencies

```
pip install -r requirements.txt
```

### 3️⃣ Train the model

```
python train_model.py
```

### 4️⃣ Run the Flask application

```
python app.py
```

### 5️⃣ Open the application

```
http://127.0.0.1:5000
```

---

## 🧠 Machine Learning Model

The project uses **TF-IDF vectorization** to convert job descriptions into numerical features and trains a **Logistic Regression classifier** to predict whether a job posting is fake or real.

### Model Architecture

![job prediction model](https://github.com/user-attachments/assets/8cc637cd-19ef-4fb0-9ded-82b9ac53ad74)

---

## 📊 Prediction Results

### Real Job Prediction

![real job prediction](https://github.com/user-attachments/assets/6543be74-2316-4027-9768-71ed9e5ac9ce)

### Fake Job Prediction

![fake job prediction](https://github.com/user-attachments/assets/4c53e456-c349-47a2-9c6e-3d52eba56676)


---

## 🎯 Applications

This system can be used in:

* Online Job Portals
* Recruitment Platforms
* HR Systems
* Job Aggregator Websites

It helps protect job seekers from fraudulent job postings.

---

## 📈 Future Improvements

* Use a **larger dataset**
* Add **deep learning models**
* Deploy using **Streamlit or cloud**
* Add **job posting verification system**
* Improve prediction accuracy

---

## 👩‍💻 Author

**Niharika Chinthada**
B.Tech – Artificial Intelligence & Machine Learning
