#import pdb
def generate_index(src,dst):
    if src < dst:
        return str(src)+"-"+str(dst)
    else:
        return str(dst)+"-"+str(src)

def max_leave_time(range_array,num_spec):
    max_time = []
    for n in range(0,num_spec):
        tmp_time = 0
        for a_t,l_t in range_array[:,n]:
            if l_t >= tmp_time:
                tmp_time = l_t
        max_time.append(tmp_time)
    max_leave_time = max(max_time)
    return max_leave_time

def algo_first_hit(arrive_time,leave_time,num_spec,links,channel,channel_spec):
    from numpy import array,dtype
    #constuct the related array
    relate_path = []
    d_type = dtype([("arrive_time","int32"),("leave_time","int32")])
    num_link = len(links)
    for src,dst in links:
        index = generate_index(src,dst)
        relate_path.append(channel[index])
    #hardcore of first-hit algorism
    #pdb.set_trace()
    relate_path = array(relate_path,dtype=d_type)
    #pdb.set_trace()
    for i in range(0,channel_spec):
        if i+num_spec > channel_spec:
            continue
        else:
            range_array = relate_path[:,i:i+num_spec]
            max_leave_time_of_channel = max_leave_time(range_array,num_spec)
            if max_leave_time_of_channel > arrive_time:
                continue
            else:
                range_array = []
                for r in range(0,num_link*num_spec):
                    range_array.append((arrive_time,leave_time))
                #pdb.set_trace()
                relate_path[:,i:i+num_spec] = array(range_array,dtype=d_type).reshape(num_link,num_spec)
                break
    else:
        return True
    #update the dict of channel
    relate_path = relate_path.tolist()
    for src,dst in links:
        index = generate_index(src,dst)
        channel[index] = relate_path.pop(0)
    return False
