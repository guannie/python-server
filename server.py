from __future__ import print_function
from flask import Flask, request, jsonify
import json
from datetime import datetime

app = Flask(__name__)
# Change ngrok listening port accordingly
# ./ngrok http 8000


@app.route("/") # take note of this decorator syntax, it's a common pattern
def hello():
    return "Hello World!"

@app.route("/config") # take note of this decorator syntax, it's a common pattern
def config():
    testConfig =  {
    'topicName' : 'deepmap/testUserId',
    'subscriptionBrokerUrl' : 'http://m14.cloudmqtt.com:10761/deepmap/user'
}
    return jsonify(testConfig)


@app.route("/location") # take note of this decorator syntax, it's a common pattern
def location():
    testLocation = {
        'macAddress':'78:31:c1:ca:63:78',
        'ipAddress':'10.0.3.114',
        'mapX':1.52,
        'mapY':80.37143,
        'lat':49.418460769020754,
        'lon':8.675101146161616,
        'ssID':'HDMI-Corporate',
        'lastLocatedTime':'2017-12-07T11:02:00.064+0100',
        'confidenceFactor':64.0,
        'floorNumber':4
}
    return jsonify(testLocation)


@app.route("/receiver", methods=['POST'])
def payload():
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



if __name__ == "__main__":
    app.run()
