GRAPH = {"A": {"B": 3, "C": 4, "E": 9, "F": 6},
         "B": {"A": 3, "C": 5, "D": 7},
         "C": {"A": 4, "B": 5},
         "D": {"B": 7},
         "E": {"B": 5, "A": 9},
         "F": {"A": 6}}


def bfs(graph, start, end):
    queue = [(start, [start])]
    while queue:
        node, path = queue.pop(0)
        for nextNode in graph[node]:
            if nextNode in path:
                continue
            elif nextNode == end:
                yield path + [nextNode]
            else:
                queue.append((nextNode, path + [nextNode]))
def djikstra(graph, the_list, start):
    thesum = 0
    item = graph.get(start)
    for x in the_list[0][1:]:
        print(graph.get(start).get("C"))
        print(x)
    print(thesum)
the_list = [x for x in bfs(GRAPH, 'A', 'D')]
djikstra(GRAPH, the_list, "B")
print(the_list)
print(the_list)