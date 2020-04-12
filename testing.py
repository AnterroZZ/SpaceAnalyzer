import os

directory_sizes_dict = {}

def get_size(start_path = ".", did_add=True):
    paths_names = os.listdir(start_path)
    for root, dirnames, filenames in os.walk(start_path):
        size_kb = 0
        sub_size = 0
        print(f"FOR {root}")
        if not dirnames:
            sub_size = 0
        else:  
            for d in dirnames:
                dp = os.path.join(root,d)
                print(dp)
                sub_size += get_size(dp)
                print(f"{dp} is adding {sub_size}")
        for f in filenames:
            fp = os.path.join(root,f)
            if not os.path.islink(fp):
                size_kb += os.path.getsize(fp)
        size_mb = round( size_kb / 10**6 )
        print(sub_size)
        print(size_mb)
        if sub_size == 0:
            if(did_add):
                return size_mb
            elif size_mb > 10000:
                print(f"The size for {root} is {size_mb+sub_size}")
                directory_sizes_dict.update({root: size_mb+sub_size})
        elif sub_size < 10000:
            print(f"The size for {root} is {size_mb+sub_size}")
            directory_sizes_dict.update({root: size_mb+sub_size})
                


if __name__ == '__main__':  
    get_size('D:\GOPRO\GoPro\Białka',False)
    print(directory_sizes_dict)