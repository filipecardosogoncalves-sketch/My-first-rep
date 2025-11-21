from PIL import Image
import random

pathImages = ".\\Pasta images\\"
width= 400
heigth=400

def imageArt():
    imageSize=(400,400)
    image1= Image.new(size=imageSize, mode="RGB")
    pixelMap=image1.load()
#interar todos os pixels da imagem, gerando um tupo RGB
    for i in range(width):
        for j in range(heigth):
            r=random.randint(0,255)
            g=random.randint(0,255)
            b=random.randint(0,255)
            pixelMap[i,j]= (r,g,b)
    image1.show()
    image1.save(pathImages+"Image_ex1")
imageArt()

