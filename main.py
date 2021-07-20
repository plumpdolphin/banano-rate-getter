from brg.kuyumcu import Kuyumcu
from brg.banfarm import BanFarm


get = BanFarm()
bprice = get.purchase_price()
sprice = get.sell_price()
print(bprice, "|", sprice)