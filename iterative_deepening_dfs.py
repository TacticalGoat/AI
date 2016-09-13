from Queue import LifoQueue,Queue
import sys
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
	found = None
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

"""Iteratively Increases the depth for dls"""
def IDDFS(node,goal):
	#setting to infinity gives memory errors range(0,sys.maxint)
	for depth in range(0,10000):
		found = dls(node,depth,goal)
		if found != None:
			return found

def findElem(node,goal):
	found = IDDFS(node,goal)
	if found != None:
		s2 = LifoQueue()
		curr = goal
		while(curr != None):
			s2.put(curr)
			if not parentMap.has_key(curr):
				break
			curr = parentMap[curr]

		while not s2.empty():
			print s2.get()

	else:
		print "Not found"


findElem("1","10")
