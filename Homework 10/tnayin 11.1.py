import time  # toghery hertov irar takic tpvelu en

def POEM():
    with open("poem.txt", "r") as F:
        for i in F:
            print(i)
            time.sleep(3)

    F.close()


POEM()
# My heart's in the Highlands, my heart is not here
# My heart's in the Highlands a-chasing the deer
# A-chasing the wild deer, and following the roe
# My heart's in the Highlands wherever I go
# Farewell to the Highlands, farewell to the North
# The birth place of Valour, the country of Worth
# Wherever I wander, wherever I rove
# The hills of the Highlands for ever I love
# Farewell to the mountains high cover'd with snow
# Farewell to the straths and green valleys below
# Farewell to the forests and wild-hanging woods
# Farewell to the torrents and loud-pouring floods
# My heart's in the Highlands, my heart is not here
# My heart's in the Highlands, a-chasing the deer
# Chasing the wild deer, and following the roe
# My heart's in the Highlands wherever I go