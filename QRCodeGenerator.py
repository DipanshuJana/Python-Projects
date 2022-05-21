import qrcode # generate a qr code for the string given by the user
import time # for customization of the program
import cv2 # for scanning the qr code
import sys

def qrCodeGenerator(user_input): # main function
    image = qrcode.make(user_input)
    image.save("D:\\Productivity\\Python\\Projects\\QRCode.jpg")


if __name__ == '__main__':

    user_input = str(input('Enter the text you want to generate the QR Code:'))
    print ('\nGenerating QR Code...')
    time.sleep(3)
    try:
        qrCodeGenerator(user_input)
        print ('Successfully generated QR Code!\n')
    except Exception as e:
        print ('Error! Unable to generate the QR Code\n')
    
    arg = input('Do you want to scan the data inside the QR Code (Y/N): ')

    # take an argument from the user wether the user wants to get the data in the qr code
    if arg == 'Y' or arg == 'y':
        try:
            print ('\nScanning...')
            time.sleep(3)
            d = cv2.QRCodeDetector()
            img, _, _ = d.detectAndDecode(cv2.imread("D:\\Productivity\\Python\\Projects\\QRCode.jpg"))
            print ('Successfully scanned the image!\n')
            print(f"The decoded image is: {img}")
        except Exception as e:
            print ('Error! Unable to complete the scan\n')

    elif arg == 'N' or arg == 'n':
        print ('Exiting the code...')
        time.sleep(1)
        sys.exit()
