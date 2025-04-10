import requests
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import project_enviorment.GetData as GetData
from project_enviorment.GetData import VarData, data

class PageOutputDTO:
    def __init__(self, page):
        self.result = {"page": page}
    def to_json(self):
        return self.data

def test_baba():
    url = GetData.loaded_data[VarData.BaseApiUrl] +"users?page=2"
    headers = GetData.get_headers()
    response = requests.get(url, headers=headers)
    assert response.status_code == 200

    response_data = response.json()
    output_dto = PageOutputDTO(response_data['page'])
    assert output_dto.result['page']==2



