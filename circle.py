import cv2
import numpy as np
from PIL import Image,ImageDraw
from matplotlib import pyplot as plt 

a=30
for a in range(30,31):
 filename = str(a) + '.jpg'
 img=Image.open(filename)
 m,n=img.size
 #print(m,n)
 img=cv2.imread(filename,0)
 #pic = img[1:n, 1:m]
 pic=img[1:n,int(m/2):m]
 #print(pic)
 cv2.imshow('image.jpg', pic)
#pic= img[int(m/2):m-1,1:n]
 cv2.imwrite('eye2.jpg',pic)




 img = cv2.imread('eye2.jpg',0)
  
 img = cv2.medianBlur(img,5)
 cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
 
 imgGray = cv2.cvtColor(cimg, cv2.COLOR_BGR2GRAY)
 m=10
 for m in range(10,150):
  threshold,imgOtsu=cv2.threshold(imgGray,m,255,cv2.THRESH_BINARY)
#ret2,imgOtsu = cv2.threshold(imgGray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
  cv2.imwrite('pic.jpg',imgOtsu)
  plt.imshow(imgOtsu,cmap = 'gray')




  img = cv2.imread('pic.jpg',0)

  img = cv2.medianBlur(img,5)
  cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
  circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20,param1=5,param2=15,minRadius=0,maxRadius=0)
# circles = np.uint16(np.around(circles))
  if circles is None:
     m=m+1;
     continue
  else:
     break

 if circles is None:
         print('no')
 else:
    circles = np.uint16(np.around(circles))
    for i in circles[0,:]:
    # draw the outer circle
     cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
     cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
     print(i[0])
    #print(a)

     '''cv2.imshow('detected circles',cimg)
     cv2.imwrite('result.jpg',cimg)
     cv2.waitKey(0)
     cv2.destroyAllWindows()

     cv2.waitKey(0)
     cv2.destroyAllWindows()'''


 a=a+1

'''
import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('pic.jpg',0)
plt.hist(img.ravel(),256,[0,256])
plt.show()
'''