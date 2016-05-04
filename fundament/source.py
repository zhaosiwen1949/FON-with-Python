import numpy as np
import scipy.stats as stats

def source(lam,miu,time):
    poi = stats.poisson.rvs(mu=lam,size=time)
    num = sum(poi)
    exp = stats.expon.rvs(scale=miu,size=num).astype("int").tolist()
    num_channels = [1,2,4,8,12]
    sig = signal(poi,exp[:],num_channels)
    #print(poi)
    #print("the durtion is",time,"minutes.")
    #print(exp)
    #print(sig)
    #print("the durtion is",len(sig),"minutes.")
    return (sig,num)

def signal(poi,exp,num_channels):
    import random
    sig = []
    arrive_time = 0
    leave_time = 0
    duration = 0
    channel = 0
    for number in poi:
        each_signal = []
        while number>=1:
            number-=1
            element_signal = ()
            duration = exp.pop(0)
            leave_time = arrive_time+duration
            channel = num_channels[random.randint(0,4)]
            element_signal = (arrive_time,leave_time,duration,channel,)
            each_signal.append(element_signal)
        sig.append(each_signal)
        arrive_time+=1
    return sig;
