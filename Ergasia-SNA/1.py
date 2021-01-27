import json
import shutil
import pandas as pd
import os
from publicConstants import size_of_classes, number_of_classes

# convert .txt to .csv file
df = pd.read_csv('./data/all.txt', sep=" ", header=None)
df.columns = ["source_id", "target_id", "timestamp"]

data_source_id = df['source_id']
data_target_id = df['target_id']
data_timestamp = df['timestamp']
df = ''

# first question
min_timestamp = min(data_timestamp)
max_timestamp = max(data_timestamp)
edge_length = len(data_timestamp)


# split to classes
counter_class = 0
j = 0
temprecord = [None] * (size_of_classes)
for i in range(size_of_classes * number_of_classes):
    temprecord[j] = {
        's': int(data_source_id[i]),
        't': int(data_target_id[i]),
        'ts': int(data_timestamp[i])
    }
    j = j + 1
    if j == size_of_classes:
        print(counter_class)
        if os.path.exists('./data/' + str(counter_class)):
            shutil.rmtree('./data/' + str(counter_class))
        os.mkdir('./data/' + str(counter_class))
        f = open('./data/' + str(counter_class) + '/data.json', 'x')
        f.write(json.dumps(temprecord))
        f.close()
        counter_class = counter_class + 1
        j = 0