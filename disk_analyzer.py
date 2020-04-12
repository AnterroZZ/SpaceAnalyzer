import os
import os

direcotry_sizes_dict = {}

def get_size(start_path = ".",size_previous = 2000):
    did_add = "no"
    total_sub_dir_size = 0
    for root, dirnames, filenames in os.walk(start_path):
        paths_names = os.listdir(start_path)
        for dirs in dirnames:
            size_kb = 0
            size_mb = 0
            if dirs in paths_names:
                path = os.path.join(root,dirs)
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
                        print(f"Adding {dirs} folder to dictonary")
                        directory_sizes_dict.update({path: size_mb})
                        did_add = "yes"
                
                elif (size_previous - total_sub_dir_size) >= 10000 and not paths_names:
                    print("listEmptyAndBiggerSize")

                


                

if __name__ == '__main__':  
    get_size('D:\GOPRO\GoPro\Białka')

