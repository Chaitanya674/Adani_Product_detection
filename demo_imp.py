import torch
import numpy as np
import matplotlib.pyplot as plt
import detector 
from detector import *

'''Declaring the Object from the library'''
#dec = detector()
'''Detection throygh a directory'''
#dec.detection_image('./result')
'''detection through a Video Cam''' 
#dec.detection_video()


'''Detection in an image and then saving it as result.jpg'''
# model = torch.hub.load('ultralytics/yolov5', 'custom', path='yolov5/runs/train/exp5/weights/last.pt')
# img = r'result\WIN_20220621_15_54_58_Pro.jpg'
# results = model(img)
# results.print()
# result = plt.imshow(np.squeeze(results.render()))
# plt.savefig("result.jpg")p[]