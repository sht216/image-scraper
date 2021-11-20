from bs4 import BeautifulSoup as bs
import json
import os 
import urllib.request
import urllib.parse
import urllib.error
from urllib.request import urlretrieve

class ImgScraper:
    # generate imgage url
    def ImageUrl(searchterm):
        searchterm = searchterm.split()
        searchterm = "+".join(searchterm)
        search_url = "https://www.google.com/search?q=" + searchterm + "&source=lnms&tbm=isch"
        return search_url 
    
    # raw html 
    def scrape_html_data(url, header):
        request = urllib.request.Request(url,headers=header)
        response = urllib.request.urlopen(request)
        responseData = response.read()
        html = bs(responseData, 'html.parser')
        return html 

    # image original link and the type of image 
    def getimageUrlList(raw_html):
        imageUrlList = []
        for a in raw_html.find_all("div", {"class":"bRMDJf islir"}):
            link, imageExtension = json.loads(a.text)["ou"], json.loads(a.text)["ity"]
            imageUrlList.append(link, imageExtension)
            
        print("there are total", len(imageUrlList), "images")
        return imageUrlList
    
    def downloadImagesFromUrl(imageUrlList, image_name, header):
        masterListofImages = []
        count = 0
        
        #print images
        imageFiles = []
        imageTypes = []
        image_counter = 0
        for i, (img, Type) in enumerate(imageUrlList):
            try:
                if (count>5):
                    break
                else:
                    count = count + 1 
                req = urllib.request.Request(img, headers=header)
                try:
                    urllib.request.urlretrieve(img,'images/' + image_name + str(image_counter) +".jpg")
                    image_counter = image_counter + 1 
                except Exception as e:
                    print("Image write failed: ", e)
                    image_counter = image_counter + 1
                    respData = urllib.request.urlopen(req)
                    raw_img = respData.read()
                    
                    imageFiles.append(raw_img)
                    imageTypes.append(Type)
                    
            except Exception as e:
                print("could not load: " + img)
                print(e)
                count = count + 1
        masterListofImages.append(imageFiles)
        masterListofImages.append(imageTypes)
                
        return masterListofImages
    
    def delete_downloaded_images(self, listOfImages):
        for self.image in listOfImages:
            try:
                os.remove('iamges/' + self.image)
            except Exception as e:
                print("error occured while deleting: " + e)
        
        return 0 
            