def algo_bellman_ford(route):
    #generate the link array to save the value of link
    link = []
    i = 0
    for n in route:
        j = 0
        for m in n:
            if m == 1:
                link.append((i,j,1))
            j += 1
        i += 1
    #initialize the dist array
    from numpy import array
    dist = array([65536]*i**2).reshape(i,i,1)
    for k in range(0,i):
        dist[k][k][0] = 0
    #the hardcore of Bellman-Ford
    dist = dist.tolist()
    for k in range(0,i):
        for t in range(0,i-1):
            for n in range(0,len(link)):
                src,dst,val = link[n]
                if dist[k][src][0] < 30000:
                    if dist[k][src][0]+val < dist[k][dst][0]:
                        dist[k][dst][0] = dist[k][src][0]+val
                        dist[k][dst].extend(dist[k][src][1:])
                        dist[k][dst].append((src,dst))
    return dist
