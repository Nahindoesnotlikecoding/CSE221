import sys

def Problem_F():
    n = int(sys.stdin.readline())
    vertices = {}
    indegree = {}
    words = []
    visited = {}
    for i in range(n):
        word = sys.stdin.readline().strip()
        words.append(word)
        for i in word:
            if i not in vertices:
                visited.update({i: False})
                vertices.update({i: []})
                indegree.update({i: 0})
    
    i = 0
    while i<len(words)-1:
        x = 0
        y = 0
        while x<len(words[i]) and y<len(words[i+1]):
            if words[i][x] == words[i+1][y]:
                x += 1
                y += 1
            else:
                vertices[words[i][x]].append(words[i+1][y])
                indegree[words[i+1][y]] += 1
                break
        
        if x<len(words[i]) and y>=len(words[i+1]):
            print(-1)
            return  
        i+=1
    
    output = []
    queue = []
    for i in indegree:
        if indegree[i] == 0:
            queue.append(i)
    while queue:
        queue.sort()
        u = queue.pop(0)
        visited[u] = True
        output.append(u)
        for v in vertices[u]:
            if indegree[v] > 0:
                indegree[v] -= 1
                if indegree[v] == 0:
                    queue.append(v)

    for i in visited:
        if visited[i] == False:
            print(-1)
            return
    
    print("".join(output))

Problem_F()
