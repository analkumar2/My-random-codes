#Author: Anal Kumar
#This program along with any batch download software can download any video file which are streamed segmentally eg. mts, ts
#I wrote the code for myself and you will probably want to understand the code and modify it heavily for your own use
#This program is basically just downloading individual parts of the file and stitching it together.

#Step 1: Specify link of any of the parts in the variable 'videolink'. You can use Video DownloadHelper for firefox for this. Just open the video in browser.
#       Then, copy the link from the Video DownloadHelper widget.
#Step 2: specify the extenstion in 'ext' variable.
#Step 3: Specify the link without the extension and the part number in 'videolink_base'.
#Step 4: Specify the name of the file in 'nameofthefile'.
#Step 5: In 'f', specify the folder where you want to put the list of files to be downloaded by your download manager.
#Step 6: In n, specify the part number of the last part of the video.
#Step 7: Run the for loop.
#Step 8: Now use the file created to download all the files.
#Step 9: Optional: Move the downloaded files to elsewhere if you want
#Step 10: The for loop in step 10 renames the video parts so that they can be joined properly in step 11.
#Step 11: Step 11 finally stitches all the video parts into a single file.


videolink = "http:/www.lkajsdfkj....................................." 

videolink_base=videolink[:168]
ext=".ts"

n=200 #Step 6

#download=[]
nameofthefile='Jarjar'


f=open("C:/Users/GSI-KOL/Desktop/batchdownload.txt", 'w') #Step 5
#Step 7
for i in range(n):
    f.write(videolink_base+str(i)+ext+'\n')
f.close()

#Step 9
import shutil
shutil.move("C:/Downloads/Video/pp","C:/Downloads/Pork/"+nameofthefile)

#Step 10
import os
for filename in os.listdir("C:/Downloads/Pork/"+nameofthefile):
        length = len(filename)
        if length==12:
            os.rename("C:/Downloads/Pork/"+nameofthefile +"/"+filename,"C:/Downloads/Pork/"+nameofthefile +"/"+filename[:8]+str(0)+str(0)+filename[-4:])
        if length==13:
            os.rename("C:/Downloads/Pork/"+nameofthefile +"/"+filename,"C:/Downloads/Pork/"+nameofthefile +"/"+filename[:8]+str(0)+filename[-5:])



#Step 11
import os
output=open("C:/Downloads/Pork/"+nameofthefile +".mp4",'ab')
for filename in os.listdir("C:/Downloads/Pork/"+nameofthefile):
    tem = open("C:/Downloads/Pork/"+nameofthefile +"/"+filename,'rb')
    output.write(tem.read())
    print filename + '\n'
    tem.close()
    









