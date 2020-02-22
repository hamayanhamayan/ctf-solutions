from pyzbar.pyzbar import decode
from PIL import Image
from typing import List
import qrcode

import HHCTF.crypto as hc

def get_qr(filepath: str) -> List[str]:
  decoded = decode(Image.open(filepath))
  result = []
  for item in decoded:
    result.append(hc.to_ascii(item.data))
  return result

def make_qr(test: str, to_path: str):
  img = qrcode.make(test)
  img.save(to_path)
