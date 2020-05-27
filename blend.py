import cv2 as cv

def resize(image):
    img = cv.imread(image, cv.IMREAD_UNCHANGED)

    print('OG: ', img.shape)

    dim = (500, 500)

    resized = cv.resize(img, dim, interpolation = cv.INTER_AREA)

    print('Resized Dimensions: ', resized.shape)
    
    return resized

image_list = ['source/1.jpg', 'source/2.jpg', 'source/3.jpg']

number_of_images = len(image_list)
percent = 1/number_of_images
for index, image in enumerate(image_list):
    image = resize(image)
    image_list[index] = image * percent
combined_image = sum(image_list).astype("uint8")
cv.imshow('combined', combined_image)
cv.waitKey(0)


# dst = cv.addWeighted(img1, 0.5, img4, 0.5, 0)
# cv.imshow('dst', dst)
# cv.destroyAllWindows()
