from brg.kuyumcu import Kuyumcu
from brg.banfarm import BanFarm
from brg.jitswap import JitSwap
from brg.bananoexchange import BananoExchange


exchanges = [Kuyumcu(),
             JitSwap()]

for get in exchanges:
    bprice = get.purchase_price()
    sprice = get.sell_price()
    print(bprice, "|", sprice)