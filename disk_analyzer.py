import os

def get_size(start_path = "."):

    directory_sizes_dict = {}
    # for root, dirnames, filenames in os.walk(start_path):
    for firstFolders in os.listdir(start_path):
        print(f"Calculating size for \'{firstFolders}\' directory'")
        total_size = 0
        for root, dirnames, filenames in os.walk(os.path.join(start_path,firstFolders)): 
            for f in filenames:
                ffile = os.path.join(root,f)
                total_size += os.path.getsize(ffile)
        total_size /= 10**6
        directory_sizes_dict.update({os.path.join(start_path,firstFolders): f'{total_size} mb'})    
    print(directory_sizes_dict)
            

            


get_size('D:\GOPRO\GoPro\Białka')

