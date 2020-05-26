import os
from flask import Flask, render_template, request
from imagescrapper.ImageScrapper import ImageScrapper
from imagescrapperservices.ImageScrapperServices import ImageScrapperServices
from flask_cors import CORS,cross_origin


app = Flask(__name__)  # initialising the flask app with the name 'app'


@app.route('/')  # route for redirecting to the home page
@cross_origin()
def home():
    return render_template('index.html')


@app.route('/showImages')  # route to show the images on a webpage
@cross_origin()
def show_images():
    scraper_object = ImageScrapperServices()
    list_of_jpg_files = scraper_object.list_only_jpg_files('static')  # obtaining the list of image files from the static folder
    print(list_of_jpg_files)
    try:
        if (len(list_of_jpg_files) > 0):  # if there are images present, show them on a wen UI
            return render_template('showImage.html', user_images=list_of_jpg_files)
        else:
            return "Please try with a different string"  # show this error message if no images are present in the static folder
    except Exception as e:
        print('no Images found ', e)
        return "Please try with a different string"


@app.route('/searchImages', methods=['GET', 'POST'])
@cross_origin()
def search_images():
    if request.method == 'POST':
        search_term = request.form['keyword']  # assigning the value of the input keyword to the variable keyword
        scraper_object= ImageScrapperServices()
        list_of_jpg_files = scraper_object.list_only_jpg_files('static')  # obtaining the list of image files from the static folder
        scraper_object.delete_existing_image(list_of_jpg_files)
        # Driver_path = './chromedriver'
        ImageScrapper.search_and_download(search_term)
    return show_images()


if __name__ == "__main__":
    # app.run(host='127.0.0.1', port=8000) # port to run on local machine
    app.run(debug=True)  # to run on cloud
