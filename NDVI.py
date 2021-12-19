import numpy
from PIL import Image
numpy.seterr(divide='ignore')

imagetifRed = Image.open('B3_cropped.TIF')
imagetifNIR = Image.open('B4_cropped.TIF')
RED = numpy.array(imagetifRed)
NIR = numpy.array(imagetifNIR)
# print(RED)
# print(NIR)

NDVI = (NIR-RED)/(NIR+RED)

print(imagetifRed.getpixel((400, 400)))
print("Выводим NDVI")
print(NDVI)
print(len(NDVI))
ndvi_image = Image.new("RGB", imagetifNIR.size, color=(255, 255, 255))
row = 0
for i in NDVI:
    for num in range(len(i)):
        if i[num] >= 0.9:
            ndvi_image.putpixel((num, row), (4, 18, 14))
        elif i[num] >= 0.8:
            ndvi_image.putpixel((num, row), (4, 38, 4))
        elif i[num] >= 0.7:
            ndvi_image.putpixel((num, row), (4, 54, 4))
        elif i[num] >= 0.6:
            ndvi_image.putpixel((num, row), (4, 66, 4))
        elif i[num] >= 0.5:
            ndvi_image.putpixel((num, row), (4, 94, 4))
        elif i[num] >= 0.4:
            ndvi_image.putpixel((num, row), (28, 114, 4))
        elif i[num] >= 0.3:
            ndvi_image.putpixel((num, row), (100, 162, 4))
        elif i[num] >= 0.2:
            ndvi_image.putpixel((num, row), (142, 182, 20))
        elif i[num] >= 0.166:
            ndvi_image.putpixel((num, row), (132, 138, 4))
        elif i[num] >= 0.133:
            ndvi_image.putpixel((num, row), (148, 114, 60))
        elif i[num] >= 0.1:
            ndvi_image.putpixel((num, row), (164, 130, 76))
        elif i[num] >= 0.066:
            ndvi_image.putpixel((num, row), (180, 150, 108))
        elif i[num] >= 0.033:
            ndvi_image.putpixel((num, row), (204, 190, 172))
        elif i[num] >= 0:
            ndvi_image.putpixel((num, row), (252, 254, 252))
        elif i[num] >= -0.1:
            ndvi_image.putpixel((num, row), (4, 18, 60))
    row += 1

ndvi_image.show()
