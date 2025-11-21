from PIL import Image

pathImages = ".\\Pasta images-20251115\\"
imagem1=Image.open(pathImages+'img1.jpg')
pixelMap=imagem1.load()

def imageFrame2():
    altura=imagem1.height
    largura=imagem1.width
    for i in range(imagem1.width):
       for j in range(imagem1.height):
             if i < 10 or i >= largura - 10 or j < 10 or j >= altura - 10:
                pixelMap[i, j] = (0, 0, 255)  # azul
             elif largura // 2 - 5 <= i <= largura // 2 + 5:
                pixelMap[i, j] = (0, 0, 255)
             elif altura // 2 - 5 <= j <= altura // 2 + 5:
                pixelMap[i, j] = (0, 0, 255)
    imagem1.show()
    imagem1.save(pathImages+'Image_ex7')
imageFrame2()