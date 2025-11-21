from PIL import Image

pathImages = ".\\Pasta images-20251115\\"

def rotation(imageName, angle):
    imagem = Image.open(pathImages + imageName)  # abre a imagem
    rotatedImage = imagem.rotate(angle, expand=True)  # roda com ajuste de tamanho
    rotatedImage.show() 
rotation("img1.jpg", 90)