#map
graph ={
    'a':{'n':['c'],'c':None},
    'b':{'n':['c','e'],'c':None},
    'c':{'n':['a','b','d','e'],'c':None},
    'd':{'n':['c'],'c':None},
    'e':{'n':['c','b'],'c':None},
    'f':{'n':[],'c':None}
}

colors=['r','g','b']

queue = ['a', 'b', 'c', 'd', 'e', 'f']

def csp():
    if len(queue) == 0:
        return True
    # sort by number of neightbors
    node = queue.pop(0)

    # sort colors based on huristic
    for color in colors:
        if all(graph[n]['c'] != color for n in graph[node]['n']): 
            graph[node]['c'] = color
            result = csp()
            if result == True:
                return True
    
    graph[node]['c'] = None
    queue.insert(0, node)
    return False   

x=csp()

for key, value in graph.items():
    print(key, value)

