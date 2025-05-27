import json


class TestResults(dict):
    testCaseResults = ""
    customData = ""
    hostName = ""
    attemptId = ""

    def __init__(self, testCaseResults, customData, hostName, attemptId):
        dict.__init__(self, testCaseResults=testCaseResults, customData=customData, hostName=hostName,
                      attemptId=attemptId)
