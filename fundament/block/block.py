def main():
    from .argument import get_args
    from .block_rate import block_rate
    lam,miu,time,num_city,channel_spec = get_args()
    block_rate(lam,miu,time,num_city,channel_spec)
