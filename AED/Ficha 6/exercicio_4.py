#Gradient

from PIL import Image

pathImages = ".\\Pasta images\\"
newSize=(250,250)
imagem= Image.new(size=newSize, mode="RGB", color="white")

pixelMap=imagem.load()
for i in range(imagem.width):
    for j in range(imagem.height):
        r=i
        g=0
        b=imagem.width - i
        pixelMap[i,j]=(r,g,b)
imagem.show()
imagem.save(pathImages+"Image_ex4")