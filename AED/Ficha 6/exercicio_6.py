from PIL import Image

pathImages = ".\\Pasta images-20251110\\"
imagem1=Image.open(pathImages+'img1.jpg')
pixelMap=imagem1.load()


def imageGrayScale():
    imagemCinza = Image.new("RGB", imagem1.size)
    pixelMapCinza = imagemCinza.load()
    for i in range(imagem1.width):
        for j in range(imagem1.height):
            p=[i,j]
            red=p[0]
            green=[1]
            blue=p[2]
            gray = int(0.299 * red + 0.587 * green + 0.114 * blue)
            pixelMapCinza[i, j] = (gray, gray, gray)
    imagemCinza.show()