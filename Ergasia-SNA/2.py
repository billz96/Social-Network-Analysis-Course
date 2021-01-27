import datetime
import json
import os
from publicConstants import size_of_classes, number_of_classes

# diabazoume to kathe arxeio-klash gia na
# broume to elaxisto kai megisto xroniko diastima
# ta apotelesmata ta grafoume sto arxeio times.json
times = [None] * number_of_classes
for i in range(number_of_classes):
    with open('./data/' + str(i) + '/data.json') as json_file:
        data = json.load(json_file)
        times[i] = {
            'fromdate': str(datetime.datetime.fromtimestamp(data[0]['ts'])),
            'todate': str(datetime.datetime.fromtimestamp(data[size_of_classes - 2]['ts'])),
            'fromtimestamp': int(data[size_of_classes - 2]['ts']),
            'totimestamp': int(data[size_of_classes - 2]['ts']),
            'classlength': len(data)
        }

if os.path.exists('./data/times.json'):
    os.remove('./data/times.json')
f = open('./data/times.json', 'x')
f.write(json.dumps(times))
f.close()