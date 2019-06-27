"""
author: Nazim Bahadir BARDAKCI || nazimbahadirbardakci[at]gmail[dot]com
advisor: Abdullah ERDEMİR      || aerdemir[at]mpg[dot]com[dot]tr
=========================================================
Detecting Pixel size of an image and find defined how many pixels have same RGB.
=========================================================
This Code calculating pixel size of an image and where you defined RGB in list.
Scanning image from x and y axis then calculating RGB colours with distance formula.
After that adding pixels number in list then show it. You can calculate percentages every colors in image
Finally Many thanks to Abdullah ERDEMIR. He helped me soo much while calculating pixels rate.
If you want to see more about to him visit : www.abdullaherdemir.com
"""
print(__doc__)

#import requirements
from PIL import Image

#Getting number of pixels
def get_number_of_pixels(filepath):
    width,height = Image.open('testorj.jpg').size
    return width*height
print(get_number_of_pixels('testorj.jpg'))#printing pixel size of defined image

#Getting determine to RGBs which are defined in list

#open image
img= Image.open('testorj.jpg')

#load image
p=img.load()

#define colors in lists
#you can use paint to see RGB of the image
c1=[245,223,137]
c2=[110,116,78]
c3=[186,176,104]
c4=[89,87,64]

count=[0,0,0,0]#set zero how many color do you have. There are four colors so i used for zeros in the list

#NOTICE : arrays always start from zero
#Start to scan image on x and y coordinates
for y in range(img.size[0]):#scanning for every coloumn
    for x in range(img.size[1]):#scanning for every row.
        #distance formula at three dimension
      dist1 = ((p[y,x][0]-c1[0])**2)+((p[y,x][1]-c1[1])**2)+((p[y,x][2]-c1[2])**2)
      dist2 = ((p[y, x][0] - c2[0]) ** 2) + ((p[y, x][1] - c2[1]) ** 2) + ((p[y, x][2] - c2[2]) ** 2)
      dist3 = ((p[y, x][0] - c3[0]) ** 2) + ((p[y, x][1] - c3[1]) ** 2) + ((p[y, x][2] - c3[2]) ** 2)
      dist4 = ((p[y, x][0] - c4[0]) ** 2) + ((p[y, x][1] - c4[1]) ** 2) + ((p[y, x][2] - c4[2]) ** 2)

      #now we are going to check which pixel close to defined color list
      mind = min(dist1,dist2,dist3,dist4)
      number=-1
      if mind==dist1:
          number=0
      if mind==dist2:
          number=1
      if mind==dist3:
          number=2
      if mind==dist4:
          number=3
      count[number]=count[number]+1

      print(x,"\t",y)#printing pixel numbers of an image it stops when reach size

print(count)#printing all pixels which are in colors list

#showing image
img.show()