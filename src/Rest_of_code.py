# Number of vehicles =10

from tqdm import tqdm
#from google.colab import files
import random
import pandas as pd
import csv
import json
import numpy as np
#from google.colab import files
import random
import pandas as pd
import csv
import json
from tqdm import tqdm
import pickle
import pickle
import numpy as np
import keras
import pandas as pd
# load the dataset
import pickle
import numpy as np
import keras
from tqdm import tqdm
# from google.colab import files
import random
import pandas as pd
import csv
import json
# from google.colab import files
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

# Number of vehicles =10




# def data_generator_for_nn(data_points):
data_points = 5
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
df.to_csv('/content/gdrive/Shareddrives/Winter Simulation 2021/write4_6_22_2021_1.csv',index=False)
outer_list=list(df)'''


with open('D:/data_for_pathplanning6_25_2021_7V.pkl', 'wb') as f:
    pickle.dump(list_features_op, f)









#print(len(ip_1))
'''print(sum(ip_1[0]))
print(sum(ip_1[1]))
print(sum(ip_1[2]))
print(sum(ip_1[3]))'''

print(sum(ip_2[0]))
print(sum(ip_2[1]))
print(sum(ip_2[2]))
print(sum(ip_2[3]))

import pandas as pd
# load the dataset


# pickle_off = open("/content/gdrive/Shareddrives/Winter Simulation 2021/data_for_pathplanning1.pkl","rb")
pickle_off = open("D:/data_for_pathplanning6_25_2021_7V.pkl", "rb")
emp = pickle.load(pickle_off)
print(len(emp[0]))
arr = np.asarray(emp)
X_P = np.array(emp[:2][:][:])
y_P = np.array(emp[2][:][:])
X_P = X_P.reshape(len(X_P[0]), len(X_P[0][0]), len(X_P))
y_P = y_P.reshape(len(y_P), len(y_P[0]))

arr = np.asarray(emp)

X_P = np.array(emp[:2][:][:])
y_P = np.array(emp[2][:][:])

X_P = X_P.reshape(len(X_P[0]), len(X_P[0][0]), len(X_P))
y_P = y_P.reshape(len(y_P), len(y_P[0]))

arr = y_P
shape = arr.shape
result_P = np.zeros(shape)
for x in range(0, shape[0]):
    for z in range(0, shape[1]):
        if arr[x][z] >= 1:
            result_P[x][z] = 1
        else:
            result_P[x][z] = 0





print(result_P)
print(sum(sum(result_P)))



#result_P=np.load('D:/predicted_zones_6_25_21_7V.npy')
#print(result_P)


import numpy as np
filein = "D:/Layout_updated_2021 (1).csv"
data = np.loadtxt(open(filein, "rb"), delimiter=",")
#print(data)
maze1=np.array(data)
maze1 = np.where(maze1 == 100, 1, maze1)
maze1 = np.where(maze1 == -1, 1, maze1)
maze1 = np.where(maze1 == 200, 1, maze1)
maze1 = np.where(maze1 == 50, 0, maze1)


Zone_total=[0]*(zone+1)
trip=-1
for re in result_P:
      #print(re)
      print(type(re))
      print(len(re))
      c=-1
      trip=trip+1
      if (trip/2)==0:
        Zone_temp=[0]*(zone+1)
        for r in re:
            c=c+1
            #print(r)
            if r==1:
                Zone_total[c]=Zone_total[c]+1
                Zone_temp[c]=1
      if (trip/2)!=0:
        for r in re:
            c=c+1
            if r==1:
              if (Zone_temp[c]!=1):
                Zone_total[c]=Zone_total[c]+1

print(sum(Zone_total))

counter=-1

key=[]
for z in Zone_total:
  counter=counter+1
  if z>=1:
     #val=zones_dictionary.get(a)
     key.append(next(((k,i) for (k,i) in zones_dictionary if zones_dictionary[(k,i)] == counter), None))
     #zones_dictionary.keys()[zones_dictionary.values(counter)]
     for i in zones_dictionary:
       #print(i)
       if zones_dictionary[i]==counter:
         key.append(i)


maze_2=maze1
print(key)
for k in key:
  maze_2[k]=0.6

from matplotlib import pyplot
import matplotlib as mpl

fig = pyplot.figure(2)

cmap2 = mpl.colors.LinearSegmentedColormap.from_list('my_colormap',
                                           ['orange','green'],
                                           256)

img2 = pyplot.imshow(maze_2,interpolation='nearest',
                    cmap = cmap2,
                    origin='lower')

pyplot.colorbar(img2,cmap=cmap2)

fig.savefig("D:/image_test_more_than_orequal3.png")



Zone_total=[0]*(zone+1)
trip=-1
for re in result_P:
      #print(re)
      print(type(re))
      print(len(re))
      c=-1
      trip=trip+1
      if (trip/2)==0:
        Zone_temp=[0]*(zone+1)
        for r in re:
            c=c+1
            #print(r)
            if r==1:
                Zone_total[c]=Zone_total[c]+1
                Zone_temp[c]=1
      if (trip/2)!=0:
        for r in re:
            c=c+1
            if r==1:
              if (Zone_temp[c]!=1):
                Zone_total[c]=Zone_total[c]+1

print(sum(Zone_total))


# pickle_off = open("/content/gdrive/Shareddrives/Winter Simulation 2021/data_for_pathplanning4.pkl","rb")
pickle_off = open("D:/data_for_pathplanning6_25_2021_7V.pkl", "rb")
emp = pickle.load(pickle_off)
print(len(emp[0]))
arr = np.asarray(emp)
X_P = np.array(emp[:2][:][:])
y_P = np.array(emp[2][:][:])
X_P = X_P.reshape(len(X_P[0]), len(X_P[0][0]), len(X_P))
y_P = y_P.reshape(len(y_P), len(y_P[0]))

arr = np.asarray(emp)

X_P = np.array(emp[:2][:][:])
y_P = np.array(emp[2][:][:])

X_P = X_P.reshape(len(X_P[0]), len(X_P[0][0]), len(X_P))
y_P = y_P.reshape(len(y_P), len(y_P[0]))

arr = y_P
shape = arr.shape
result_P = np.zeros(shape)
for x in range(0, shape[0]):
    for z in range(0, shape[1]):
        if arr[x][z] >= 1:
            result_P[x][z] = 1
        else:
            result_P[x][z] = 0

import numpy as np

filein = "D:/Layout_updated_2021 (1).csv"
data = np.loadtxt(open(filein, "rb"), delimiter=",")
# print(data)
maze1 = np.array(data)
maze1 = np.where(maze1 == 100, 1, maze1)
maze1 = np.where(maze1 == -1, 1, maze1)
maze1 = np.where(maze1 == 200, 1, maze1)
maze1 = np.where(maze1 == 50, 0, maze1)

Zone_total = [0] * (zone + 1)
trip = -1
for re in result_P:
    # print(re)
    print(type(re))
    print(len(re))
    c = -1
    trip = trip + 1
    if (trip / 2) == 0:
        Zone_temp = [0] * (zone + 1)
        for r in re:
            c = c + 1
            # print(r)
            if r == 1:
                Zone_total[c] = Zone_total[c] + 1
                Zone_temp[c] = 1
    if (trip / 2) != 0:
        for r in re:
            c = c + 1
            if r == 1:
                if (Zone_temp[c] != 1):
                    Zone_total[c] = Zone_total[c] + 1

fig.savefig("D:/image_test_more_than_orequal3.png")




# def data_generator_for_nn(data_points):
data_points = 5
ip_1 = []
ip_2 = []
ip_3 = []
op_1 = []

from tqdm.auto import tqdm

m1 = 0
m2 = 0
m1_list = []
m2_list = []
not_giving_up = 0
time_list_no_traffic_avoidance = []
time_list_Traffic_Avoidance = []

for not_giving_up in tqdm(range(1)):
    number_of_times_all_vehicles_can_be_avoided = 0
    number_of_times_its_useful = 0
    trial_list = []
    sum_total_time = 0
    distance_total = 0
    time_list_No_Avoidance = []
    distance_list_No_Avoidance = []
    time_list_Traffic_Avoidance = []
    distance_list_Traffic_Avoidance = []
    no_of_vehicles_noT = []
    no_of_vehicles_T = []
    # with tqdm(total=100, position=0, leave=True) as pbar:
    for trial in range(100):
        # Step1
        from tqdm import tqdm

        data_points = 1
        ip_1_s = []
        ip_2_f = []
        op_1_t = []
        count_data = 1
        distance_travelled_by_Native_AStar = []
        time_taken_by_Native_AStar = []
        distance_travelled_avoiding1V = []
        time_taken_avoiding1V = []
        distance_travelled_avoiding2V = []
        time_taken_avoiding2V = []
        distance_travelled_avoiding3V = []
        time_taken_avoiding3V = []
        while count_data < 2:
            count_data = count_data + 1
            # data_points=1
            for N in tqdm(range(0, data_points)):
                ip_1_s = []
                ip_2_f = []
                op_1_t = []
                n = 1
                A1_n1_path = Decentralized_multi_agent_paths(n,data,P)
                # writing number of vehicles begning their trip in each zone
                for A1 in A1_n1_path:
                    A1_n = [A1]
                    Zone_start_trip = [0] * (zone + 1)
                    Zone_finish_trip = [0] * (zone + 1)
                    # Zone_rack=[0]*(zone+1)
                    for a in A1_n:
                        temp_init = list(a[0])

                        temp_init = tuple(temp_init)
                        init = zones_dictionary.get(temp_init)

                        Zone_start_trip[init] = Zone_start_trip[init] + 1

                    # writing number of vehicles ending their trip in each zone
                    for A1 in A1_n:
                        A1_n = [A1]

                        temp_final = list(a[-1])

                        temp_final = tuple(temp_final)
                        # print(temp_final)
                        final = zones_dictionary.get(temp_final)
                        # print(final)
                        Zone_finish_trip[final] = Zone_finish_trip[final] + 1
                    # writing number of vehicles that go to a deck in a zone as intermediate point

                    # writing zone busy-ness

                    Z_n_b = Zone_business(A1_n,zones_dictionary,zone)

                    ip_1_s.append(Zone_start_trip)

                    ip_2_f.append(Zone_finish_trip)

                    # ip_3.append(Zone_rack)

                    op_1_t.append(Z_n_b)

            list_features_op_testcase = []
            list_features_op_testcase.append(ip_1_s)
            list_features_op_testcase.append(ip_2_f)
            # list_features_op.append(ip_3)
            list_features_op_testcase.append(op_1_t)

            import pickle

            with open('D:/data_for_pathplanning_test_case2.pkl',
                      'wb') as f:
                pickle.dump(list_features_op_testcase, f)
            with open('D:/start_and_end_point_test_case2.pkl',
                      'wb') as f:
                pickle.dump(A1_n1_path, f)

            import pickle

            pickle_off = open(
                "D:/data_for_pathplanning_test_case2.pkl", "rb")
            emp = pickle.load(pickle_off)

            op_1_t = emp[2][:][:]
            # print(len(op_1_t))
            # print(len(op_1_t[0]))
            arr = np.array(op_1_t)
            shape = arr.shape
            zone_traversed = np.zeros(shape)
            for x in range(0, shape[0]):
                for z in range(0, shape[1]):
                    if arr[x][z] >= 1:
                        zone_traversed[x][z] = 1
                    else:
                        zone_traversed[x][z] = 0
            # print(len(zone_traversed))
            no_of_vehicles_noT

            # o=[sum(sum(zone_traversed))]
            # distance_travelled_by_Native_AStar.append(sum(sum(zone_traversed)))
            # time_A_Star=sum(sum(zone_traversed))
            # distance_list_No_Avoidance.append(time_A_Star)
            distance_A_Star = 0
            time_A_Star = 0

            no_of_vehicles_noTraffic = 0
            # Distance Travelled
            for zone_traversed_counter in zone_traversed:
                for i in range(0, len(zone_traversed[0])):
                    if zone_traversed_counter[i] != 0:
                        if Zone_total[i] == 0:
                            print(zone_number_of_cells_dict)
                            print(len(zone_number_of_cells_dict))
                            print(zone)
                            distance_A_Star = distance_A_Star + zone_number_of_cells_dict[i]
                        if Zone_total[i] == 1:
                            time_A_Star = distance_A_Star + zone_number_of_cells_dict[i]
                            no_of_vehicles_noTraffic = no_of_vehicles_noTraffic + 1
                        if Zone_total[i] == 2:
                            time_A_Star = time_A_Star + 3
                            no_of_vehicles_noTraffic = no_of_vehicles_noTraffic + 2
                        if Zone_total[i] == 3:
                            time_A_Star = time_A_Star + 4
                            no_of_vehicles_noTraffic = no_of_vehicles_noTraffic + 3
                        if Zone_total[i] >= 3:
                            time_A_Star = time_A_Star + Zone_total[i] + 1
                            no_of_vehicles_noTraffic = no_of_vehicles_noTraffic + Zone_total[i]

            for zone_traversed_counter in zone_traversed:
                for i in range(0, len(zone_traversed[0])):
                    if zone_traversed_counter[i] != 0:
                        if Zone_total[i] == 1:
                            time_A_Star = time_A_Star + 2
                            no_of_vehicles_noTraffic = no_of_vehicles_noTraffic + 1
                        if Zone_total[i] == 2:
                            time_A_Star = time_A_Star + 3
                            no_of_vehicles_noTraffic = no_of_vehicles_noTraffic + 2
                        if Zone_total[i] == 3:
                            time_A_Star = time_A_Star + 4
                            no_of_vehicles_noTraffic = no_of_vehicles_noTraffic + 3
                        if Zone_total[i] >= 3:
                            time_A_Star = time_A_Star + Zone_total[i] + 1
                            no_of_vehicles_noTraffic = no_of_vehicles_noTraffic + Zone_total[i]

            time_taken_by_Native_AStar.append(time_A_Star)
            time_list_no_traffic_avoidance.append(time_A_Star)
            no_of_vehicles_noT.append(no_of_vehicles_noTraffic)
            distance_travelled_by_Native_AStar.append(distance_A_Star)

            counter = -1
            time_A_Star = 0

            key = []

            for z in Zone_total:
                counter = counter + 1
                if z >= 1:
                    # val=zones_dictionary.get(a)
                    key.append(
                        next(((k, i) for (k, i) in zones_dictionary if zones_dictionary[(k, i)] == counter), None))
                    # zones_dictionary.keys()[zones_dictionary.values(counter)]
                    for i in zones_dictionary:
                        # print(i)
                        if zones_dictionary[i] == counter:
                            key.append(i)

            maze_2 = maze1
            # print(key)
            for k in key:
                maze_2[k] = 1



            # Start and end positions
            # More specifically - start , shelf, shelf,dock
            init = []
            final = []
            # print(A1_n1_path)
            for A1 in A1_n1_path:
                A1_n = [A1]
                # Zone_rack=[0]*(zone+1)
                for a in A1_n:
                    # print(a)
                    # print(a[0])
                    init.append(a[0])
                    final.append(a[-1])
            # def data_generator_for_nn(data_points):
            data_points = 1
            ip_1_avoid2 = []
            ip_2_avoid2 = []
            op_1_avoid2 = []
            for N in range(0, data_points):
                # print(n)
                # n = random. randint(10,15) #randomly generated number between 2 to 20
                n = 1
                A1_n1_avoid2 = []
                test_planner = P.PathPlanner(maze_2, True)
                # print(init)
                start = init[0]
                # print(type(start))
                start = list(start)
                temp = start
                start[1] = temp[0]
                start[0] = temp[1]
                end = final[0]
                temp1 = end
                end = list(end)
                end[1] = temp1[0]
                end[0] = temp1[1]
                a1 = test_planner.a_star(start, end)
                # print(type(a1))

                start = init[1]
                start = list(start)
                temp = start
                start[1] = temp[0]
                start[0] = temp[1]
                end = final[1]
                temp1 = end
                end = list(end)
                end[1] = temp1[0]
                end[0] = temp1[1]
                a2 = test_planner.a_star(start, end)
                A1_n1_avoid2.append(a1)
                A1_n1_avoid2.append(a2)
                # print(A1_n1_avoid2)
                # print(len(A1_n1_avoid2))
                # print(len(A1_n1_avoid2[0]))
                check = 1
                for A_check_empty in A1_n1_avoid2:
                    if A_check_empty == []:
                        check = 0
                    else:
                        check = check * 1
                if (check == 1):
                    if ((A1_n1_avoid2[0]) == []) and (len(A1_n1_avoid2[1] == 0)):
                        # writing number of vehicles begning their trip in each zone
                        for A1 in A1_n1_avoid2:
                            # print(A1)
                            A1_n = [A1]
                            Zone_start_trip = [0] * (zone + 1)
                            Zone_finish_trip = [0] * (zone + 1)
                            # Zone_rack=[0]*(zone+1)
                            for a in A1_n1_avoid2:
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
                            for A1 in A1_n1_avoid2:
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

                            # writing zone busy-ness

                            Z_n = Zone_business(A1_n1_avoid2,zones_dictionary,zone)

                            ip_1_avoid2.append(Zone_start_trip)

                            ip_2_avoid2.append(Zone_finish_trip)

                            # ip_3.append(Zone_rack)

                            op_1_avoid2.append(Z_n)

            if ((A1_n1_avoid2[0] != []) and (A1_n1_avoid2[1] != [])):
                list_features_op_avoid2 = []
                list_features_op_avoid2.append(ip_1_avoid2)
                list_features_op_avoid2.append(ip_2_avoid2)
                # list_features_op.append(ip_3)
                list_features_op_avoid2.append(op_1_avoid2)
            if ((A1_n1_avoid2[0] == []) or (A1_n1_avoid2[1] == [])):
                print("no path found")
                distance_travelled_avoiding1V.append(0)
                time_taken_avoiding1V.append(0)
            else:
                arr = np.array(op_1_avoid2)
                shape = arr.shape
                zone_traversed_1 = np.zeros(shape)
                for x in range(0, shape[0]):
                    for z in range(0, shape[1]):
                        if arr[x][z] >= 1:
                            zone_traversed_1[x][z] = 1
                        else:
                            zone_traversed_1[x][z] = 0

                # print(zone_traversed_1.shape)
                time_taken_A_Star_avoid2 = sum(zone_traversed_1)
                distance_travelled_avoiding1V.append(time_taken_A_Star_avoid2)
                # print(time_taken_A_Star_avoid2)

                for zone_traversed_1 in op_1_avoid2:
                    for i in range(0, len(zone_traversed[0])):
                        if zone_traversed_counter[i] != 0:
                            if Zone_total[i] == 1:
                                time_taken_A_Star_avoid2 = time_taken_A_Star_avoid2 + 2
                            if Zone_total[i] == 2:
                                time_taken_A_Star_avoid2 = time_taken_A_Star_avoid2 + 3
                            if Zone_total[i] == 3:
                                time_taken_A_Star_avoid2 = time_taken_A_Star_avoid2 + 4

                time_taken_avoiding1V.append(time_taken_A_Star_avoid2)

                del (time_taken_A_Star_avoid2)

            import numpy as np

            filein = "D:/Layout_updated_2021 (1).csv"
            data = np.loadtxt(open(filein, "rb"), delimiter=",")
            # print(data)
            maze1 = np.array(data)
            maze1 = np.where(maze1 == 100, 1, maze1)
            maze1 = np.where(maze1 == -1, 1, maze1)
            maze1 = np.where(maze1 == 200, 1, maze1)
            maze1 = np.where(maze1 == 50, 0, maze1)

            Zone_total = [0] * (zone + 1)
            trip = -1
            for re in result_P:
                # print(re)
                # print(type(re))
                # print(len(re))
                c = -1
                trip = trip + 1
                if (trip / 2) == 0:
                    Zone_temp = [0] * (zone + 1)
                    for r in re:
                        c = c + 1
                        # print(r)
                        if r == 1:
                            Zone_total[c] = Zone_total[c] + 1
                            Zone_temp[c] = 1
                if (trip / 2) != 0:
                    for r in re:
                        c = c + 1
                        if r == 1:
                            if (Zone_temp[c] != 1):
                                Zone_total[c] = Zone_total[c] + 1

            key = []
            counter = -1
            for z in Zone_total:
                counter = counter + 1
                if z >= 2:
                    # val=zones_dictionary.get(a)
                    key.append(
                        next(((k, i) for (k, i) in zones_dictionary if zones_dictionary[(k, i)] == counter), None))
                    # zones_dictionary.keys()[zones_dictionary.values(counter)]
                    for i in zones_dictionary:
                        # print(i)
                        if zones_dictionary[i] == counter:
                            key.append(i)

            maze_3 = maze1
            # print(key)
            for k in key:
                maze_3[k] = 1

            from tqdm import tqdm


            # Start and end positions
            # More specifically - start , shelf, shelf,dock
            init = []
            final = []
            # print(A1_n1_path)
            for A1 in A1_n1_path:
                A1_n = [A1]
                # Zone_rack=[0]*(zone+1)
                for a in A1_n:
                    # print(a)
                    # print(a[0])
                    init.append(a[0])
                    final.append(a[-1])
            # def data_generator_for_nn(data_points):
            data_points = 1
            ip_1_avoid2 = []
            ip_2_avoid2 = []
            op_1_avoid2 = []
            for N in range(0, data_points):
                # print(n)
                # n = random. randint(10,15) #randomly generated number between 2 to 20
                n = 1
                A1_n1_avoid2 = []
                test_planner = P.PathPlanner(maze_3, True)
                # print(init)
                start = init[0]
                # print(type(start))
                start = list(start)
                temp = start
                start[1] = temp[0]
                start[0] = temp[1]
                end = final[0]
                temp1 = end
                end = list(end)
                end[1] = temp1[0]
                end[0] = temp1[1]
                a1 = test_planner.a_star(start, end)
                # print(type(a1))

                start = init[1]
                start = list(start)
                temp = start
                start[1] = temp[0]
                start[0] = temp[1]
                end = final[1]
                temp1 = end
                end = list(end)
                end[1] = temp1[0]
                end[0] = temp1[1]
                a2 = test_planner.a_star(start, end)
                A1_n1_avoid2.append(a1)
                A1_n1_avoid2.append(a2)
                # print(A1_n1_avoid2)
                # print(len(A1_n1_avoid2))
                check = 1
                for A_check_empty in A1_n1_avoid2:
                    if A_check_empty == []:
                        check = 0
                    else:
                        check = check * 1
                if ((A1_n1_avoid2[0] != -1) and (A1_n1_avoid2[1] != -1)):
                    if (check == 1):
                        if ((A1_n1_avoid2[0] != []) and (A1_n1_avoid2[1] != [])):
                            # writing number of vehicles begning their trip in each zone
                            for A1 in A1_n1_avoid2:
                                # print(A1)
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

                                # writing zone busy-ness

                                Z_n = Zone_business(A1_n1_avoid2,zones_dictionary,zone)

                                ip_1_avoid2.append(Zone_start_trip)

                                ip_2_avoid2.append(Zone_finish_trip)

                                # ip_3.append(Zone_rack)

                                op_1_avoid2.append(Z_n)

            if (A1_n1_avoid2[0] != -1 and A1_n1_avoid2[0] != -1):
                list_features_op_avoid2 = []
                list_features_op_avoid2.append(ip_1_avoid2)
                list_features_op_avoid2.append(ip_2_avoid2)
                # list_features_op.append(ip_3)
                list_features_op_avoid2.append(op_1_avoid2)
            if ((A1_n1_avoid2[0] == -1) or (A1_n1_avoid2[1] == -1)):
                print("no path found")
                distance_travelled_avoiding2V.append(0)
                time_taken_avoiding2V.append(0)
            else:
                arr = np.array(op_1_avoid2)
                shape = arr.shape
                zone_traversed_1 = np.zeros(shape)
                for x in range(0, shape[0]):
                    for z in range(0, shape[1]):
                        if arr[x][z] >= 1:
                            zone_traversed_1[x][z] = 1
                        else:
                            zone_traversed_1[x][z] = 0

                if (zone_traversed_1 != []):
                    avoid_2_more = 0
                    time_taken_A_Star_avoid2 = sum(sum(zone_traversed_1))
                    distance_travelled_avoiding2V.append(time_taken_A_Star_avoid2)
                    # print(time_taken_A_Star_avoid2)
                    for zone_traversed_1 in op_1_avoid2:
                        for i in range(0, len(zone_traversed[0])):
                            if zone_traversed_counter[i] != 0:
                                if Zone_total[i] == 1:
                                    time_taken_A_Star_avoid2 = time_taken_A_Star_avoid2 + 2
                                    avoid_2_more = avoid_2_more + 1
                                if Zone_total[i] == 2:
                                    time_taken_A_Star_avoid2 = time_taken_A_Star_avoid2 + 3
                                    avoid_2_more = avoid_2_more + 2
                                if Zone_total[i] == 3:
                                    time_taken_A_Star_avoid2 = time_taken_A_Star_avoid2 + 4
                                    avoid_2_more = avoid_2_more + 3

                    time_taken_avoiding2V.append(time_taken_A_Star_avoid2)
                    del (time_taken_A_Star_avoid2)
                else:
                    time_taken_avoiding2V.append(0)
                    avoid_2_more = 0
                    # del(time_taken_A_Star_avoid2)
            # distance_travelled_avoiding3V=[]
            # time_taken_avoiding3V=[]

            import numpy as np

            filein = "D:/Layout_updated_2021 (1).csv"
            data = np.loadtxt(open(filein, "rb"), delimiter=",")
            # print(data)
            maze1 = np.array(data)
            maze1 = np.where(maze1 == 100, 1, maze1)
            maze1 = np.where(maze1 == -1, 1, maze1)
            maze1 = np.where(maze1 == 200, 1, maze1)
            maze1 = np.where(maze1 == 50, 0, maze1)

            counter = -1

            key = []
            for z in Zone_total:
                counter = counter + 1
                if z >= 3:
                    # val=zones_dictionary.get(a)
                    key.append(
                        next(((k, i) for (k, i) in zones_dictionary if zones_dictionary[(k, i)] == counter), None))
                    # zones_dictionary.keys()[zones_dictionary.values(counter)]
                    for i in zones_dictionary:
                        # print(i)
                        if zones_dictionary[i] == counter:
                            key.append(i)

            maze_4 = maze1
            # print(key)
            for k in key:
                maze_4[k] = 1

from tqdm.auto import tqdm

m1 = 0
m2 = 0
m1_list = []
m2_list = []
not_giving_up = 0
time_list_no_traffic_avoidance = []
time_list_Traffic_Avoidance = []

for not_giving_up in tqdm(range(1)):
    number_of_times_all_vehicles_can_be_avoided = 0
    number_of_times_its_useful = 0
    trial_list = []
    sum_total_time = 0
    distance_total = 0
    time_list_No_Avoidance = []
    distance_list_No_Avoidance = []
    time_list_Traffic_Avoidance = []
    distance_list_Traffic_Avoidance = []
    no_of_vehicles_noT = []
    no_of_vehicles_T = []
    # with tqdm(total=100, position=0, leave=True) as pbar:
    for trial in range(100):
        # Step1
        from tqdm import tqdm

        data_points = 1
        ip_1_s = []
        ip_2_f = []
        op_1_t = []
        count_data = 1
        distance_travelled_by_Native_AStar = []
        time_taken_by_Native_AStar = []
        distance_travelled_avoiding1V = []
        time_taken_avoiding1V = []
        distance_travelled_avoiding2V = []
        time_taken_avoiding2V = []
        distance_travelled_avoiding3V = []
        time_taken_avoiding3V = []
        while count_data < 2:
            count_data = count_data + 1
            # data_points=1
            for N in tqdm(range(0, data_points)):
                ip_1_s = []
                ip_2_f = []
                op_1_t = []
                n = 1
                A1_n1_path = Decentralized_multi_agent_paths(n,data,P)
                # writing number of vehicles begning their trip in each zone
                for A1 in A1_n1_path:
                    A1_n = [A1]
                    Zone_start_trip = [0] * (zone + 1)
                    Zone_finish_trip = [0] * (zone + 1)
                    # Zone_rack=[0]*(zone+1)
                    for a in A1_n:
                        temp_init = list(a[0])

                        temp_init = tuple(temp_init)
                        init = zones_dictionary.get(temp_init)

                        Zone_start_trip[init] = Zone_start_trip[init] + 1

                    # writing number of vehicles ending their trip in each zone
                    for A1 in A1_n:
                        A1_n = [A1]

                        temp_final = list(a[-1])

                        temp_final = tuple(temp_final)
                        # print(temp_final)
                        final = zones_dictionary.get(temp_final)
                        # print(final)
                        Zone_finish_trip[final] = Zone_finish_trip[final] + 1
                    # writing number of vehicles that go to a deck in a zone as intermediate point

                    # writing zone busy-ness

                    Z_n_b = Zone_business(A1_n,zones_dictionary,zone)

                    ip_1_s.append(Zone_start_trip)

                    ip_2_f.append(Zone_finish_trip)

                    # ip_3.append(Zone_rack)

                    op_1_t.append(Z_n_b)

            list_features_op_testcase = []
            list_features_op_testcase.append(ip_1_s)
            list_features_op_testcase.append(ip_2_f)
            # list_features_op.append(ip_3)
            list_features_op_testcase.append(op_1_t)

            import pickle

            with open('D:/data_for_pathplanning_test_case2.pkl',
                      'wb') as f:
                pickle.dump(list_features_op_testcase, f)
            with open('D:/start_and_end_point_test_case2.pkl',
                      'wb') as f:
                pickle.dump(A1_n1_path, f)

            import pickle

            pickle_off = open(
                "D:/data_for_pathplanning_test_case2.pkl", "rb")
            emp = pickle.load(pickle_off)

            op_1_t = emp[2][:][:]
            # print(len(op_1_t))
            # print(len(op_1_t[0]))
            arr = np.array(op_1_t)
            shape = arr.shape
            zone_traversed = np.zeros(shape)
            for x in range(0, shape[0]):
                for z in range(0, shape[1]):
                    if arr[x][z] >= 1:
                        zone_traversed[x][z] = 1
                    else:
                        zone_traversed[x][z] = 0
            # print(len(zone_traversed))
            no_of_vehicles_noT

            # o=[sum(sum(zone_traversed))]
            # distance_travelled_by_Native_AStar.append(sum(sum(zone_traversed)))
            # time_A_Star=sum(sum(zone_traversed))
            # distance_list_No_Avoidance.append(time_A_Star)
            distance_A_Star = 0
            time_A_Star = 0

            no_of_vehicles_noTraffic = 0
            # Distance Travelled
            for zone_traversed_counter in zone_traversed:
                for i in range(0, len(zone_traversed[0])):
                    if zone_traversed_counter[i] != 0:
                        if Zone_total[i] == 0:
                            distance_A_Star = distance_A_Star + zone_number_of_cells_dict[i]
                        if Zone_total[i] == 1:
                            distance_A_Star = distance_A_Star + zone_number_of_cells_dict[i]
                            no_of_vehicles_noTraffic = no_of_vehicles_noTraffic + 1
                        if Zone_total[i] == 2:
                            distance_A_Star = time_A_Star + 3
                            no_of_vehicles_noTraffic = no_of_vehicles_noTraffic + 2
                        if Zone_total[i] == 3:
                            distance_A_Star = time_A_Star + 4
                            no_of_vehicles_noTraffic = no_of_vehicles_noTraffic + 3
                        if Zone_total[i] >= 3:
                            distance_A_Star = time_A_Star + Zone_total[i] + 1
                            no_of_vehicles_noTraffic = no_of_vehicles_noTraffic + Zone_total[i]

            for zone_traversed_counter in zone_traversed:
                for i in range(0, len(zone_traversed[0])):
                    if zone_traversed_counter[i] != 0:
                        if Zone_total[i] == 1:
                            time_A_Star = time_A_Star + 2*zone_number_of_cells_dict[i]
                            no_of_vehicles_noTraffic = no_of_vehicles_noTraffic + 1
                        if Zone_total[i] == 2:
                            time_A_Star = time_A_Star + 3*zone_number_of_cells_dict[i]
                            no_of_vehicles_noTraffic = no_of_vehicles_noTraffic + 2
                        if Zone_total[i] == 3:
                            time_A_Star = time_A_Star + 4*zone_number_of_cells_dict[i]
                            no_of_vehicles_noTraffic = no_of_vehicles_noTraffic + 3
                        if Zone_total[i] >= 3:
                            time_A_Star = time_A_Star + Zone_total[i] *zone_number_of_cells_dict[i]+ 1
                            no_of_vehicles_noTraffic = no_of_vehicles_noTraffic + Zone_total[i]

            time_taken_by_Native_AStar.append(time_A_Star)
            time_list_no_traffic_avoidance.append(time_A_Star)
            no_of_vehicles_noT.append(no_of_vehicles_noTraffic)
            distance_travelled_by_Native_AStar.append(distance_A_Star)

            counter = -1
            time_A_Star = 0

            key = []

            for z in Zone_total:
                counter = counter + 1
                if z >= 1:
                    # val=zones_dictionary.get(a)
                    key.append(
                        next(((k, i) for (k, i) in zones_dictionary if zones_dictionary[(k, i)] == counter), None))
                    # zones_dictionary.keys()[zones_dictionary.values(counter)]
                    for i in zones_dictionary:
                        # print(i)
                        if zones_dictionary[i] == counter:
                            key.append(i)

            maze_2 = maze1
            # print(key)
            for k in key:
                maze_2[k] = 1

            from tqdm import tqdm
            #from google.colab import files
            import random
            import pandas as pd
            import csv
            import json

            # Start and end positions
            # More specifically - start , shelf, shelf,dock
            init = []
            final = []
            # print(A1_n1_path)
            for A1 in A1_n1_path:
                A1_n = [A1]
                # Zone_rack=[0]*(zone+1)
                for a in A1_n:
                    # print(a)
                    # print(a[0])
                    init.append(a[0])
                    final.append(a[-1])
            # def data_generator_for_nn(data_points):
            data_points = 1
            ip_1_avoid2 = []
            ip_2_avoid2 = []
            op_1_avoid2 = []
            for N in range(0, data_points):
                # print(n)
                # n = random. randint(10,15) #randomly generated number between 2 to 20
                n = 1
                A1_n1_avoid2 = []
                test_planner = P.PathPlanner(maze_2,True)
                # print(init)
                start = init[0]
                # print(type(start))
                start = list(start)
                temp = start
                start[1] = temp[0]
                start[0] = temp[1]
                end = final[0]
                temp1 = end
                end = list(end)
                end[1] = temp1[0]
                end[0] = temp1[1]
                a1 = test_planner.a_star(start, end)
                # print(type(a1))

                start = init[1]
                start = list(start)
                temp = start
                start[1] = temp[0]
                start[0] = temp[1]
                end = final[1]
                temp1 = end
                end = list(end)
                end[1] = temp1[0]
                end[0] = temp1[1]
                a2 = test_planner.a_star(start, end)
                A1_n1_avoid2.append(a1)
                A1_n1_avoid2.append(a2)
                # print(A1_n1_avoid2)
                # print(len(A1_n1_avoid2))
                # print(len(A1_n1_avoid2[0]))
                check = 1
                for A_check_empty in A1_n1_avoid2:
                    if A_check_empty == []:
                        check = 0
                    else:
                        check = check * 1
                if (check == 1):
                    if ((A1_n1_avoid2[0]) == []) and (len(A1_n1_avoid2[1] == 0)):
                        # writing number of vehicles begning their trip in each zone
                        for A1 in A1_n1_avoid2:
                            # print(A1)
                            A1_n = [A1]
                            Zone_start_trip = [0] * (zone + 1)
                            Zone_finish_trip = [0] * (zone + 1)
                            # Zone_rack=[0]*(zone+1)
                            for a in A1_n1_avoid2:
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
                            for A1 in A1_n1_avoid2:
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

                            # writing zone busy-ness

                            Z_n = Zone_business(A1_n1_avoid2,zones_dictionary,zone)

                            ip_1_avoid2.append(Zone_start_trip)

                            ip_2_avoid2.append(Zone_finish_trip)

                            # ip_3.append(Zone_rack)

                            op_1_avoid2.append(Z_n)

            if ((A1_n1_avoid2[0] != []) and (A1_n1_avoid2[1] != [])):
                list_features_op_avoid2 = []
                list_features_op_avoid2.append(ip_1_avoid2)
                list_features_op_avoid2.append(ip_2_avoid2)
                # list_features_op.append(ip_3)
                list_features_op_avoid2.append(op_1_avoid2)
            if ((A1_n1_avoid2[0] == []) or (A1_n1_avoid2[1] == [])):
                print("no path found")
                distance_travelled_avoiding1V.append(0)
                time_taken_avoiding1V.append(0)
            else:
                arr = np.array(op_1_avoid2)
                shape = arr.shape
                zone_traversed_1 = np.zeros(shape)
                for x in range(0, shape[0]):
                    for z in range(0, shape[1]):
                        if arr[x][z] >= 1:
                            zone_traversed_1[x][z] = 1
                        else:
                            zone_traversed_1[x][z] = 0

                # print(zone_traversed_1.shape)
                time_taken_A_Star_avoid2 = sum(zone_traversed_1)
                distance_travelled_avoiding1V.append(time_taken_A_Star_avoid2)
                # print(time_taken_A_Star_avoid2)

                for zone_traversed_1 in op_1_avoid2:
                    for i in range(0, len(zone_traversed[0])):
                        if zone_traversed_counter[i] != 0:
                            if Zone_total[i] == 1:
                                time_taken_A_Star_avoid2 = time_taken_A_Star_avoid2 + 2
                            if Zone_total[i] == 2:
                                time_taken_A_Star_avoid2 = time_taken_A_Star_avoid2 + 3
                            if Zone_total[i] == 3:
                                time_taken_A_Star_avoid2 = time_taken_A_Star_avoid2 + 4

                time_taken_avoiding1V.append(time_taken_A_Star_avoid2)

                del (time_taken_A_Star_avoid2)

            import numpy as np

            filein = "D:/Layout_updated_2021 (1).csv"
            data = np.loadtxt(open(filein, "rb"), delimiter=",")
            # print(data)
            maze1 = np.array(data)
            maze1 = np.where(maze1 == 100, 1, maze1)
            maze1 = np.where(maze1 == -1, 1, maze1)
            maze1 = np.where(maze1 == 200, 1, maze1)
            maze1 = np.where(maze1 == 50, 0, maze1)

            Zone_total = [0] * (zone + 1)
            trip = -1
            for re in result_P:
                # print(re)
                # print(type(re))
                # print(len(re))
                c = -1
                trip = trip + 1
                if (trip / 2) == 0:
                    Zone_temp = [0] * (zone + 1)
                    for r in re:
                        c = c + 1
                        # print(r)
                        if r == 1:
                            Zone_total[c] = Zone_total[c] + 1
                            Zone_temp[c] = 1
                if (trip / 2) != 0:
                    for r in re:
                        c = c + 1
                        if r == 1:
                            if (Zone_temp[c] != 1):
                                Zone_total[c] = Zone_total[c] + 1

            key = []
            counter = -1
            for z in Zone_total:
                counter = counter + 1
                if z >= 2:
                    # val=zones_dictionary.get(a)
                    key.append(
                        next(((k, i) for (k, i) in zones_dictionary if zones_dictionary[(k, i)] == counter), None))
                    # zones_dictionary.keys()[zones_dictionary.values(counter)]
                    for i in zones_dictionary:
                        # print(i)
                        if zones_dictionary[i] == counter:
                            key.append(i)

            maze_3 = maze1
            # print(key)
            for k in key:
                maze_3[k] = 1

            from tqdm import tqdm
            #from google.colab import files
            import random
            import pandas as pd
            import csv
            import json

            # Start and end positions
            # More specifically - start , shelf, shelf,dock
            init = []
            final = []
            # print(A1_n1_path)
            for A1 in A1_n1_path:
                A1_n = [A1]
                # Zone_rack=[0]*(zone+1)
                for a in A1_n:
                    # print(a)
                    # print(a[0])
                    init.append(a[0])
                    final.append(a[-1])
            # def data_generator_for_nn(data_points):
            data_points = 1
            ip_1_avoid2 = []
            ip_2_avoid2 = []
            op_1_avoid2 = []
            for N in range(0, data_points):
                # print(n)
                # n = random. randint(10,15) #randomly generated number between 2 to 20
                n = 1
                A1_n1_avoid2 = []
                test_planner = P.PathPlanner(maze_3,True)
                # print(init)
                start = init[0]
                # print(type(start))
                start = list(start)
                temp = start
                start[1] = temp[0]
                start[0] = temp[1]
                end = final[0]
                temp1 = end
                end = list(end)
                end[1] = temp1[0]
                end[0] = temp1[1]
                a1 = test_planner.a_star(start, end)
                # print(type(a1))

                start = init[1]
                start = list(start)
                temp = start
                start[1] = temp[0]
                start[0] = temp[1]
                end = final[1]
                temp1 = end
                end = list(end)
                end[1] = temp1[0]
                end[0] = temp1[1]
                a2 = test_planner.a_star(start, end)
                A1_n1_avoid2.append(a1)
                A1_n1_avoid2.append(a2)
                # print(A1_n1_avoid2)
                # print(len(A1_n1_avoid2))
                check = 1
                for A_check_empty in A1_n1_avoid2:
                    if A_check_empty == []:
                        check = 0
                    else:
                        check = check * 1
                if ((A1_n1_avoid2[0] != -1) and (A1_n1_avoid2[1] != -1)):
                    if (check == 1):
                        if ((A1_n1_avoid2[0] != []) and (A1_n1_avoid2[1] != [])):
                            # writing number of vehicles begning their trip in each zone
                            for A1 in A1_n1_avoid2:
                                # print(A1)
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

                                # writing zone busy-ness

                                Z_n = Zone_business(A1_n1_avoid2,zones_dictionary,zone)

                                ip_1_avoid2.append(Zone_start_trip)

                                ip_2_avoid2.append(Zone_finish_trip)

                                # ip_3.append(Zone_rack)

                                op_1_avoid2.append(Z_n)

            if (A1_n1_avoid2[0] != -1 and A1_n1_avoid2[0] != -1):
                list_features_op_avoid2 = []
                list_features_op_avoid2.append(ip_1_avoid2)
                list_features_op_avoid2.append(ip_2_avoid2)
                # list_features_op.append(ip_3)
                list_features_op_avoid2.append(op_1_avoid2)
            if ((A1_n1_avoid2[0] == -1) or (A1_n1_avoid2[1] == -1)):
                print("no path found")
                distance_travelled_avoiding2V.append(0)
                time_taken_avoiding2V.append(0)
            else:
                arr = np.array(op_1_avoid2)
                shape = arr.shape
                zone_traversed_1 = np.zeros(shape)
                for x in range(0, shape[0]):
                    for z in range(0, shape[1]):
                        if arr[x][z] >= 1:
                            zone_traversed_1[x][z] = 1
                        else:
                            zone_traversed_1[x][z] = 0

                if (zone_traversed_1 != []):
                    avoid_2_more = 0
                    time_taken_A_Star_avoid2 = sum(sum(zone_traversed_1))
                    distance_travelled_avoiding2V.append(time_taken_A_Star_avoid2)
                    # print(time_taken_A_Star_avoid2)
                    for zone_traversed_1 in op_1_avoid2:
                        for i in range(0, len(zone_traversed[0])):
                            if zone_traversed_counter[i] != 0:
                                if Zone_total[i] == 1:
                                    time_taken_A_Star_avoid2 = time_taken_A_Star_avoid2 + 2
                                    avoid_2_more = avoid_2_more + 1
                                if Zone_total[i] == 2:
                                    time_taken_A_Star_avoid2 = time_taken_A_Star_avoid2 + 3
                                    avoid_2_more = avoid_2_more + 2
                                if Zone_total[i] == 3:
                                    time_taken_A_Star_avoid2 = time_taken_A_Star_avoid2 + 4
                                    avoid_2_more = avoid_2_more + 3

                    time_taken_avoiding2V.append(time_taken_A_Star_avoid2)
                    del (time_taken_A_Star_avoid2)
                else:
                    time_taken_avoiding2V.append(0)
                    avoid_2_more = 0
                    # del(time_taken_A_Star_avoid2)
            # distance_travelled_avoiding3V=[]
            # time_taken_avoiding3V=[]

            import numpy as np

            filein = "D:/Layout_updated_2021 (1).csv"
            data = np.loadtxt(open(filein, "rb"), delimiter=",")
            # print(data)
            maze1 = np.array(data)
            maze1 = np.where(maze1 == 100, 1, maze1)
            maze1 = np.where(maze1 == -1, 1, maze1)
            maze1 = np.where(maze1 == 200, 1, maze1)
            maze1 = np.where(maze1 == 50, 0, maze1)

            counter = -1

            key = []
            for z in Zone_total:
                counter = counter + 1
                if z >= 3:
                    # val=zones_dictionary.get(a)
                    key.append(
                        next(((k, i) for (k, i) in zones_dictionary if zones_dictionary[(k, i)] == counter), None))
                    # zones_dictionary.keys()[zones_dictionary.values(counter)]
                    for i in zones_dictionary:
                        # print(i)
                        if zones_dictionary[i] == counter:
                            key.append(i)

            maze_4 = maze1
            # print(key)
            for k in key:
                maze_4[k] = 1

            from tqdm import tqdm
            #from google.colab import files
            import random
            import pandas as pd
            import csv
            import json

            # Start and end positions
            # More specifically - start , shelf, shelf,dock
            init = []
            final = []
            # print(A1_n1_path)
            for A1 in A1_n1_path:
                A1_n = [A1]
                # Zone_rack=[0]*(zone+1)
                for a in A1_n:
                    # print(a)
                    # print(a[0])
                    init.append(a[0])
                    final.append(a[-1])
            # def data_generator_for_nn(data_points):
            data_points = 1
            ip_1_avoid2 = []
            ip_2_avoid2 = []
            op_1_avoid2 = []
            for N in range(0, data_points):
                # print(n)
                # n = random. randint(10,15) #randomly generated number between 2 to 20
                n = 1
                A1_n1_avoid2 = []
                test_planner1 = P.PathPlanner(maze_4, True)
                # print(init)
                start = init[0]
                # print(type(start))
                start = list(start)
                temp = start
                start[1] = temp[0]
                start[0] = temp[1]
                end = final[0]
                temp1 = end
                end = list(end)
                end[1] = temp1[0]
                end[0] = temp1[1]
                a1 = test_planner1.a_star(start, end)
                # print(type(a1))

                start = init[1]
                start = list(start)
                temp = start
                start[1] = temp[0]
                start[0] = temp[1]
                end = final[1]
                temp1 = end
                end = list(end)
                end[1] = temp1[0]
                end[0] = temp1[1]
                a2 = test_planner1.a_star(start, end)
                A1_n1_avoid2.append(a1)
                A1_n1_avoid2.append(a2)
                # print(A1_n1_avoid2)
                # print(len(A1_n1_avoid2))
                check = 1
                for A_check_empty in A1_n1_avoid2:
                    if A_check_empty == []:
                        check = 0
                    else:
                        check = check * 1
                if (check == 1):
                    if ((len(A1_n1_avoid2[0]) != 0) and (len(A1_n1_avoid2[1]) != 0)):
                        # writing number of vehicles begning their trip in each zone
                        for A1 in A1_n1_avoid2:
                            # print(A1)
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
                            for A1 in A1_n1_avoid2:
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

                            # writing zone busy-ness

                            Z_n = Zone_business(A1_n1_avoid2,zones_dictionary,zone)

                            ip_1_avoid2.append(Zone_start_trip)

                            ip_2_avoid2.append(Zone_finish_trip)

                            # ip_3.append(Zone_rack)

                            op_1_avoid2.append(Z_n)

            if ((len(A1_n1_avoid2[0]) != 0) and (len(A1_n1_avoid2[1]) != 0)):
                list_features_op_avoid2 = []
                list_features_op_avoid2.append(ip_1_avoid2)
                list_features_op_avoid2.append(ip_2_avoid2)
                # list_features_op.append(ip_3)
                list_features_op_avoid2.append(op_1_avoid2)
            if ((len(A1_n1_avoid2[0]) == 0) or (len(A1_n1_avoid2[1]) == 0)):
                print("no path found")
                distance_travelled_avoiding2V.append(0)
                time_taken_avoiding2V.append(0)
            else:
                arr = np.array(op_1_avoid2)
                shape = arr.shape
                zone_traversed_1 = np.zeros(shape)
                for x in range(0, shape[0]):
                    for z in range(0, shape[1]):
                        if arr[x][z] >= 1:
                            zone_traversed_1[x][z] = 1
                        else:
                            zone_traversed_1[x][z] = 0

                time_taken_A_Star_avoid2 = sum(sum(zone_traversed_1))
                distance_travelled_avoiding3V.append(time_taken_A_Star_avoid2)
                # print(time_taken_A_Star_avoid2)

                avoid_3_or_more = 0

                for zone_traversed_1 in op_1_avoid2:
                    for i in range(0, len(zone_traversed[0])):
                        if zone_traversed_counter[i] != 0:
                            if Zone_total[i] == 1:
                                time_taken_A_Star_avoid2 = time_taken_A_Star_avoid2 + 2
                                avoid_3_or_more = avoid_3_or_more + 1
                            if Zone_total[i] == 2:
                                time_taken_A_Star_avoid2 = time_taken_A_Star_avoid2 + 3
                                avoid_3_or_more = avoid_3_or_more + 2
                            if Zone_total[i] == 3:
                                time_taken_A_Star_avoid2 = time_taken_A_Star_avoid2 + 3
                                avoid_3_or_more = avoid_3_or_more + 3

                time_taken_avoiding3V.append(time_taken_A_Star_avoid2)

                # time_list_no_traffic_avoidance.append(time_taken_by_Native_AStar[0])
                # distance_list_No_Avoidance.append(distance_travelled_by_Native_AStar[0])
                print(distance_travelled_by_Native_AStar)
                if (time_taken_by_Native_AStar > time_taken_avoiding3V) and (time_taken_avoiding3V != 0) and (
                        time_taken_avoiding3V != []):
                    # if (time_taken_avoiding2V >= time_taken_avoiding3V):
                    number_of_times_its_useful = number_of_times_its_useful + 1
                    sum_total_time = sum_total_time + (time_taken_by_Native_AStar[0] - time_taken_avoiding3V[0])
                    distance_total = distance_total + (
                                distance_travelled_avoiding3V[0] - distance_travelled_by_Native_AStar[0])
                    time_list_No_Avoidance.append(time_taken_by_Native_AStar[0])
                    distance_list_No_Avoidance.append(distance_travelled_by_Native_AStar[0])
                    time_list_Traffic_Avoidance.append(time_taken_avoiding3V[0])
                    distance_list_Traffic_Avoidance.append(distance_travelled_avoiding3V)
                    no_of_vehicles_T.append(avoid_3_or_more)

                else:
                    if ((time_taken_by_Native_AStar > time_taken_avoiding2V) and (time_taken_avoiding2V != 0) and (
                            time_taken_avoiding2V != [])):
                        number_of_times_its_useful = number_of_times_its_useful + 1
                        sum_total_time = sum_total_time + (time_taken_by_Native_AStar[0] - time_taken_avoiding2V[0])
                        print(distance_travelled_by_Native_AStar)
                        distance_total = distance_total + (
                                    distance_travelled_avoiding3V[0] - distance_travelled_by_Native_AStar[0])
                        distance_total = distance_total + (
                                    distance_travelled_avoiding3V[0] - distance_travelled_by_Native_AStar[0])
                        # time_list_No_Avoidance.append(time_taken_by_Native_AStar[0])
                        # distance_list_No_Avoidance.append(distance_travelled_by_Native_AStar[0])
                        time_list_Traffic_Avoidance.append(time_taken_avoiding2V)
                        distance_list_Traffic_Avoidance.append(distance_travelled_avoiding2V)
                        no_of_vehicles_T.append(avoid_2_more)
                    else:
                        # time_list_No_Avoidance.append(time_taken_by_Native_AStar[0])
                        # distance_list_No_Avoidance.append(distance_travelled_by_Native_AStar[0])
                        if ((time_taken_avoiding3V[0] > time_taken_avoiding2V) and (time_taken_avoiding2V != 0) and (
                                time_taken_avoiding2V != [])):
                            time_list_Traffic_Avoidance.append(time_taken_avoiding2V)
                            distance_list_Traffic_Avoidance.append(distance_travelled_avoiding2V)
                            no_of_vehicles_T.append(avoid_2_more)
                        else:
                            if ((time_taken_avoiding3V != 0) and (time_taken_avoiding3V != [])):
                                time_list_Traffic_Avoidance.append(time_taken_avoiding3V)
                                distance_list_Traffic_Avoidance.append(distance_travelled_avoiding3V)
                                no_of_vehicles_T.append(avoid_3_or_more)
                            else:
                                time_list_Traffic_Avoidance.append(0)
                                distance_list_Traffic_Avoidance.append(0)
                                no_of_vehicles_T.append(0)

    # if (time_taken_avoiding1V != [0]):
    # number_of_times_all_vehicles_can_be_avoided = number_of_times_all_vehicles_can_be_avoided +1
    # trial_list.append(trial)

    print(number_of_times_its_useful)
    print(trial_list)

    from statistics import mean

    # print(mean(time_list_no_traffic_avoidance))
    # m1=(mean(time_list_no_traffic_avoidance))
    m1_list.append(m1)
    # print(mean(distance_list_No_Avoidance))
    t_l = []
    # print((time_list_Traffic_Avoidance))
    for t_l_t_a in time_list_Traffic_Avoidance:
        if (isinstance(t_l_t_a, int)):
            t_l.append(float(t_l_t_a))
        if (isinstance(t_l_t_a, float)):
            t_l.append(t_l_t_a)
        if (isinstance(t_l_t_a, list)):
            for t in t_l_t_a:
                t_l.append(t)

    no_t = []
    t_2 = []
    counter = 0
    for a in t_l:
        if a != 0:
            t_2.append(a)
            no_t.append(time_list_no_traffic_avoidance[counter])
        counter = counter + 1

    print(mean(no_t))
    m1 = (mean(no_t))
    print(mean(t_2))
    m2 = (mean(t_2))
    m2_list.append(m2)
    not_giving_up = not_giving_up + 1
    print(not_giving_up)
    if (m1 > m2):
        break

# Importing library
import csv

np.savetxt('D:/array_t_no_traffic_6_27_1.csv', no_t, delimiter=',',
           fmt='%d')
np.savetxt('D:/array_t_traffic_avoid_6_27_1.csv', t_2, delimiter=',',
           fmt='%d')
np.savetxt('D:/array_no_traffic_avoidance_6_27_1.csv',
           distance_list_No_Avoidance, delimiter=',', fmt='%d')
np.savetxt('D:/array_traffic_avoidance_6_27_1.csv',
           distance_list_Traffic_Avoidance, delimiter=',', fmt='%d')
np.savetxt('D:/array_traffic_num_vehicles_avoided_6_27_1.csv',
           no_of_vehicles_T, delimiter=',', fmt='%d')
np.savetxt('D:/array_no_traffic_num_vehicles_avoided_6_27_1.csv',
           no_of_vehicles_noT, delimiter=',', fmt='%d')


