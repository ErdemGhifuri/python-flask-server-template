from flask import Blueprint, make_response, Response
from json import dumps

# services
from services.webScraping import WebScraping

# route
routing: Blueprint = Blueprint('routing', __name__)

@routing.route('/')
async def index():
  response: Response = None
  status: int = None
  try:
    response: Response = make_response(dumps({ 'status': 'SUCCESS', 'message': 'Service is up and running' }))
    status = 200
  except Exception as error:
    print(error)
    response: Response = make_response(dumps({ 'status': 'FAILED', 'message': 'Service is offline' }))
    status = 503
  finally:
    response.headers['Content-Type'] = 'application/json'
    return response, status

@routing.route('/web-scrapping')
async def webScraping():
  response: Response = None
  status: int = None
  try:
    data = await WebScraping.scrape()
    response: Response = make_response(dumps({ 'status': 'SUCCESS', 'data': data }))
    status = 200
  except Exception as error:
    print(error)
    response: Response = make_response(dumps({ 'status': 'FAILED', 'message': 'INTERNAL_ERROR' }))
    status = 500
  finally:
    response.headers['Content-Type'] = 'application/json'
    return response, status

@routing.route('/<path:path>', methods=['GET', 'POST'])
async def notFound(path: str):
  response: Response = make_response()
  response.headers['Content-Type'] = 'application/json'
  return response, 404