import qrcode
# img = qrcode.make('Rajat Khadka')
# type(img)  # qrcode.image.pil.PilImage
# img.save("ram.png")

##wifi link qr generator
# wifi_type = "WPA"
# wifi_ssid ="StarLink!!"
# wifi_password = "g%ah92p9#"
# wifi = f"WIFI:T:{wifi_type};S:{wifi_ssid};P:{wifi_password};;"
# img = qrcode.make('wifi')
# type(img)
# img.save("wifi.png")

#qrcode to send email
# email_address = 'razat.khadka729@gmail.com'
# subject = "My First Email Using Python"
# body = " Hello, this is my first email using Python."
# mailto = f"mailto:{email_address}?subject={subject}&body={body}"
# img = qrcode.make(mailto)
# type(img)
# img.save("email.png")

# #send sms to contact
phone_number = "980808888"
message = "Hello there !"
sms = f"SMSTO:{phone_number}:{message}"
img = qrcode.make(sms)
type(img)
img.save("sms.png")
