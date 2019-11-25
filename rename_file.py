import os
os.chdir(r'C:\Users\karanbari\Desktop\YOLO\images\train_cleaned')



folder_name = r'C:\Users\karanbari\Desktop\YOLO\images\train_cleaned'
c=0

for i in os.listdir(folder_name):
    dst = 'Image' + str(c) +'.jpg'
    src = folder_name + '\\'+i
#     print(src)
    os.rename(src,dst)
    c+=10
