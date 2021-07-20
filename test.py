from brg.kuyumcu import Kuyumcu
from brg.banfarm import BanFarm
from brg.jitswap import JitSwap
from brg.bananoexchange import BananoExchange


exchanges = [Kuyumcu(inverse_pair=True),
             JitSwap(inverse_pair=True)]

for get in exchanges:
    bprice = get.purchase_price()
    sprice = get.sell_price()
    print(bprice, "|", sprice)