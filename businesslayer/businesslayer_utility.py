from scraper.scraper import ImgScraper

class BusinessLayer:
    keywords=""
    fileloc=""
    image_name=""
    header=""
    
    def downloadImages(keyword, header):
        imageScraper = ImgScraper
        url = imageScraper.ImageUrl(keyword)
        raw_html = imageScraper.scrape_html_data(url, header)
        
        imageUrlList = imageScraper.getimageUrlList(raw_html)
        
        masterListOfImages = imageScraper.downloadImagesFromUrl(imageUrlList, keyword, header)
        
        return masterListOfImages