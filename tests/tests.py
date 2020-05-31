import pytest
import os
import shutil
import cv2 as cv

from image_blend.helpers import image_weight, create_file_list, resize

@pytest.fixture
def image_files():
    path = os.getcwd()
    directory = 'temp'
    os.mkdir(directory)
    file_list = ['1.jpg', '2.jpg', '3.jpg', '4.jpg']
    for file_ in file_list:
        with open(f'{directory}/{file_}', 'w') as fp:
            pass
    yield directory
    os.chdir(path)
    shutil.rmtree('temp')

def test_can_print_images():
    image_list = ['image1.jpg', 'image2.jpg', 'image3.jpg']
    weight = image_weight(image_list)
    assert weight == 1/3

def test_can_create_file_list(image_files):
    file_list = create_file_list(image_files)
    assert len(file_list) == 4

def test_can_resize():
    file_list = create_file_list('tests/images')
    for file_ in file_list:
        img = cv.imread(file_, cv.IMREAD_UNCHANGED)
        print(file_)
        img = resize(img, (500, 500))
        assert img.shape == (500, 500, 3)
