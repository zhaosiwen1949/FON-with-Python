def get_args(lam=2,miu=35,time=100,num=320):
    import sys
    import getopt
    try:
        options,args = getopt.getopt(sys.argv[1:],"l:m:t:n:",["lam=","miu=","time=","num="])
    except getopt.GetoptError:
        sys.exit()
    for opt,val in options:
        if opt in ("-l","--lam"):
            lam = int(val)
        if opt in ("-m","--miu"):
            miu = int(val)
        if opt in ("-t","--time"):
            time = int(val)
        if opt in ("-n","--num"):
            num = int(val)
    #print(lam,miu,time,num)
    return (lam,miu,time,num)
