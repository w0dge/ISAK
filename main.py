import re
from PIL import Image

fileName = "MTL_new.txt"
imageName = "B3_new.TIF"
orelCoordinates = {
    "UL": [53.1, 35.9],
    "UR": [53.1, 36.2],
    "LL": [52.8, 35.9],
    "LR": [52.8, 36.2]
}


def getPixels(filename):
    try:
        f = open(filename, 'r')
    except FileNotFoundError:
        print(f"{filename} doesn't exist")
        exit(-1)
    text = f.read()
    size = {
        "LINES": float(re.search(r"(?<=THERMAL_LINES = )\d*.\d", text)[0]),
        "SAMPLES": float(re.search(r"(?<=THERMAL_SAMPLES = )\d*.\d", text)[0])
    }
    return size


def getCoord(filename):
    try:
        f = open(filename, 'r')
    except FileNotFoundError:
        print(f"{filename} doesn't exist")
        exit(-1)
    text = f.read()
    coordinates = {
        "UL": [float(re.search(r"(?<=CORNER_UL_LAT_PRODUCT = )\d*.\d", text)[0]),
               float(re.search(r"(?<=CORNER_UL_LON_PRODUCT = )\d*.\d", text)[0])],
        "UR": [float(re.search(r"(?<=CORNER_UR_LAT_PRODUCT = )\d*.\d", text)[0]),
               float(re.search(r"(?<=CORNER_UR_LON_PRODUCT = )\d*.\d", text)[0])],
        "LL": [float(re.search(r"(?<=CORNER_LL_LAT_PRODUCT = )\d*.\d", text)[0]),
               float(re.search(r"(?<=CORNER_LL_LON_PRODUCT = )\d*.\d", text)[0])],
        "LR": [float(re.search(r"(?<=CORNER_LR_LAT_PRODUCT = )\d*.\d", text)[0]),
               float(re.search(r"(?<=CORNER_LR_LON_PRODUCT = )\d*.\d", text)[0])]
    }
    f.close()
    return coordinates


def deltaCoords(filename):
    coordinates = getCoord(filename)
    coords = {
        "UL": [],
        "UR": [],
        "LL": [],
        "LR": []
    }
    for coordinate in coordinates:
        coords[coordinate].append(
            abs((coordinates[coordinate][0] - orelCoordinates[coordinate][0]) * delta["height"]))
        coords[coordinate].append(
            abs((coordinates[coordinate][1] - orelCoordinates[coordinate][1]) * delta["width"]))

    return coords


def deltaPixel(height, width, coordinates):
    deltas = {
        "width": height / (coordinates["UR"][1] - coordinates["UL"][1]),
        "height": width / (coordinates["UR"][0] - coordinates["LR"][0])}
    return deltas


def newImage(name, newImageName, newPixels, height):
    try:
        image = Image.open(name)
    except FileNotFoundError:
        print(f"Image doesn't exist, {name} is incorrect. Can't crop it")
        exit(-1)
    cropped = image.crop(
        (newPixels["UL"][1], newPixels["UL"][0], newPixels["LR"][1] - 1000, height - newPixels["LR"][0]))
    cropped.save(newImageName)
    print(image.size)
    image = Image.open("e.TIF")
    print(image.size)


pixel = getPixels(fileName)
delta = deltaPixel(pixel["LINES"], pixel["SAMPLES"], getCoord(fileName))
pixels = deltaCoords(fileName)
print(delta)
print(pixel)
print(pixels)
newImage(imageName, "B3_cropped.TIF", pixels, pixel["LINES"])


