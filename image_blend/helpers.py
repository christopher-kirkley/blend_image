import os
import cv2 as cv
import numpy as np
import requests
import shutil

from config import FLICKR_KEY

def image_weight(image_list):
    percent = 1/len(image_list)
    return percent

def create_file_list(directory):
    file_list = os.listdir(directory)
    image_list = [f'{directory}/{file_}' for file_ in file_list if file_.endswith(('jpg','jpeg', 'png',))]
    return image_list

def resize(img, size):
    sh, sw = size
    h, w, *_ = img.shape
    aspect = w/h

    # interpolation method
    if h > sh or w > sw: # shrinking image
        interp = cv.INTER_AREA
    else: # stretching image
        interp = cv.INTER_CUBIC

    if aspect < 1:
        # Vertical image
        new_w = int(round(sw*aspect))
        new_h = sh
        padding = (sw - new_w)/2
        pad_left, pad_right = int(np.ceil(padding)), int(np.floor(padding))
        pad_top, pad_bot = 0, 0
    elif aspect > 1:
        # Horizontal image
        new_w = sw
        new_h = int(round(sh/aspect))
        padding = (sh - new_h)/2
        pad_top, pad_bot = int(np.ceil(padding)), int(np.floor(padding))
        pad_left, pad_right = 0, 0
    else:
        # Square image
        new_w = sw
        new_h = sh
        pad_top, pad_bot, pad_left, pad_right = 0, 0, 0, 0
    
    if len(img.shape) == 2:
         img = cv.cvtColor(img, cv.COLOR_GRAY2BGR)
    elif img.shape[2] == 4:
        img = img[:,:,:3]

    img = cv.resize(img, (new_w, new_h), interpolation=interp)
    img = cv.copyMakeBorder(img, pad_top, pad_bot, pad_left, pad_right, borderType=cv.BORDER_CONSTANT, value=(255, 255, 255))
    print(img.shape)
    return img


def resp_from_location(lat, lon):
    r = requests.get(f'https://www.flickr.com/services/rest/?method=flickr.photos.search&api_key={FLICKR_KEY}&accuracy=16&lat={lat}&lon={lon}&format=json&nojsoncallback=1')
    return r

def resp_from_keyword(keyword):
    r = requests.get(f'https://www.flickr.com/services/rest/?method=flickr.photos.search&api_key={FLICKR_KEY}&tags={keyword}&format=json&nojsoncallback=1')
    return r

def create_flickr_photo_list(response):
    json_result = response.json()
    photos = json_result['photos']['photo']
    photo_list = []
    for photo in photos:
        url = f'https://farm{photo["farm"]}.staticflickr.com/{photo["server"]}/{photo["id"]}_{photo["secret"]}.jpg'
        photo_list.append(url)
    return photo_list

def download_photo(photo_list):
    os.mkdir('temp')
    for index, url in enumerate(photo_list):
        # download url
        filename = url.split("/")[-1]
        r = requests.get(url, stream = True)
        if r.status_code == 200:
            r.raw.decode_content = True
        with open(f'temp/{filename}', 'wb') as f:
            shutil.copyfileobj(r.raw, f)
    return True

def clean_up():
    shutil.rmtree('temp')
    return True
