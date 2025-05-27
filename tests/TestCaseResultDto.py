import json

class TestCaseResultDto(dict):
    methodName = ""
    methodType = ""
    actualScore = 0
    earnedScore = 0
    status = ""
    isMandatory = True
    erroMessage = ""
    
    def __init__(self, methodName, methodType, actualScore, earnedScore, status, isMandatory, erroMessage):
        dict.__init__(self, methodName=methodName, methodType=methodType, actualScore=actualScore, 
                     earnedScore=earnedScore, status=status, isMandatory=isMandatory, erroMessage=erroMessage)