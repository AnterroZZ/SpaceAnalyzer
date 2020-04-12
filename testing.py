import os
import matplotlib.pyplot as plt

dics = {
    'D:\\GOPRO\\GoPro\\Białka\\Po': 13534,
    'D:\\GOPRO\\GoPro\\Białka\\Przed\\Nowy folder': 15170,
    'D:\\GOPRO\\XIAOMI\\GOPRO': 11306
 }
                


if __name__ == '__main__':  
    dics = dict(sorted(dics.items(), key= lambda x: [x[1], x[0]], reverse=True))
    print(dics)
    