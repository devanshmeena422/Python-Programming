import shutil

# shutil.rmtree('total;') # This will remove the directory even after the directory having files this is a powerfull module
shutil.copy("fullpart.txt" , "halfpart.txt") # This will copy the file and created new file of the same content of what we defined 

shutil.move("halfpart.txt" , 'dir/') # This will move the existing file to a existing directory 