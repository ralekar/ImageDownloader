
import urllib2
import re,os
from os.path import basename
from urlparse import urlsplit


#url = "http://www.yahoo.com"
#urlContent = urllib2.urlopen(url).read()
# HTML image tag: <img src="url" alt="some_text"/>

def makeDirectory(directory):
    if not os.path.exists(directory):
	    os.makedirs(directory)
	    
def listImageUrls():
    imgUrls=[]
    typeCover=['tinycov','minicov','covers450','covers150dpi','covers300dpi']
    typeCoverExtn=['.gif','.gif','.jpg','.jpg','.jpg']
    files=open("count_by_record.txt","r")
    link="http://images.nap.edu/images/cover.php?id="
    typeLink="&type=" #covers450"
    for ids in files:
        temp=re.split(",",str(ids.strip()))
        year=re.split("/",temp[1])[2]
        if int(year)>=1995:
            index=0
            for cover in typeCover:
                urlLink=link+temp[0]+typeLink+cover
                ImgData(urlLink,cover,typeCoverExtn[index],temp[0])
                index+=1

def ImgData(link,directory,extn,ids):
    makeDirectory(directory)
    imgData = urllib2.urlopen(link).read()
    output = open(directory+"/"+ids+extn,'wb')
    output.write(imgData)
    output.close()



def main():
    listImageUrls()



if __name__=="__main__":
    main()
