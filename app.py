from werkzeug.exceptions import MethodNotAllowed
from flask_cors import CORS, cross_origin
from flask import Flask, render_template, request, jsonify
from scraper.scraper import ImgScraper
from businesslayer.businesslayer_utility import BusinessLayer
import os 

# import request
app = Flask(__name__)       # initialising flask app with name 'app'

@app.route('/')     # route for rediecting to the home page
@cross_origin()
def home():
    return render_template('index.html')

@app.route('/showImages')
@cross_origin()
def showImages():
    list_images = os.listdir('images')
    print(list_images)
    
    try:
        if(len(list_images)>0):
            return render_template('showImages.html')
        else:
            return "Image does not present"
    except Exception as e:
        print("No images found",e)
        return "Please try with a different keyboard"

@app.route('/searchImages', methods=['GET','POST'])
def searchImages():
    if request.method=="POST":
        search_term = request.form['keyword']
    else:
        print("Please search something else")
        
    imagescraper_utility = BusinessLayer        
    imagescraper = ImgScraper()
    list_images = os.listdir('images')
    imagescraper.delete_downloaded_images(list_images)        #del previous image before new search
    
    image_name = search_term.split()
    image_name = "+".join(image_name)
    
    header ={'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"}
    list_images = imagescraper_utility.downloadImages(search_term, header)
    
    return showImages()


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8000)        