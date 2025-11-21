#Bandeira da frança

from PIL import Image

pathImages = ".\\Pasta images\\"
newSize=(250,250)
imagem= Image.new(size=newSize, mode="RGB", color="white")

pixelMap=imagem.load()
for i in range(imagem.width):
    for j in range(imagem.height):
        if i<80:
            pixelMap[i,j]=(0,0,255)
        elif i<160:
            pixelMap[i,j]=(255,255,255)
        else:
            pixelMap[i,j]=(255,0,0)
imagem.show()
imagem.save(pathImages+"Image_ex3")