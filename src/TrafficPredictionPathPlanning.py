import numpy as np
from matplotlib import pyplot
import matplotlib as mpl
from numpy import array, where
from random import choice
def read_map(filein):
    #filein = "D:/Layout_updated_2021 (1).csv"
    data = np.loadtxt(open(filein, "rb"), delimiter=",")
    print(data)
    fig = pyplot.figure(2)

    cmap2 = mpl.colors.LinearSegmentedColormap.from_list('my_colormap',
                                           ['orange','blue','green','white','red'],
                                           256)

    img2 = pyplot.imshow(data,interpolation='nearest',
                    cmap = cmap2,
                    origin='lower')

    #pyplot.colorbar(img2,cmap=cmap2)

    fig.savefig("D:/Warehouse_layout.png")

    maze1 = np.array(data)
    maze1 = np.where(maze1 == 100, 1, maze1)
    maze1 = np.where(maze1 == -1, 1, maze1)
    maze1 = np.where(maze1 == 200, 1, maze1)
    maze1 = np.where(maze1 == 50, 0, maze1)

    fig = pyplot.figure(2)

    cmap2 = mpl.colors.LinearSegmentedColormap.from_list('my_colormap',
                                                     ['orange', 'blue', 'green'],
                                                     256)

    img2 = pyplot.imshow(maze1, interpolation='nearest',
                     cmap=cmap2,
                     origin='lower')

    #pyplot.colorbar(img2, cmap=cmap2)

    fig.savefig("D:/Warehouse_maze_seen_by_ASTAR.png")

    size_data = np.size(data)
    shape_data = np.shape(data)
    '''print(size_data)
    print(shape_data)
    print(data.shape)'''


    def countX(lst, x):
        count = 0
        for el in lst:
            for ele in el:
                if (ele == x):
                    count = count + 1
        return count


    print('{} has occurred {} times'.format(50, countX(data, 50)))
    print('{} has occurred {} times'.format(100, countX(data, 100)))
    print('{} has occurred {} times'.format(200, countX(data, 200)))
    print('{} has occurred {} times'.format(0, countX(data, 0)))
    print('{} has occurred {} times'.format(-1, countX(data, -1)))

    zones_dictionary = {}
    zone_number_of_cells_dict = []

    # New zoning
    # Involves labeling available free paths as zones
    # It can be noticed that there are vertical and horizontal free paths which make up the zones
    # If a zone is enterd, it can be left only through the intersections
    zone = 0
    zone1 = 1
    zone2 = 1
    c50 = 0
    c0 = 0
    maze = np.array(data)
    else_counter = 0
    for row in range(0, shape_data[0] - 1):
        for colm in range(0, shape_data[1] - 1):
            if maze[row, colm] == 50:
                else_counter = 0
                zone = zone + 1
                # zone1=zone1+1
                zones_dictionary[(row, colm)] = zone
                zone_number_of_cells_dict.append(1)
                zone = zone + 1
                c50 = c50 + 1
            elif maze[row, colm] == 0 and maze[row, colm + 1] != 200 and maze[row, colm + 1] != 100 and maze[
                row, colm + 1] != -1:
                # print(row,colm)
                zones_dictionary[(row, colm)] = zone
                if else_counter == 1:
                    zone_number_of_cells_dict.append(else_counter)
                else:
                    del zone_number_of_cells_dict[-1]
                    zone_number_of_cells_dict.append(else_counter)
                c0 = c0 + 1
            else:
                else_counter = else_counter + 1
                if else_counter == 22:
                    zone = zone - 1
                    zone_number_of_cells_dict = zone_number_of_cells_dict[:-1]
                # zones_dictionary[(row,colm)]=0

    for colm in range(0, shape_data[1] - 1):
        for row in range(0, shape_data[0] - 1):
            if maze[row, colm] == 50:
                if else_counter >= 33:
                    zone = zone - 1
                    del zone_number_of_cells_dict[-1]
                else_counter = 0
                zone = zone + 1
                c50 = c50 + 1
            elif maze[row, colm] == 0 and maze[row + 1, colm] != 200 and maze[row + 1, colm] != 100 and maze[
                row + 1, colm] != -1:
                # print(row,colm)
                zones_dictionary[(row, colm)] = zone
                if else_counter == 1:
                    zone_number_of_cells_dict.append(else_counter)
                else:
                    del zone_number_of_cells_dict[-1]
                    zone_number_of_cells_dict.append(else_counter)

                # print(row,colm)
                # print(row,colm)
                c0 = c0 + 1
            else:
                # continue
                else_counter = else_counter + 1
                # 33

    # print(zones_dictionary)
    # zones_dictionary = {key:val for key, val in zones_dictionary.items() if val != 0}
    # print(zones_dictionary)
    counter = 0
    for i in zones_dictionary:
        # print(i)
        if zones_dictionary[i] == 3:
            print(i)
            counter = counter + 1
    print(counter)
    # Should be 1238
    # print(0)
    # print(c0)
    # print(50)
    # print(c50)
    # print(c+co)
    print(zone)


    counter=[0]*zone
    for j in range(0,zone):
      for i in zones_dictionary:
        #print(i)
        if zones_dictionary[i]==j:
            counter[j]=counter[j]+1

    print(sum(counter))
    print(zone_number_of_cells_dict)

    zone_number_of_cells_dict=np.zeros(zone)
    for v in zones_dictionary.values():
            print(v)
            for c in range(0,zone):
                    if v==c:
                        zone_number_of_cells_dict[c]=zone_number_of_cells_dict[c]+1
    print(len(zone_number_of_cells_dict))
    for i in range(0,len(zone_number_of_cells_dict)):
        print(zone_number_of_cells_dict[i])
    return zone,zones_dictionary, data, maze1,zone_number_of_cells_dict


