def calculate_block(source,route):
    block = 0
    for every_minute in source:
        for arrive_time,leave_time,duration,num_spec,path in every_minute:

