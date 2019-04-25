import cv2
import numpy as np
import os


##############
# 图片对比度，亮度调整
#########

workPath = os.getcwd()
print(workPath)
path = workPath + "\\img\\"
newPath = workPath + "\\new\\"
# c是对比度，b是亮度
def contrast_demo(oldImg, c, b, filename):
    rows, cols, chunnel = oldImg.shape
    blank = np.zeros([rows, cols, chunnel], oldImg.dtype)
    dst = cv2.addWeighted(oldImg, c, blank, 1 - c, b)
    cv2.imencode('.tif', dst)[1].tofile(newPath + filename)


for filename in os.listdir(path):
    if filename.endswith(".tif"):
        print(filename)
        img_path = path + filename
        img1 = cv2.imdecode(np.fromfile(img_path, dtype=np.uint8), cv2.IMREAD_COLOR)
        contrast_demo(img1, 20, 80, filename)

print("done")
