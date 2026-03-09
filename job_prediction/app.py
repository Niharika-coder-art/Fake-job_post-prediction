
from flask import Flask,render_template,request
import pickle

app = Flask(__name__)

with open("model.pkl","rb") as f:
    vectorizer,model = pickle.load(f)

@app.route("/",methods=["GET","POST"])
def home():
    result=None
    if request.method=="POST":
        text=request.form["jobtext"]
        vec=vectorizer.transform([text])
        pred=model.predict(vec)[0]
        result="Fake Job Post" if pred==1 else "Real Job Post"
    return render_template("index.html",result=result)

if __name__=="__main__":
    app.run(debug=True)
