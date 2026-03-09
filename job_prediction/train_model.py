
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle

df = pd.read_csv("data/jobs_sample.csv")

X_train,X_test,y_train,y_test = train_test_split(df["description"],df["label"],test_size=0.3,random_state=42)

vectorizer = TfidfVectorizer(stop_words="english")
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

model = LogisticRegression()
model.fit(X_train_vec,y_train)

pred = model.predict(X_test_vec)
print("Accuracy:",accuracy_score(y_test,pred))

with open("model.pkl","wb") as f:
    pickle.dump((vectorizer,model),f)
