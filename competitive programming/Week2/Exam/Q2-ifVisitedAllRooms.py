def are_connected(rooms):
    marked = []
    connections = []
    components = 0

    for i in range(len(rooms)):
        marked.append(False)
        connections.append(i)

    def dfs(x):
        for y in x:
            if(y>len(rooms)-1):
                pass
            else:
                if not marked[y]:
                    marked[y] = True
                    dfs(rooms[y])
                    connections[y] = components

    for x in range(len(rooms)):
        if not marked[x]:
            marked[x] = True
            components+=1
            connections[x] = components
            dfs(rooms[x])

    if components==1:
        return True
    else:
        return False


if __name__ == '__main__':
    print(are_connected([[1],[0,2],[3]]))
    print(are_connected([[1,3], [3,0,1], [2], [0]]))
    print(are_connected([[1,2,3], [0], [0], [0]]))
    print(are_connected([[1], [0, 2, 4], [1, 3, 4], [2], [1, 2]]))
    print(are_connected([[1], [2,3], [1,2], [4], [1], [5]]))
    print(are_connected([[1], [2], [3], [4], [2]]))
    print(are_connected([[1], [1, 3], [2], [2, 4, 6], [], [1, 2, 3], [1]]))