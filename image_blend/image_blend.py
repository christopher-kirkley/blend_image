import cv2 as cv
import argparse

from helpers import image_weight, create_file_list, resize

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='image_blend',
                                    description='Blend together directory of images',
                                    usage = '%(prog)s -d [options] directory output',)
    parser.add_argument('-s',
                        dest='data',
                        nargs=2,
                        help='size of output image',
                        type=int,
                        action='store',
                        required=True,
                        )

    parser.add_argument('-f',
                        dest='data',
                        nargs=1,
                        help='flickr keyword',
                        type=str,
                        action='store',
                        )

    parser.add_argument('-d',
                        dest='data',
                        nargs='1',
                        help='directory of source files',
                        type=str,
                        action='store',
                        )

    parser.add_argument('output', type=str, help='output')

    args = parser.parse_args()

    def transform(image_list):
        for index, image in enumerate(image_list):
            print(index, image)
            img = cv.imread(image, cv.IMREAD_UNCHANGED)
            print(img.shape)
            img = resize(img, dim)
            img = img * weight
            combined += img
            yield combined

    dim = tuple(args.data)
    print(dim)
    image_list = create_file_list(args.directory)
    weight = image_weight(image_list)
    combined_image = transform(image_list).astype("uint8")
    # for index, image in enumerate(image_list):
    #     print(index, image)
    #     img = cv.imread(image, cv.IMREAD_UNCHANGED)
    #     print(img.shape)
    #     img = resize(img, dim)
    #     image_list[index] = img * weight
    # combined_image = sum(image_list).astype("uint8")
    cv.imwrite(f'{args.output}.jpg', combined_image)

