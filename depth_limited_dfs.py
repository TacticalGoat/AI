from Queue import Queue,LifoQueue

"""This is a recursive implementation to facilitate use with itereative deepening
	I was too lazy to make it iterative basically same comments apply for finding path
"""
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

parentMap = {}
visited = []
def dls(node,depth,goal):
	found = []
	visited.append(node)
	if node == goal:
		return node
	if depth == 0 and node != goal:
		return None
	elif depth > 0:
		for child in g[node]:
			if child not in visited:
				parentMap[child] = node
			found = dls(child,depth-1,goal)
			if found != None:
				return found

	return None

def findElem(node,depth,goal):
	found = dls(node,depth,goal)
	if found != None:
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

	else:
		print "Cannot be found at this depth!"



findElem("1",3,"10")