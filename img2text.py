from PIL import Image
from pytesseract import pytesseract
import glob
import os
import re

#define your tesseract.exe file path
path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def convertImage2Text(img):
    pytesseract.tesseract_cmd = path_to_tesseract 
    text = pytesseract.image_to_string(img) 
    return text[:-1]
    
def convertText2Field(img2text):
    
    #extract value of ringgit
    textRM = re.search("RM( {0,1}\d{1,5}\.\d{2})",img2text)
    valueRM = textRM.group(1).replace(' ','')
    Rm.append(valueRM)
    
    #extract value of date
    textDate = re.search ("(\d{1,2} \w{3} 20\d{2})", img2text)
    textDate = textDate.group(1).replace(' ','')
    date.append(textDate)
    
#_____________________________________________________________extract value of merchant_____________________________________________________________________________

    '''following code causing an issue, this is because of if user scan QR that is business, it contain "Merchant Name",
        if the account were personal account, it will showing as "Receipient Name" instead
        
        As for now required, better solution. Maybe split into 2 category,
        1. Merchant QR
        2. Personal QR
    '''
    
    try:
        merchant = re.search ("Merchant Name\n([^\n]*)", img2text)
        merchantName.append(merchant.group(1))
    except AttributeError as e:
        print("not match")
    except ValueError as e:
        print("value error")

      
    
if __name__=="__main__":
    
    directory_path = r"C:\Users\firex\OneDrive\Documents\duitNow\sample image"
    png_files = glob.glob(os.path.join(directory_path, "*.png"))
    
    Rm=[]
    date = []
    merchantName= []
    
    for file in png_files:
        img2text = convertImage2Text(file)
        
        toList= convertText2Field(img2text=img2text)
        
    rint(merchantName)
        
    
        
    
