import requests
import json
import webbrowser

class Corona_virus_tracker_functions:
    def __init__(self):
        pass

    def get_data(self, item="local_total_cases"):
        end_point = "https://www.hpb.health.gov.lk/api/get-current-statistical"
        information = json.loads(json.dumps(requests.get(end_point).json()))
        return (information["data"][item])

    def visit_site(self):
        url = "https://www.hpb.health.gov.lk/en"
        webbrowser.open(url)

obj1 = Corona_virus_tracker_functions()

