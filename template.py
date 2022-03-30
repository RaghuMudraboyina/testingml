

import os,sys

dirs = [
    os.path.join("data", "raw"),
    os.path.join("data","processed"),
    "notebooks",
    "saved_models",
    "src"
]
#loop over above directories ,exist_ok =false means if the folder is already created it will throw an error.if the dircetory
#exsits it will not throw an error

for dir_ in dirs:
    os.makedirs(dir_,exist_ok=True)
    with open(os.path.join(dir_, ".gitkeep"),"w") as f:
        pass
#.gitignore will ignore the files which we we dont to push .we need to create _int__ file just to make package
files = [
    "dvc.yaml",
    "params.yaml",
    ".gitignore",
   os.path.join("src","__init__.py")
]

for file_ in files:
    with open(file_,"w") as f:
        pass
