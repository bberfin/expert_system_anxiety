import json

with open('static/jsonFiles/questions.json') as f:
  veri = json.load(f)
  


def takeQuestions():  
    rule_no=1
    target_no=0
    theList = list()
    for i in veri["target"][target_no]["rules"]:
        theList.append(veri["target"][target_no]["rules"][str(rule_no)])#veri["target"][0]["rules"][str(i+1)]
        rule_no+=1

    return theList