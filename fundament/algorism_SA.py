def algo_SA(source,spectrum):
    block = 0
    for every_minute in source:
        for arrive_time,leave_time,duration,num_spec in every_minute:
            count = 0
            for every_spec in spectrum:
                arrive_time_of_spec,leave_time_of_spec = every_spec
                if arrive_time >= leave_time_of_spec:
                    if count+num_spec-1 >= len(spectrum):
                        continue
                    else:
                        if spectrum[count] == spectrum[count+num_spec-1]:
                            tmp_spec = []
                            tmp_num = num_spec
                            while tmp_num >= 1:
                                tmp_spec.append((arrive_time,leave_time))
                                tmp_num -= 1
                            spectrum[count:count+num_spec] = tmp_spec
                            break
                        else:
                            count += 1
                            continue
                else:
                    count += 1
                    continue
            else:
                block += 1
    return block
