#Program name:    Imagecrawler from text file
#Auther: Muntakimur Rahaman
#Version= 0.0.1
#Contact= muntakim1104001@gmail.com

#******************************************#               
# usage python3 script.py 'textfile_name'  #
#******************************************#

#imports
import urllib.request
import sys

#varaibles
r=0
try:
    var=sys.argv[1]
    file=open(var,'r') #opening the text file
    data=file.readlines() #reading files

#for loop for download every image from url in Text file

    for f in data:
        curl=f.rstrip()
        urllib.request.urlretrieve(curl,"image%s.jpg"%(str(r))) #using url retriver for download images from url
        r+=1 #increament(r=r+1)
    print("Download successfull!")
except:
    print ('text file required!! \nPlease type python3 script.py "textfile_name"')



#output willbe image0.jpg to the length of the file.jpg
