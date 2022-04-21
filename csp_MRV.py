
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

def m_colors(node):
    neighbors_colors=[]
    allowed=[]
    for nd in graph[node]['n']:
        neighbors_colors.append(graph[nd]['c'])
    
    for color in colors:
        if color not in(neighbors_colors):
            allowed.append(color)

    return len(allowed)

queue = ['a', 'b', 'c', 'd', 'e', 'f']

def csp():
    temp=[]
    if len(queue) == 0:
        return True
    node = queue.pop(0)
    for color in colors:
        if all(graph[n]['c'] != color for n in graph[node]['n']): 
            graph[node]['c'] = color
            # sort queue by number of colors allowed
            queue.sort(key=m_colors)
            print(queue)
            result = csp()
            if result == True:
                return True

    graph[node]['c'] = None
    queue.insert(0, node)
    return False   

x=csp()

for key, value in graph.items():
    print(key, value)

