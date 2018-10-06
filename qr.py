# import qr code library
# import class Person
import qrcode
from person import Person

# Create qr code instance
qr = qrcode.QRCode(
    version = 1,
    error_correction = qrcode.constants.ERROR_CORRECT_H,
    box_size = 10,
    border = 4,
)

# the data of the QR we want to store
data = Person(first_name='Joe', last_name='Doe', address='California, L.A.', phone='1144148493', email='joedoe@example.com')

#add data
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR code instance
img = qr.make_image()

img.save(data.email + ".jpg")
