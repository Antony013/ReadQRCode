import cv2

def read_qr_code(filename) :
    img = cv2.imread(filename)
    detect = cv2.QRCodeDetector()
    value, points, straight_qrcode = detect.detectAndDecode(img)
    return print(value)

filename = input("Entre le nom de l'image QR Code : ")
splitFilename = filename.split(".")

if splitFilename[-1] == 0:
    print("Il manque l'extension de l'image (uniquement le PNG est accepté)")
elif splitFilename[-1] != "png":
    print("L'extension n'est pas assuré, veuillez entrer une image au format PNG")
else :
    read_qr_code(filename)
