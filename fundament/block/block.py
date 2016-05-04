from .argument import get_args
from .block_rate import block_rate
lam,miu,time,num = get_args()
block_rate(lam,miu,time,num)
