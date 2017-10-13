from __future__ import print_function
from flask import Flask, request, jsonify
import json
from datetime import datetime

app = Flask(__name__)
# Change ngrok listening port accordingly
# ./ngrok http 8000


@app.route("/receiver", methods=['POST'])
def payloa():
    content = request.json
    # print('I got some JSON: {}'.format(request.json))
    print(content)
    print('done')
    print()

    path = 'json/'
    filename = path + str(datetime.now()) + '.json'


    with open('content.json', 'a+') as f:
        f.write(',')
        json.dump(content, f)
        f.close()


    with open(filename, 'w') as f:
       json.dump(content, f)
    return 'ok'