from Queue import Queue,LifoQueue
#Just an example graph taken from wikipedia 
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
	#This is a Stack Last in First out Queue = LifoQueue
	s = LifoQueue()
	#Used to keep track of parents for path finding purposes
	parentMap = {}
	#Visited nodes list
	visited = []
	s.put(root)
	while not s.empty():
		v = s.get()
		#break on goal state found
		if v == goal:
			break
		if v not in visited:
			visited.append(v)
			for neighbour in g[v]:
				s.put(neighbour)
				"""Done to prevent infinite loops between parents and 
				   children while finding paths"""
				if neighbour in visited:
					continue
				"""Map parent to children i,e whin 4 is being added to queue it's
				   also recorded that 3 is it's parent"""
				parentMap[neighbour] = v

	"""The path found will be in reverse order so we add it to a stack and pop to
	    straighten the path"""
	s2 = LifoQueue()
	curr = goal
	while(curr != None):
		s2.put(curr)
		if not parentMap.has_key(curr):
			break
		curr = parentMap[curr]

	while not s2.empty():
		print s2.get()

findElem(g,"1","10")