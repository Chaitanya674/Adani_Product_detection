import cv2
import uuid 
import os 
import time

from numpy import append

cap = cv2.VideoCapture(0)

IMAGES_PATH = os.path.join('data' , 'images')
labels = ['Fortune_Product']
number_img  = 20
sleep_time = 5

class data_gen():

    def add_new_label(self ,name):
        labels.append(name)
        #add this name at the last for the dataset.yml file in the yolov5 directory
    
    def data_collector(self):
            for label in labels:
                print('collecting images for {}'.format(label))
                time.sleep(sleep_time)

                for img_num in range(number_img):
                    print('collecting images for {} , image number {}'.format(label , img_num))

                    ret, frame = cap.read()

                    data_id = str(uuid.uuid1())
                    
                    img_name = os.path.join(IMAGES_PATH, label+'.'+data_id+'.jpg')

                    bigger = cv2.resize(frame, (255, 255))

                    cv2.imwrite(img_name, bigger)

                    name_text = label+'.'+ data_id +'.txt'

                    f = open(f"./data/labels/{name_text}","w+")

                    #f.write("15 0.494118 0.560784 0.556863 0.698039\n")

                    f.write("15 0.500000 0.519608 0.521569 0.615686\n")

                    f.write("15 0.488235 0.535294 0.262745 0.882353\n")

                    f.write("15 0.507843 0.501961 0.749020 0.298039\n")

                    cv2.imshow('Image Collection', frame)

                    time.sleep(2)

                    if cv2.waitKey(10) & 0xFF == ord('q'):
                        break

            cap.release()
            cv2.destroyAllWindows()

    def start_train(self):
        os.system('cd yolov5 && python train.py --img 320 --batch 16 --epochs 500 --data dataset.yml --weights yolov5s.pt --workers 2')