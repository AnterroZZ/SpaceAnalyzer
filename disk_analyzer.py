import os

directory_sizes_dict = {}

def get_size(start_path = ".",size_previous = 2000):
    paths_names = os.listdir(start_path)
    print(paths_names)
    did_add = "no"
    total_sub_dir_size = 0
    for root, dirnames, filenames in os.walk(start_path):
        for dirnames in paths_names:
            size_kb = 0
            size_mb = 0
            path = os.path.join(root,dirnames)
            print(path)
            for sub_root, d, f in os.walk(path):
                for current_file in f:
                    ffile = os.path.join(sub_root,current_file)
                    size_kb += os.path.getsize(ffile)
                size_mb = round( size_kb / 10**6 )

                    #TODO Delete paths name cause scaned

                    
                if size_mb >= 10000:
                    get_size(path,size_mb)
                elif size_mb >= 3000:
                    print(f"Adding {dirnames} folder to dictonary")
                    directory_sizes_dict.update({path: size_mb})
                    did_add = "yes"
        break
                # elif (size_previous - total_sub_dir_size) >= 10000 and not paths_names:
                #     print("listEmptyAndBiggerSize")

                


                
if __name__ == '__main__':  
    get_size('D:\GOPRO\GoPro\Białka')
    print(directory_sizes_dict)

