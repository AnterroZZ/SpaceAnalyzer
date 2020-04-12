import os
import matplotlib.pyplot as plt

directory_sizes_dict = {}

def get_size(start_path = ".", did_add=True):
    paths_names = os.listdir(start_path)
    for root, dirnames, filenames in os.walk(start_path):
        size_kb = 0
        sub_size = 0
        if not dirnames:
            sub_size = 0
        else:  
            for d in dirnames:
                dp = os.path.join(root,d)
                sub_size += get_size(dp)
        for f in filenames:
            fp = os.path.join(root,f)
            if not os.path.islink(fp):
                size_kb += os.path.getsize(fp)
        size_mb = round( size_kb / 10**6 )
        print(f"Total size for {root} is {size_mb}mb in files and {sub_size}mb in subfolders")
        if did_add:
            return size_mb + sub_size
        elif sub_size < 10000 and size_mb + sub_size > 10000:
            # print(f"The size for {root} is {size_mb+sub_size}")      
            directory_sizes_dict.update({root: size_mb+sub_size})
                


if __name__ == '__main__':  
    get_size('D:\GOPRO',False)

    directory_sizes_dict = dict(sorted(directory_sizes_dict.items(), key= lambda x: [x[1], x[0]], reverse=False))
    plt.barh(range(len(directory_sizes_dict)), list(directory_sizes_dict.values()), align='center')
    plt.title('Folders taking the most space')
    plt.xlabel('Size')
    plt.show()