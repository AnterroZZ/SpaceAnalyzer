import os
def get_precise_size(starting_path):
    total_size = 0
    for root, dirnames, filenames in os.walk(starting_path): 
            for f in filenames:
                ffile = os.path.join(root,f)
                total_size += os.path.getsize(ffile)
    return total_size

def get_size(start_path = "."):

    directory_sizes_dict = {}
    # for root, dirnames, filenames in os.walk(start_path):
    for firstFolders in os.listdir(start_path):
        print(f"Calculating size for \'{firstFolders}\' directory'")
        # for root, dirnames, filenames in os.walk(os.path.join(start_path,firstFolders)): 
        #     for f in filenames:
        #         ffile = os.path.join(root,f)
        #         total_size += os.path.getsize(ffile)
        path = os.path.join(start_path,firstFolders)
        size_of_folder = get_precise_size(path)
        size_mb = round( size_of_folder / 10**6)
        if(size_mb >= 2000):
            for root, dirnames, filenames in os.walk(path):
                for dirs in dirnames:
                    print(os.path.join(root,dirs))
                    

        directory_sizes_dict.update({path: f'{size_mb} mb'})    
    # print(directory_sizes_dict)
            

            

if __name__ == '__main__':  
    get_size('D:\GOPRO\GoPro\Białka')

