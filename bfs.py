from Queue import LifoQueue,Queue
"""Everything the same for bfs as dfs refer to previous comments
   use a queue in place of a stack"""
g = {
    "1":["2","7","8"],
    "2":["3","6","1"],
    "3":["4","5","2"],
    "4":["3"],
    "5":["3"],
    "6":["2"],
    "7":["1"],
    "8":["9","12"],
    "9":["10","11","8"],
    "10":["9"],
    "11":["9"],
    "12":["8"]
}



def findElem(g,root,goal):
    q = Queue()
    parentMap = {}
    q.put("1")
    visited = []
    while not q.empty():
        v = q.get()
        if v == goal:
            break
        if v not in visited:
            visited.append(v)
            print(v)
            for neighbour in g[v]:
                q.put(neighbour)
                if neighbour in visited:
                    continue
                parentMap[neighbour] = v

    s2 = LifoQueue()
    curr = goal
    print parentMap
    while(curr != None):
        s2.put(curr)
        if not parentMap.has_key(curr):
            break
        curr = parentMap[curr]

    while not s2.empty():
        print s2.get()


findElem(g,"1","10")