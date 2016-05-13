def get_args(lam=2,miu=35,time=100,num_city=14,channel_spec=320):
    import sys
    #import pdb
    import getopt
    try:
        options,args = getopt.getopt(sys.argv[1:],"l:m:t:n:c:",["lam=","miu=","time=","num_city=","channel_spec="])
    except getopt.GetoptError:
        sys.exit()
    for opt,val in options:
        if opt in ("-l","--lam"):
            lam = int(val)
        if opt in ("-m","--miu"):
            miu = int(val)
        if opt in ("-t","--time"):
            time = int(val)
        if opt in ("-n","--num_city"):
            num_city = int(val)
        if opt in ("-c","--channel_spec"):
            channel_spec = int(val)
    #print(lam,miu,time,num)
    #pdb.set_trace()
    return (lam,miu,time,num_city,channel_spec)
