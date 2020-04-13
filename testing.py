import os
import matplotlib.pyplot as plt

dics = {
    'D:\\GOPRO\\GoPro\\Białka\\Pierwszy': 15170,
 }
sub_dics = ['D:\\GOPRO\\GoPro\\Białka']
                


if __name__ == '__main__':  
    for root, dirnames, filenames in os.walk('D:\GOPRO\GoPro\Białka'):
        print(root)
        if root in sub_dics:
            for d in dirnames:
                pt = os.path.join(root,d)
                print(pt)
                sub_dics.append(pt)
    print(sub_dics)
    