# Number of agents = 4,6,8,10
# A zone can be classified as busy / not busy or on a scale of business
# Which method we pick will decide if we need classification or regression
# Classification seems like a good option
# This is to measure business
import numpy
from numpy import array, where
from random import choice
import random
#import PathPlanner


def Decentralized_multi_agent_paths(n, data,PathPlanner, k=None,
                                    maze_passed=None):  # Added K for consistency with the random generator. Like seeding
    # n=4
    A = []

    for i in range(1, n + 1):
        if maze_passed == None:
            maze1 = np.array(data)
            maze1 = np.where(maze1 == 100, 1, maze1)
            maze1 = np.where(maze1 == -1, 1, maze1)
            maze1 = np.where(maze1 == 200, 1, maze1)
            maze1 = np.where(maze1 == 50, 0, maze1)
        if maze_passed != None:
            maze1 = maze_passed

        init_position = random.choice(array(where(data == 0)).T)
        shelf_to_go = random.choice(array(where(data == 100)).T)
        Final_dock = random.choice(array(where(data == 200)).T)

        if data[shelf_to_go[0] - 1, shelf_to_go[1]] == 0:
            shelf_to_go[0] = shelf_to_go[0] - 1
        else:
            shelf_to_go[0] = shelf_to_go[0] + 1
        end1 = tuple(shelf_to_go)
        start2 = end1
        if data[Final_dock[0] - 1, Final_dock[1]] == 0:
            Final_dock[0] = Final_dock[0] - 1
        else:
            Final_dock[0] = Final_dock[0] + 1

        I = tuple(init_position)
        temp = init_position[0]
        init_position[0] = init_position[1]
        init_position[1] = temp

        S = tuple(shelf_to_go)
        temp = shelf_to_go[0]
        shelf_to_go[0] = shelf_to_go[1]
        shelf_to_go[1] = temp

        F = tuple(Final_dock)
        temp = Final_dock[0]
        Final_dock[0] = Final_dock[1]
        Final_dock[1] = temp

        start1 = tuple(init_position)
        end1 = tuple(shelf_to_go)
        start2 = tuple(shelf_to_go)
        end2 = tuple(Final_dock)

        test_planner = PathPlanner.PathPlanner(maze1, True)
        a1 = test_planner.a_star(start1, end1)
        a2 = test_planner.a_star(start2, end2)
        # print(a1)

        a1 = list(a1)
        a1.insert(0, I)
        # for i in range(1,20): #Picking up from the shelf takes 20 time stamps
        # a1.insert(len(a1),S)

        a2 = list(a2)
        # for i in range(1,20): #Docking takes 20 time stamps
        a1.insert(0, S)
        # a2.insert(len(a2),F)
        # a1.extend(a2)
        A.append(a1)
        A.append(a2)

    return A

# Measuring zone business
#Number of agents in a zone
#Number of agents in a zone at a time
#Number of agents that want to cross a zone at a time
def Zone_business (A1,zones_dictionary,zone):
      #print(zone)
      No_of_agents_in_Zone=[0] * (zone+1)
      for A in A1:
          #print(A)
          for a in A:
              a=list(a)
              temp_a=list(a)
              #print(temp_a)
              #temp=temp_a[0]
              #temp_a[0]=temp_a[1]
              #temp_a[1]=temp
              #print(temp_a)
              #temp_a[0]=temp_a[0]
              #temp_a[1]=temp_a[1]
              temp_a=tuple(temp_a)
              #temp_a=temp_a
              #print(temp_a)
              val=zones_dictionary.get(temp_a)
              #val=zones_dictionary.get(a)
              #print(val)
              No_of_agents_in_Zone[val]=No_of_agents_in_Zone[val]+1



      #print(No_of_agents_in_Zone)
      return No_of_agents_in_Zone

