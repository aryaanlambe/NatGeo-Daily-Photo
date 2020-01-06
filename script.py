from bs4 import BeautifulSoup
import requests, shutil, datetime,os

'''
File: FILENAME:file_name
Author: Aryaan Lambe
Description: Get & Save Photo of the Day from nationalgeographic.com
'''
r = requests.get("https://www.nationalgeographic.com/photography/photo-of-the-day/")
data = r.content

# Print data
soup = BeautifulSoup(data, "html.parser")
# Print soup.prettify()
print('_____________________________')
ImageUrl = ''
for link in soup.find_all('script'):
    if link.getText().find('aemLeadImage') != -1:
        # Print (Link)
        ImageUrl = link.getText()
ImageUrl = ImageUrl[ImageUrl.find('aemLeadImage\': \'')+ 16 : ]
ImageUrl = ImageUrl[: ImageUrl.find('\'') ]
print (ImageUrl)
r = requests.get(ImageUrl , stream=True)
data = r.raw
print (data)
with open("NatGeo" + os.sep + str(datetime.datetime.today().date()) + ".jpg", 'wb') as out_file:
     shutil.copyfileobj(r.raw, out_file)
del r
os.startfile(os.getcwd()+os.sep +"NatGeo" + os.sep + str(datetime.datetime.today().date()) + ".jpg")




