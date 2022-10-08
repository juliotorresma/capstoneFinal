import sys
sys.path.insert(1, '/Users/julitorresma/Desktop/capstoneFinal/data_Generators')
from utils import *
import shutil
import random 
import json
import datetime
import os

'''
‘id’:1,-- done 
“ts”: 2022--06-06T22:06:06,-- done 
“Customer_first_name” : “test”-- done
“Customer_last_name”: “test”, --done
“Amount”: 1000 --done
“Type” : “0” # 0 - in_store, 1-online --done
'''

def mainGenerator(size):
    id_list = randomlistID(1, size)
    time_stamp = listTimeStamp(size)
    first_names = getFirstNames(size)
    last_names = getLastNames(size)
    amounts = getRandomAmounts(size)
    types = generateRandomTypes(size)
    
    deleteFiles("./",".json")

    with open(f'{datetime.datetime.now().timestamp()}.json', 'w') as f:
        for i in range(size):
            json_format = {"id":id_list[i],
                        "ts":time_stamp[i],
                        "customer_first_name":first_names[i],
                        "customer_last_name":last_names[i],
                        "amount":amounts[i],
                        "type":types[i]}

            json_line = json.dumps(json_format)
            f.write(json_line)
            f.write('\n')
    
mainGenerator(100)