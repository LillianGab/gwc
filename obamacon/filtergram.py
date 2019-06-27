from PIL import Image

#img = Image.open("image5.jpg")
#Shows image file opens up
#img.show()
#Gives the size of the image in pixels
#print(img.size)
#Gives length of image
#print(img.height)
#gives width of image
#print(img.width)
#Gives name of image
#print(img.filename)
#Gives mode of image
#print(img.mode)
#gives sequence object of image
#print(img.getdata(band=None))
### (not working) print(img.getpixel((3,2))

#pixl = img.getpixel((0,0))
#print(pixl)

#img = Image.open("frootloops.jpg")
#img.show()


import filters

# Should return a new image object with filter applied
def main():
    imagenames = ["guessilldie", "frootloops"]

if __name__ == "__main__":
    main()