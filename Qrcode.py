#to qrcode(quick respond code) to generate you need pip(pypng, pyqrcode) to read pip(pyzbar, pillow)

#to generate
import pyqrcode

qr = pyqrcode.create('https://uplifthub.ng')
qr.png('hub.png', scale=8)


#to read QR code
from pyzbar.pyzbar import decode
from PIL import Image

d = decode(Image.open('hub.png'))

print(d[0].data.decode('ascii'))
