import os

os.chdir("R:\\rifat")

for f in os.listdir():
    file_name,file_ext=os.path.splitext(f)

    f_coureid,f_chapter,f_file,f_random,f_name=file_name.split('_')

    new_name='{}-{}-{}{}'.format(f_chapter,f_file,f_name,file_ext)
    os.rename(f,new_name)
    
    #print(new_name)