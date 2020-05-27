import os

DIM = (500, 500)

image_list = ['source/1.jpg', 'source/2.jpg', ]

def image_weight(image_list):
    percent = 1/len(image_list)
    return percent

def create_file_list(directory):
    file_list = os.listdir(directory)
    image_list = [f'{directory}/{file_}' for file_ in file_list if file_.endswith('jpg')]
    return image_list


