def reconstruct_queue(people):
    if not people:
        return []

    # key=height, value=(k-value, index)
    people_dct, height, result = {}, [], []

    for i in range(len(people)):
        p = people[i]
        if p[0] in people_dct:
            people_dct[p[0]].append((p[1], i))
        else:
            people_dct[p[0]] = [(p[1], i)]
            height.append(p[0])

    height.sort()

    for h in height[::-1]:
        people_dct[h].sort()
        for p in people_dct[h]:
            result.insert(p[0], people[p[1]])
    return result


if __name__ == '__main__':
    print(reconstruct_queue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]))
    print(reconstruct_queue([[12,0],[6,3],[3,4],[9,2], [11,1],[1,5]]))
    print(reconstruct_queue([ [2,4], [5,1], [3,3], [1,5], [4,2], [6,0]]))
