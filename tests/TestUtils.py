from tests.TestResults import TestResults
from tests.TestCaseResultDto import TestCaseResultDto
import json
import requests
import os


class TestUtils:
    GUID = "dc66f3c1-630f-40ab-8314-f7bb9ffcb71f"
    # URL = "https://yaksha-prod-sbfn.azurewebsites.net/api/YakshaMFAEnqueue?code=jSTWTxtQ8kZgQ5FC0oLgoSgZG7UoU9Asnmxgp6hLLvYId/GW9ccoLw=="
    URL = "https://compiler.techademy.com/v1/mfa-results/push"

    @classmethod
    def yakshaAssert(self, test_name, result, test_type):
        ref = open("custom.ih", "r")
        customData = ref.read()
        ref.close()
        test_case_results = dict()

        result_status = "Failed"
        result_score = 0
        if result:
            result_status = "Passed"
            result_score = 1

        test_case_result_dto = TestCaseResultDto(test_name, test_type, 1, result_score, result_status, True, "")
        test_case_results[self.GUID] = test_case_result_dto

        hostName = os.environ.get('HOSTNAME')
        attemptId = os.environ.get('ATTEMPT_ID')

        test_results = TestResults(json.dumps(test_case_results), customData, hostName, attemptId)

        final_result = json.dumps(test_results)

        response = requests.post(self.URL, final_result, headers={"Content-Type": "application/json"})
        if response.status_code not in [200, 201]:
            length = len(customData)
            print(f'⚠️ Unable to push test cases from {hostName}, please try again![{length}]')
