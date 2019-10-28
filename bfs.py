from collections import deque

graph = {}

graph['START'] = {'A': 6, 'B': 2}
graph['A'] = {'FIN': 1}
graph['B'] = {'A': 3, 'FIN': 5}
graph['FIN'] = {}


