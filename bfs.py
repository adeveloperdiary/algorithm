from collections import deque

graph = {}

graph['START'] = {'A': 6, 'B': 2}
graph['A'] = {'END': 1}
graph['B'] = {'A': 3, 'END': 5}
graph['END'] = {}

'''
graph['START'] = {'A': 10}
graph['A'] = {'B': 20}
graph['B'] = {'END': 30, 'C': 1}
graph['C'] = {'A': 1}
graph['END'] = {}

graph['START'] = {'A': 5, 'C': 2}
graph['A'] = {'B': 4, 'D': 2}
graph['B'] = {'END': 3, 'D': 6}
graph['C'] = {'A': 8, 'D': 7}
graph['D'] = {'END': 1}
graph['END'] = {}
'''

costs = {}

parents = {}
processed = []


def find_lowest_cost():
    selected = None

    for node in costs:
        if node not in processed:
            if selected is None:
                selected = node
            else:
                if costs[node] < costs[selected]:
                    selected = node

    return selected


def calculate_path(start, end):
    for key in graph:
        if key != start:
            costs[key] = float('inf')
            parents[key] = None

    processed.append(start)

    for key in graph[start]:
        costs[key] = graph[start][key]
        parents[key] = start

    node = find_lowest_cost()

    while node is not None:
        outputs = graph[node]
        processed.append(node)
        if outputs != {}:
            start_to_my_cost = costs[node]

            for out in outputs:
                current_cost = costs[out]
                new_total_cost = start_to_my_cost + outputs[out]
                if new_total_cost < current_cost:
                    costs[out] = new_total_cost
                    parents[out] = node
        node = find_lowest_cost()

    path = []

    parent = end

    while parent is not None:
        path.append(parent)
        if parent in parents:
            parent = parents[parent]
        else:
            parent = None

    return path


if __name__ == "__main__":
    path = calculate_path("START", "END")
    print("->".join(path[::-1]))
    print(costs)
