def calculate_block(source,route,channel,channel_spec):
    from .algo_R_BF import algo_bellman_ford
    from .algo_SA_FH import algo_first_hit
    block = 0
    dist = algo_bellman_ford(route)
    for every_minute in source:
        for arrive_time,leave_time,duration,num_spec,path in every_minute:
            src,dst = path
            links = dist[src][dst]
            if algo_first_hit(arrive_time,leave_time,num_spec,links[1:],channel,channel_spec):
                block += 1
    return block
