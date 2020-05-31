import cv2 as cv
import argparse

from image_blend.helpers import image_weight, create_file_list, resize, create_flickr_photo_list, download_photo, clean_up,\
resp_from_location, resp_from_keyword

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='image_blend',
                                    description='Blend together directory of images',
                                    usage = '%(prog)s -s [options] -f [options] -d [options] output',)
    parser.add_argument('-s',
                        dest='data',
                        nargs=2,
                        help='size of output image',
                        type=int,
                        action='store',
                        required=True,
                        )

    parser.add_argument(
                        '-k',
                        dest='keyword',
                        nargs=1,
                        help='flickr keyword',
                        type=str,
                        action='store',
                        )

    parser.add_argument(
                        '-l',
                        dest='location',
                        nargs=2,
                        help='flickr latitude/longitude',
                        type=str,
                        action='store',
                        )

    parser.add_argument(
                        '-d',
                        dest='directory',
                        nargs=1,
                        help='source file directory',
                        type=str,
                        action='store',
                        )

    parser.add_argument('output', type=str, help='output')

    args = parser.parse_args()

    dim = tuple(args.data)
    if args.keyword:
        response = resp_from_keyword(args.keyword)
        photo_list = create_flickr_photo_list(response)
        download_photo(photo_list)
        image_list = create_file_list('temp')
    elif args.location:
        lat, lon = args.location
        response = resp_from_location(lat, lon)
        photo_list = create_flickr_photo_list(response)
        download_photo(photo_list)
        image_list = create_file_list('temp')
    else:
        image_list = create_file_list(args.directory[0])
    weight = image_weight(image_list)
    for index, image in enumerate(image_list):
        print(index)
        img = cv.imread(image, cv.IMREAD_UNCHANGED)
        img = resize(img, dim)
        image_list[index] = img * weight
    combined_image = sum(image_list).astype("uint8")
    cv.imwrite(f'{args.output}.jpg', combined_image)
    # try:
    #     clean_up()
    # except:
    #     pass

