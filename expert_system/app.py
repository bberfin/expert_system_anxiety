from flask import Flask # flask kütüphanemizi projemize import ettik.
from flask import send_file 
from flask import render_template
from flask import request, redirect, url_for

#from operations.writeJson import write_json
from operations.data import takeQuestions,write_json,write_question_json
from operations.writeToCsv import writeToCsv,deleteCsv
from engine.inference import returnPercentageList
from engine.inference import returnNameList,returnAdvice
from engine.inference import Inference
import json

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
    adviceData= returnAdvice()
    global counter
    counter=-1
    if(adviceData[0]=="True"):
        return render_template('result_page.html', data=percentageData,nameData=nameData, dataLen=percentageData.__len__(),advice_one=adviceData[1],advice_two=adviceData[2],flag="True")
    else:
        return render_template('result_page.html', data=percentageData,nameData=nameData, dataLen=percentageData.__len__(),advice_one=adviceData[1],advice_two=adviceData[2],flag="True")
  



@app.route("/add_questions")
def page_add_questions(): # Bir fonksiyon oluşturduk.

 return render_template('add_questions.html') # Sitemizde görmek istediğimiz şeyi return ettik.

@app.route("/registeredData",methods=["post"])
def page_registeredData(): 

  

    name = request.form['name']
    r1= request.form['rule1']
    r2=request.form['rule2']
    r3= request.form['rule3']
    r4=request.form['rule4']
    r5=request.form['rule5']
    newAnxiety = {"name":name,"rules":{"1":r1,"2":r2,"3":r3,"4":r4,"5":r5} }
    symptoms = list()
    symptoms.append(r1)
    symptoms.append(r2)
    symptoms.append(r3)
    symptoms.append(r4)
    symptoms.append(r5)
    write_json(newAnxiety) 
    write_question_json(symptoms)
    return render_template('registeredData.html',name=name,r1=r1,r2=r2,r3=r3,r4=r4,r5=r5) # Sitemizde görmek istediğimiz şeyi return ettik.
 


              

