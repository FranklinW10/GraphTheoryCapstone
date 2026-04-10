savedturns = []
savedoptions = []
saveddensitys = []
savedpaths = []
expectedTimes =[]
SavedMaxs = []
SavedAverages = []

def CalculateCaptureTime(V, E):
    savedE = E.copy()
    for i in V:

#        VertexDensity = deg(i) / 2*NumEdges
        for j in V:
            current = i
            Probcalc(i,j,current, E.copy() , savedE, 0, [], [])
            calctotaltime(j, i, saveddensitys)
            saveddensitys.clear()



def Probcalc(i,j,current, E, savedE, turns, path, options_list):
    global savedoptions, savedturns, saveddensitys, savedpaths
    path = path + [current]

    if i != j:
        optionslist = []
        for u, v in E:
            if u == current:
                optionslist.append(v)
            elif v == current:
                optionslist.append(u)
        for next_vertex in optionslist:
            new_turns = turns + 1
            new_options = options_list + [len(optionslist)]
            if next_vertex == j:
                savedturns.append(new_turns)
                calc(new_turns, new_options)
                savedpaths.append(path.copy())
            else:
                newE = contract(E.copy(), current)
                Probcalc(i, j, next_vertex, newE, savedE, new_turns, path.copy(), new_options)
    


def contract(E, v):
    # Find neighbors of v
    neighbors = set()
    for u, w in E:
        if u == v:
            neighbors.add(w)
        elif w == v:
            neighbors.add(u)
    newE = set(E)

    # Add all edges between neighbors
    neighbors = list(neighbors)
    for i in range(len(neighbors)):
        for j in range(i+1, len(neighbors)):
            a = neighbors[i]
            b = neighbors[j]
            if a != b:
                newE.add((min(a,b), max(a,b)))

    # Remove edges involving v
    newE = { (u,w) for (u,w) in newE if u != v and w != v }

    return list(newE)


# def contract(E, i, current):
#     newE = []
#     for u, v in E:
#         # merge i into current
#         if u == i:
#             u = current
#         if v == i:
#             v = current

#         # remove self-loops only
#         if u != v:
#             newE.append((u, v))

#     return newE

def calc(turns, savedoptions_new):
    total = 1
    for i in savedoptions_new:
        total = total*(1/i)
    num = turns * total
    saveddensitys.append(num)

def calctotaltime(k, l, saveddensitys):
    total = 0
    for i in saveddensitys:
        total = total + i
    expectedTimes.append((sum(saveddensitys), k, l))
    print("Robber:", k, "Cop:", l, "Expected:", sum(saveddensitys))
    if k==len(V):
        calcsmax()
        if l == len(V):
            calcfinal()

def calcsmax():
    expected_values = [t[0] for t in expectedTimes]
    copPlacement = expectedTimes[0][2]
    Eavg = sum(expected_values) / len(expected_values)
    SavedAverages.append((Eavg, copPlacement))

    max_val = max(t[0] for t in expectedTimes)
    max_tuples = [t for t in expectedTimes if t[0] == max_val]
    # store them (either extend the list or append the sublist)
    SavedMaxs.extend(max_tuples)

#    max_tuple = max(expectedTimes, key=lambda t: t[0])
#    SavedMaxs.append(max_tuple)
    expectedTimes.clear()


def calcfinal():
    min_val = min(t[0] for t in SavedMaxs)
    max_val = max(t[0] for t in SavedMaxs)

    Smin_list = [t for t in SavedMaxs if t[0] == min_val]
    Smax_list = [t for t in SavedMaxs if t[0] == max_val]
    Savgmax = max(SavedAverages, key = lambda t: t[0])
    Savgmin = min(SavedAverages, key = lambda t: t[0])
    Averages = [t[0] for t in SavedAverages]
    for i in Averages:
        print(i)
    print("\nSmin (ties):")
    for t in Smin_list:
        print(" Cop:", t[2], "Robber:", t[1], "Expected:", t[0])

    print("\nSmax (ties):")
    for t in Smax_list:
        print(" Cop:", t[2], "Robber:", t[1], "Expected:", t[0])
    print("Savgmin: \n Cop:", Savgmin[1], "Expected:", Savgmin[0])
    print("Savgmax: \n Cop:", Savgmax[1], "Expected:", Savgmax[0])
    print(V)
    print(E)

V = [1,2,3,4]
E = [
(1,2),
(2,3),
(1,3),
(3,4)
]

CalculateCaptureTime(V, E)







