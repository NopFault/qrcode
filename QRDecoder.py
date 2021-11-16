import qrcode

from pyzbar import pyzbar
from PIL import Image

class QRCoder:

    def __init__(self, file:str = None, data:str = None):
        self.file = file
        self.data = data
        self.type = None

    def create_qrcode(self) -> dict:
        qr = qrcode.QRCode(version=1, box_size=20, border=6)
        qr.add_data(self.data)
        qr.make(fit=True)

        image = qr.make_image(fill_color="black", back_color="white")
        image.save(self.file)

        return {
            "data": self.data,
            "to_file": self.file
        }

    def read_qrcode(self) -> dict:
        image = Image.open(self.file)
        qr = pyzbar.decode(image)[0]
        self.data = qr.data.decode("utf-8")
        self.type = qr.type
        return {
            "from_file": self.file,
            "data_type": self.type,
            "data": self.data,
        }
