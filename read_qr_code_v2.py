import cv2
from PIL import Image

def read_qr_code(filename) :
    img = cv2.imread(filename)
    detect = cv2.QRCodeDetector()
    value, points, straight_qrcode = detect.detectAndDecode(img)
    return print(value)

filename = input("Entre le nom de l'image QR Code : ")
splitFilename = filename.split(".")
read = True

if splitFilename[-1] == 0:
    read = False
    print("Il manque l'extension de l'image (uniquement le PNG est accepté)")
elif splitFilename[-1] != "png":
    print("L'extension n'est pas assuré, veuillez entrer une image au format PNG")
    read = False
    convert = input('Voulez-vous convertir le format de l\'image ? (o pour oui)')
    if convert == 'o': 
        # filename = input('Entrez le nommage de l\'image à convertir : ')
        imgFrom = Image.open(filename)
        imgFrom.save(filename+".png")
        restartReadQrCode = input('Voulez vous retenter la lecture du QR Code avec la même image avec la nouvelle extension ? (o pour oui)')
        if restartReadQrCode == 'o':
            read = True

if read == True:
    read_qr_code(filename)
    