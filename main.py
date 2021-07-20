from brg.kuyumcu import Kuyumcu
from brg.banfarm import BanFarm
from brg.jitswap import JitSwap


get = JitSwap()
bprice = get.purchase_price()
sprice = get.sell_price()
print(bprice, "|", sprice)