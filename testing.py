import os

directory_sizes_dict = {}

def get_size(start_path = ".", value_to_beat= 20000):
    did_add = "no"
    for root, dirnames, filenames in os.walk(start_path):
        print(dirnames)
        if not dirnames:
            return did_add
        for dirs in dirnames:  
            total_size = 0 
            size_mb = 0
            if dirs in os.listdir(start_path):
                path = os.path.join(root,dirs)
                for r, d, ff in os.walk(path): 
                    for f in ff:
                        ffile = os.path.join(r,f)
                        total_size += os.path.getsize(ffile)
                    size_mb = round(total_size / 10 **6)
                    value_to_beat /= 2
                if(size_mb >= 10000):
                    if get_size(path, value_to_beat) is "no":
                        print(f"Adding {dirs} folder to dictonary")
                        directory_sizes_dict.update({path: size_mb})
                else:
                    print(f"Adding {dirs} folder to dictonary")
                    directory_sizes_dict.update({path: size_mb})
                    did_add = "yes"
                


if __name__ == '__main__':  
    get_size('D:\GOPRO\GoPro\Białka', 20000)
    print(directory_sizes_dict)