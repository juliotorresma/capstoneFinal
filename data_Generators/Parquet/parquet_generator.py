import sys
sys.path.insert(1, '/Users/julitorresma/Desktop/capstoneFinal/data_Generators')
from utils import *
import shutil
import random 
from datetime import datetime
import json
import pandas as pd
import os
'''
    Parquet structure: 
	Id: int
	Customer: Struct
		First_name: String
		Last_name: String
	Amount: int
	ts: timestamp,
	Store_id: int   
''' 
def mainGeneration(size):
    id_list = randomlistID(size+1, size)
    time_stamp = listTimeStamp(size)
    first_names = getFirstNames(size)
    last_names = getLastNames(size)
    amounts = getRandomAmounts(size)
    store_ids = generateStoresIds(size)
    frame = []
    for i in range(size):
        frame.append([id_list[i], first_names[i], last_names[i], amounts[i], time_stamp[i], store_ids[i]])

    df = pd.DataFrame(frame, columns =['Id', 'First_name', 'Last_name', 'Amount', 'ts', 'Store_id'])
    
    deleteFiles("./",".parquet")

    df.to_parquet(f'{datetime.now().timestamp()}.parquet') 
    print(df)

mainGeneration(100)