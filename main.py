from maps.YuOsusume import YuOsusume

# ↓のリストには、メンバーの各オススメ学食が格納されます。
data = [YuOsusume(), ]
from maps.GakushokuTakato import GakushokuTakato

# ↓のリストには、メンバーの各オススメ学食が格納されます。
data = [GakushokuTakato(), ]

for rank, d in enumerate(data, start=1):
    print(f"{rank}位: {d.get_menu()}")
    print("---------------------------------")
    print(d.get_summary())
    print(d.get_author())
    print()