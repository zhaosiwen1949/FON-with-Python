def block_rate(lam,miu,time,num):
    from ..source import source
    from ..spectrum import generate_spectrum
    from ..algorism_SA import algo_SA
    src,nums = source(lam,miu,time)
#   print(src)
    spec = generate_spectrum(num)
#   print(spec)
    block = algo_SA(src,spec)
    block_rate = block/nums
    print("The number of block is",block)
    print("The rate of block is",block_rate)
