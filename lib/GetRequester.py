import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        returned_data = []
        returns = json.loads(self.get_response_body())
        for returned in returns:
            returned_data.append(returned)
        return returned_data 

get_requester = GetRequester("https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json")

response_json = get_requester.load_json()
# response_content = get_requester.get_response_body()
print (response_json)
# print(response_content)
