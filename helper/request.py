from requests import get, post, Response
from re import match

class ApiRequest:
  async def get(path: str):
    response: Response = get(url=path)
    if response.status_code == 200:
      if(match('application/json', response.headers['Content-Type'])):
        return response.json()
      else:
        return response.text
    else:
      raise ValueError(response.text)
  
  async def post(path: str, payload: dict):
    response: Response = post(url=path, data=payload)
    if response.status_code == 200:
      if(match('application/json', response.headers['Content-Type'])):
        return response.json()
      else:
        return response.text
    else:
      raise ValueError(response.text)