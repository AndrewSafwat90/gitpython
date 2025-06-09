from PIL import Image


myImage = Image.open("E:\python\py1\py2\cat.jpg")

# myImage.show()

myBox = [370, 150, 750, 750]
myNewImage = myImage.crop(myBox)
# myNewImage.show()

myConvertedImage = myNewImage.convert("L")
myConvertedImage.show()
