def block_rate(lam,miu,time,num_city,channel_spec):
    import pdb
    from ..resource.source import source
    from ..resource.route import generate_route,route_dict
    from ..resource.channel import generate_channel
    from ..algorism.algo_main import calculate_block
    src,nums = source(lam,miu,time,num_city)
    route = generate_route(route_dict(num_city))
    channel = generate_channel(route,channel_spec)
    block = calculate_block(src,route,channel,channel_spec)
    block_rate = block/nums
    pdb.set_trace()
    print("The number of block is",block)
    print("The rate of block is",block_rate)
