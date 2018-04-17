import heapq
import sys

class Person:
        def __init__(self):
                self.x_pos = None
                self.y_pos = None
                self.map = Graph()
        def set_position(self, x, y):
                self.x_pos = float(x)
                self.y_pos = float(y)
        def closest_node(self):
                lowest = -1
                name = None
                for io in self.map.graph_nodes:
                        node = self.map.NodeObjects[io]
                        print(str(node.x_pos)+" "+str(self.x_pos)+" "+str(node.y_pos)+" "+str(self.y_pos))
                        manhat = abs(node.x_pos - self.x_pos) + abs(node.y_pos - self.y_pos)
                        if lowest == -1 or lowest > manhat:
                                lowest = manhat
                                name = io
                return name
        def get_path(self, dest):
                #position = 2000
                position = self.closest_node()
                route = self.map.shortest_path(position, dest)
                #print("route: {}".format(str(route)))
                route.append(position)
                route.reverse()
                return route
        def get_points(self, dest):
                path = self.get_path(dest)
                print("path: {}".format(str(path)))
                x_s = []
                y_s = []
                for a in path:
                        node = self.map.NodeObjects[a]
                        x_s.append(node.x_pos)
                        y_s.append(node.y_pos)
                return x_s, y_s
class Node:
        def __init__(self, NodeID):
                self.NodeID = NodeID
                self.x_pos = None
                self.y_pos = None
                self.IsNode = False
        def configNode(self, x_pos, y_pos, IsNode):
                self.x_pos = x_pos
                self.y_pos = y_pos
                self.IsNode = IsNode
        def __str__(self):
                return str(self.x_pos) + " " + str(self.y_pos) + " " + str(self.IsNode)
class Graph:

    def __init__(self):
		self.vertices = {}
        WinlabMap={
        2000:{2001:2.1,2012:15.2},
        2001:{2000:2.1,2002:4.1},
        2002:{2001:4.1,2003:5.6,2008:4.2},
        2003:{2002:5.6,2004:5.6,2011:4.2},
        2004:{2003:5.6,2005:4.2},
        2005:{2004:4.2,2006:4.2},
        2006:{2007:5.7,2010:5.6,2005:4.2},
        2007:{2006:5.7},
        2008:{2002:4.2,2009:4.2},
        2009:{2008:4.2,2010:5.6},
        2010:{2009:5.6,2006:5.6,2011:4.2},
        2011:{2003:4.2,2010:4.2},
        2012:{2000:15.2,2013:2.1},
        2013:{2012:2.1},
        2014:{2004:4.0,2015:2.4},
        2015:{2014:2.4,2016:2.8},
        2016:{2015:2.8}
            }
        print("inside constructor of Graph class")
        self.graph_nodes=[2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016]
        for vertice in self.graph_nodes:
            self.add_vertex(vertice,WinlabMap[vertice])

        Winlab_Nodes={2000:[-1.1,-2.7,True],2001:[1.0,-2.7,True],2002:[1.0,1.4,True],2003:[6.6,1.4,False],2004:[12.1,1.4,True],
                2005:[12.1,5.7,False],2006:[12.1,9.9,True],2007:[15.6,9.9,False],2008:[1.0,5.7,False],2009:[1.0,9.9,True],2010:[6.6,9.9,False],2011:[6.6,5.7,False],
                2012:[-16.3,-2.7,False],2013:[-16.3,-0.6,False],2014:[15.9,1.4,False],2015:[15.9,-1.4,False],2016:[13.3,-1.7,False]}
        self.NodeObjects = {}
        for name in self.graph_nodes:
                self.NodeObjects[name] = Node(name)
                self.NodeObjects[name].configNode(Winlab_Nodes[name][0], Winlab_Nodes[name][1], Winlab_Nodes[name][2])

        print('NodeObjects: {}'.format(str(self.NodeObjects)))

    def add_vertex(self, name, edges):
        self.vertices[name] = edges

    def shortest_path(self, start, finish):
        distances = {} # Distance from start to node
        previous = {} # Previous node in optimal path from source
        nodes = [] # Priority queue of all nodes in Graph
        for vertex in self.vertices:
            if vertex == start: # Set root node as distance of 0
                distances[vertex] = 0
                heapq.heappush(nodes, [0, vertex])
            else:
                distances[vertex] = sys.maxsize
                heapq.heappush(nodes, [sys.maxsize, vertex])
            previous[vertex] = None

        while nodes:
			smallest = heapq.heappop(nodes)[1]
            if smallest == finish:
                path = []
                while previous[smallest]:
                    path.append(smallest)
                    smallest = previous[smallest]
                return path
            if distances[smallest] == sys.maxsize:
                break

            for neighbor in self.vertices[smallest]:
                alt = distances[smallest] + self.vertices[smallest][neighbor]
                if alt < distances[neighbor]:
                    distances[neighbor] = alt
                    previous[neighbor] = smallest
                    for n in nodes:
                        if n[1] == neighbor:
                            n[0] = alt
                            break
                    heapq.heapify(nodes)
        return distances


    def __str__(self):
        return str(self.vertices)
