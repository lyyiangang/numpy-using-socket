import sys
sys.path.append('../../npsocket')
from npsocket import SocketNumpyArray
import cv2
print('you need start receiver.py first')
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
sock_sender = SocketNumpyArray()
# 'localhost'
sock_sender.initialize_sender('127.0.0.1', 9999)

while True:
    ret, frame = cap.read()
    # frame = cv2.resize(frame, (620, 480))
    sock_sender.send_numpy_array(frame)
