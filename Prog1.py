from PIL import Image, ImageFont, ImageDraw
import math
#lista caractere 
caractere = "@$B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
Ascii_car = list(caractere)
#Ascii_car = ["@", "#", "S", "%", "?","*","+","-",":",",","."," "]
fontEu = ImageFont.truetype("TIMESBD0.ttf", 7)
#calculez interval 
interval =  len(Ascii_car)/256
factor = 0.5
inaltime_car = 9
latime_caracter = 4.5 
caracter_ratio = latime_caracter/inaltime_car
#color to alb negru 
def black_and_white(image):
    alb_negru= image.convert("L")    
    return alb_negru

#fisier destinatie 
text_photo = open("photo.txt","w")

#pixel to caracter 

def pix_to_car( x  ):
    return Ascii_car[math.floor(x*interval)] 

#deschid poza 
try:
   poza= Image.open("gardfild.jpg")
except:
    print("eroare la deschidere ")
width,height = poza.size

copie = poza
#resize photo
poza =  poza.resize((int(factor*width),int(factor*height*caracter_ratio)), Image.NEAREST)
width,height = poza.size

#facem poza alba 
alb= black_and_white(poza)
alb.save("poza.png","png")

#poza output 


outputImage = Image.new("RGB",  (int(width*latime_caracter) ,int(height*inaltime_car)), color = (255,255,255))

#prelucram pixelii 
pix = alb.load()
width,height = poza.size
d= ImageDraw.Draw(outputImage)

for i in range(height):
    for j in range(width):
        gray= pix[j,i]
        text_photo.write(pix_to_car(gray))
        #d.text((j*latime_caracter,i*inaltime_car),pix_to_car(gray),font =fontEu, fill = copie.getpixel((j,i)) )
        #d.text((j*latime_caracter,i*inaltime_car),'#',font =fontEu, fill = copie.getpixel((j,i)) )
        d.text((j*latime_caracter,i*inaltime_car),pix_to_car(gray),font =fontEu, fill = (0,0,0) )
    text_photo.write("\n")


outputImage.save("final.png")