import base45
import zlib
import cbor2
import json

from QRDecoder import QRCoder
from cose.messages import CoseMessage

qrcoder = QRCoder("GP.jpg")
rez = qrcoder.read_qrcode()

payload = rez['data'][4:]
decoded = base45.b45decode(payload)
decompressed = zlib.decompress(decoded)
cose = CoseMessage.decode(decompressed)
print(json.dumps(cbor2.loads(cose.payload), indent=2))
