import cv2 as cv
import argparse

from helpers import image_weight, create_file_list

if __name__ == '__main__':
    DIM = (500, 500)
    parser = argparse.ArgumentParser(prog='image_blend',
                                    description='Blend together directory of images',
                                    usage = '%(prog)s directory',)
    
    parser.add_argument('directory', type=str, help='directory')
    args = parser.parse_args()
    image_list = create_file_list(args.directory)
    weight = image_weight(image_list)
    for index, image in enumerate(image_list):
        print(index, image)
        img = cv.imread(image, cv.IMREAD_UNCHANGED)
        print(img.shape)
        img = cv.resize(img, DIM, interpolation = cv.INTER_AREA)
        image_list[index] = img * weight
    combined_image = sum(image_list).astype("uint8")
    cv.imshow('combined', combined_image)
    cv.waitKey(0)

