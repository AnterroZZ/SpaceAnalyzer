from flask import Flask, render_template
import matplotlib.pyplot as plt
import os
import webbrowser

#Change this to change directory that you want to be scanned
scanned_directory = 'D:\Program Files (x86)'

#Change these 2 to alter the size of folders and files to be found
scanned_file_size = 2000
scanned_dir_size = 5000



directory_sizes_dict = {}
files_sizes_dict = {}
sub_list = []


app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

def get_size(start_path = ".", did_add=True, dir_size=10000, file_size=2000):
    paths_names = os.listdir(start_path)
    for root, dirnames, filenames in os.walk(start_path, topdown=True):
        if root in sub_list:
            sub_list.remove(root)
            for d in dirnames:
                pt = os.path.join(root,d)
                sub_list.append(pt)
        else:
            size_kb = 0
            size_mb = 0
            sub_size = 0
            # If directory doesnt have any subdirectories
            if not dirnames:
                sub_size = 0
            else:  
                # Browsing through all subdirectories to get their size
                for d in dirnames:
                    dp = os.path.join(root,d)
                    sub_size += get_size(dp)
            # Summing sizes of all files in current directory
            for f in filenames:
                fp = os.path.join(root,f)
                if not os.path.islink(fp):
                    size_current = round( os.path.getsize(fp) / 10**6 )
                    if size_current> file_size:
                        files_sizes_dict.update({f: size_current})
                    size_mb += size_current
            print(f"Total size for {root} is {size_mb}mb in files and {sub_size}mb in subfolders")
            if did_add:
                return size_mb + sub_size
            elif size_mb > dir_size:
                directory_sizes_dict.update({root: size_mb+sub_size})
                for x in dirnames:
                    sub_list.append(os.path.join(root,x))
            elif sub_size < dir_size and size_mb + sub_size > dir_size:
                # print(f"The size for {root} is {size_mb+sub_size}")      
                directory_sizes_dict.update({root: size_mb+sub_size})
                for x in dirnames:
                    sub_list.append(os.path.join(root,x))

                
if __name__ == '__main__':

    get_size(scanned_directory,False, dir_size=scanned_dir_size,file_size=scanned_file_size)
    print(directory_sizes_dict)
    # print(sub_list)

    directories, directories_sizes = zip(*sorted(directory_sizes_dict.items(), key= lambda x: [x[1], x[0]], reverse=False))
    files, files_sizes = zip(*sorted(files_sizes_dict.items(), key= lambda x: [x[1], x[0]], reverse=False))
    plt.figure(figsize=(10,5))
    plt.barh(directories,directories_sizes)
    plt.title('Biggest sized folders')
    plt.xlabel('Size')
    plt.tight_layout()
    plt.savefig("static/graphs/folder_sizes.png")

    plt.figure(figsize=(10,5))
    plt.barh(files,files_sizes)
    plt.title('Biggest sized files')
    plt.xlabel('Size')
    plt.tight_layout()
    plt.savefig("static/graphs/files_sizes.png")


    if os.name is 'nt':
        os.system("set FLASK_APP=analyzer.py") 
        os.system("set FLASK_DEBUG=1")
    else:
        os.system("export FLASK_APP=analyzer.py") 
        os.system("export FLASK_DEBUG=1")
    webbrowser.open('http://localhost:5000', new=2)
    app.run(debug=False)
    