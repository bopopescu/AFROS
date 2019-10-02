import threading
import cv2


class split (threading.Thread) :

    def run(self):
        vidcap = cv2.VideoCapture('video_temp/video.avi')
        success, image = vidcap.read()
        count = 0
        success = True
        while success:
            success, image = vidcap.read()
            cv2.imwrite("frame%d.jpg" % count, image)  # save frame as JPEG file
            print('Read a new frame: ', success)
            count += 1

        else:
            pass