import pytesseract
import cv2
import PIL.Image
myconfig = r"--psm 11 --oem 3"
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
img = cv2.imread("tim1.jpg")
height, width= img.shape

boxes = pytesseract.image_to_boxes(img,config=myconfig)
for box in boxes.splitlines():
	box = box.split(" ")
	img = cv2.rectangle(img,(int(box[1]),height - int(box[2])),(int(box[3]),height - int(box[4])),(0,255,0))
cv2.imshow("img",img)
cv2.waitkey(0)
