import os
import cv2
import numpy as np

##############
# 格式转换，tif 转 jpg
#########

workPath = os.getcwd()
path = workPath + "\\img\\"
newPath = workPath + "\\new\\"

# 找到当前路径下的所有.tif文件
tif_list = [x for x in os.listdir(path) if x.endswith(".tif")]
for num, filename in enumerate(tif_list):
    # 这里选择-1，不进行转化
    img = cv2.imdecode(np.fromfile(path+filename, dtype=np.uint8), -1)
    filename = filename[0:filename.index(".tif")]
    print(filename)
    cv2.imencode('.tif', img)[1].tofile(newPath + filename + ".jpg")
    print('总共:',len(tif_list),'张，剩余:',len(tif_list)-num-1,'张')