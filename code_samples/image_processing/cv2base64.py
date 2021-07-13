import cv2
import base64
import numpy as np

# read image by cv2
img = cv2.imread('test.jpg')
# encode base64
tmp = base64.b64encode(cv2.imencode('.png', img)[1]).decode()
# decode base64
rv = base64.b64decode(tmp.encode())
# read from buffer
rv = np.frombuffer(rv, dtype='uint8')
# cv2 decode
rv = cv2.imdecode(rv, 1)
# write image
cv2.imwrite('rv.png', rv)