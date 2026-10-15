from maps.GakushokuTakato import GakushokuTakato
from maps.YuOsusume import YuOsusume
from maps.RinOsusume import RinOsusume
from maps.Gakusyoku_k25120 import Gakusyoku_k25120

# ↓のリストには、メンバーの各オススメ学食が格納されます。
data = [GakushokuTakato(), RinOsusume(),YuOsusume(),Gakusyoku_k25120(),]

for rank, d in enumerate(data, start=1):
    print(f"{rank}位: {d.get_menu()}")
    print("---------------------------------")
    print(d.get_summary())
    print(d.get_author())
    print()