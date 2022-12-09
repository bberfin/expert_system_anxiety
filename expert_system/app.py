
from flask import Flask # flask kütüphanemizi projemize import ettik.
from flask import render_template
from flask import request, redirect, url_for

from operations.data import takeQuestions
from operations.writeToCsv import writeToCsv, deleteCsv
from engine.inference import returnPercentageList
from engine.inference import returnNameList
from engine.inference import Inference


app = Flask(__name__) # app değişkenizimizin Flask olduğunu belirttik.

global counter
counter=-1
knowledgeBaseFile = "static/jsonFiles/knowledge.json"
clauseBaseFile = "static/jsonFiles/clause.json"

@app.route("/") # Endpoint imizi tanımladık.
def page_main(): # Bir fonksiyon oluşturduk.
    deleteCsv()
    return render_template('main_page.html') # Sitemizde görmek istediğimiz şeyi return ettik.

@app.route("/question_page", methods=["GET", "POST"])
def page_question():
  
    global counter
    data= takeQuestions()
    if(counter+1 == len(data)):
        isDone=True
    else:
        isDone=False
        
    if (isDone == False):
        counter+=1
        if request.method == 'POST':
            answer = request.form.get('ans')
            if (answer == "yes"):
                writeToCsv(data[counter-1])        
        return render_template('question_page.html', question=data[counter], finish="False")
    else:
        return render_template('question_page.html', question=data[counter], finish="True")

@app.route("/result_page")
def page_result():
    inferenceEngine = Inference()
    inferenceEngine.startEngine(knowledgeBaseFile,
                            clauseBaseFile,
                            verbose=True,
                            method=inferenceEngine.FORWARD)
    percentageData = returnPercentageList()
    nameData = returnNameList()
    global counter
    counter=-1
    return render_template('result_page.html', data=percentageData,nameData=nameData, dataLen=percentageData.__len__())