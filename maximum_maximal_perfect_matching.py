def find_matching(graph, n):
    matching_set = list()

    # 1 edge
    edges=show_edges(graph_edges, total_v)
    matching_set = edges

    # 2 edges
    temp = edges
    res = []
    for i in temp:
        degree_list=reset_degree(n)
        matching = []
        update_degree([i],degree_list)
        #possible_edges = add_edge(degree_list,graph_edges)

        for j in edges:
            item = []
            if(check_degree(j[0],j[1],degree_list)):
                #update_degree([j],degree_list)
                item.append(i)
                item.append(j)
                item.sort()
                if(item not in res):
                    res.append(item)

    # more than 2 edges
    temp = res
    size = 3
    while (size < total_v):
        n_edges = []
        for i in temp: 
            degree_list=reset_degree(n)
            matching = []
            update_degree(i,degree_list)

            for j in edges:
                item = []
                if(check_degree(j[0],j[1],degree_list)):
                    for k in i:
                        item.append(k)
                    item.append(j)
                    item.sort()
                    if(item not in n_edges):
                        n_edges.append(item)
        if(n_edges):   
            for i in n_edges:
                if i not in res:
                    res.append(i)
        temp = n_edges
        size = size + 1
        x=matching_set+res

    return x

def show_edges(graph, n):
    matching_set = list()

    for i in range(n):
        set_vertex = graph_edges.get(i)
        for j in range(len(set_vertex)):
            if i > set_vertex[j]:
                matching_set.append([i, set_vertex[j]])
            elif i < set_vertex[j]:
                matching_set.append([set_vertex[j],i])
    matching_set = [i for m, i in enumerate(matching_set) if i not in matching_set[:m]]
    edges = matching_set
    return edges

def check_degree(vertex1, vertex2, degree_list):
    if degree_list[vertex1] == 1 or degree_list[vertex2] == 1:
        return False
    else:
        return  True

def update_degree(element,degree_list):
    for i in element:
        if(i):
            if (type(i[0]) == int):
                degree_list[i[0]] = 1
                degree_list[i[1]] = 1
            else:
                for k in i:
                    degree_list[k[0]] = 1
                    degree_list[k[1]] = 1

def reset_degree(total_v):
    degree_list = []
    for i in range(total_v):
        degree_list.append(0)
    return degree_list

def maximum_matching(x,maximal):
    mx = 0
    for i in x:
        if (len(i)>mx):
            mx = len(i)
    res = []
    for i in x:
        if (i and type(i[0]) != int and len(i) == mx):
            res.append(i)
    if (res):
        return res
    else:
        return maximal

def maximal_matching(x,total_v,graph_edges):
    degree_list=reset_degree(total_v)
    res = []
    edge = show_edges(graph_edges, total_v)
    for i in x:
        degree_list=reset_degree(total_v)
        do_not = 0
        if (i):
            update_degree([i],degree_list)
            for j in edge:
                if(check_degree(j[0],j[1],degree_list) == True):
                    do_not = 1
                    break
        if(i and do_not != 1):
            res.append(i)
    return res

def perfect_matching(x,total_v):
    res = []
    for i in x:
        degree_list=reset_degree(total_v)
        update_degree([i],degree_list)
        degree_list.sort()
        if(degree_list[0] == 0):
            continue
        res.append(i)
    if(res):
        return res
    else:
        return("perfect graph does not exist")


print("Total Vertex in graph:")
total_v = int(input())
degree_list = reset_degree(total_v)
print(degree_list)
graph_edges = dict()
for i in range(total_v):
    print("Enter separted names of all vertices connected with ", i,"th vertex:")
    graph_edges[i] = list(map(int,input().strip().split()))
print("graph: ",graph_edges)
ans=find_matching(graph_edges, total_v)
ans.insert(0,[])
print("Matching graphs:",ans)
maximal = maximal_matching(ans,total_v,graph_edges)
print("Maximal matching: ",maximal)
maximum = maximum_matching(ans,maximal)
print("Maximum matching: ",maximum)
print("Prefect matching: ",perfect_matching(maximum,total_v))