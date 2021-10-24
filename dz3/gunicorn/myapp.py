import datetime
import json


def app(environ, start_response):
    data_set = {"time": datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"),
                "url": environ['HTTP_HOST']+environ['RAW_URI']}
    data = json.dumps(data_set)
    status = '200 OK'
    print(environ)
    response_headers = [
        ('Content-type', 'application/json'),
        ('Content-Length', str(len(data)))
    ]
    start_response(status, response_headers)
    return [bytes(data, 'utf-8')]