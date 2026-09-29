# Assuming we will use regression with the neural networks
#  data consists of varying number of vehices, random start and end locations traffic in each zone throughout the trip, traffic in each zone during each time stamp
from tqdm import tqdm
#from google.colab import files
import random
import pandas as pd
import csv
import json



filein = "D:/Layout_updated_2021 (1).csv"
from TrafficPredictionPathPlanning import read_map
zone,zones_dictionary, data, maze1,zone_number_of_cells_dict= read_map(filein)
print(zone_number_of_cells_dict)
from TrafficPredictionPathPlanning import Decentralized_multi_agent_paths
from TrafficPredictionPathPlanning import Zone_business
import PathPlanner
P=PathPlanner




# def data_generator_for_nn(data_points):
data_points = 150000
ip_1 = []
ip_2 = []
ip_3 = []
op_1 = []
for N in tqdm(range(0, data_points)):
    # print(n)
    # n = random. randint(10,15) #randomly generated number between 2 to 20
    n = 1
    A1_n1 = Decentralized_multi_agent_paths(n,data,P)
    # writing number of vehicles begning their trip in each zone
    for A1 in A1_n1:
        A1_n = [A1]
        Zone_start_trip = [0] * (zone + 1)
        Zone_finish_trip = [0] * (zone + 1)
        # Zone_rack=[0]*(zone+1)
        for a in A1_n:
            # print(a)
            # print(a[0])
            temp_init = list(a[0])
            # temp=temp_init[0]
            # temp_init[0]=temp_init[1]
            # temp_init[1]=temp
            temp_init = tuple(temp_init)
            init = zones_dictionary.get(temp_init)
            # print(init)
            # print(data[init])
            Zone_start_trip[init] = Zone_start_trip[init] + 1

        # writing number of vehicles ending their trip in each zone
        for A1 in A1_n:
            A1_n = [A1]
            # print(a[-1])
            temp_final = list(a[-1])
            # temp=temp_final[0]
            # temp_final[0]=temp_final[1]
            # temp_final[1]=temp
            # temp_final=tuple(temp_final)
            temp_final = tuple(temp_final)
            # print(temp_final)
            final = zones_dictionary.get(temp_final)
            # print(final)
            Zone_finish_trip[final] = Zone_finish_trip[final] + 1
        # writing number of vehicles that go to a deck in a zone as intermediate point
        '''for a in A1_n: 
          count={}
          for item in a:
            count[item]=a.count(item)
  
          for item in a: 
            if count==20 and item !=a[0] and item !=a[-1]:
                temp_rack=item
                #temp=temp_rack[0]
                #temp_rack[0]=temp_rack[1]
                #temp_rack[1]=temp
                #temp_rack=tuple(temp_rack)
                rack= zones_dictionary.get(temp_rack)
                Zone_rack[rack]=Zone_rack[rack]+1'''
        # writing zone busy-ness

        Z_n = Zone_business(A1_n,zones_dictionary,zone)

        ip_1.append(Zone_start_trip)

        ip_2.append(Zone_finish_trip)

        # ip_3.append(Zone_rack)

        op_1.append(Z_n)

list_features_op = []
list_features_op.append(ip_1)
list_features_op.append(ip_2)
# list_features_op.append(ip_3)
list_features_op.append(op_1)
'''df = pd.DataFrame({'ip_1':ip_1,'ip_2':ip_2,'ip_3':ip_3,'op_1':op_1})
df.to_csv('/content/gdrive/Shareddrives/Winter Simulation 2021/write4.csv',index=False)
outer_list=list(df)'''

import pickle

with open('D:/data_for_training150000_1v_1t.pkl', 'wb') as f:
    pickle.dump(list_features_op, f)
