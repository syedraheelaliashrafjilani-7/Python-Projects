import qrcode #pip install qrcode then import
#You can also make user input
#data = input("Enter a Link: ")
data = "https://www.youtube.com" #Give any choice of link you want to generate Qr Code
qr = qrcode.make(data) #this line of code makes qr code
qr.save("qrcode.png") #using this to save qrcode image
print("Qr Code is Created Succesfully..") 